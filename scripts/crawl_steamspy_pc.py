"""
Incrementally crawl SteamSpy PC games to exactly 15,000 unique appids.

Features:
- Fast page skipping: Skips already crawled candidate pages instantly without 60s sleep.
- Clear console progress logging with flush=True.
- Checkpoints saved every 100 games.
- Resumes automatically from current row count to 15,000 rows.
"""

import os
import sys
import time
from typing import Any

import pandas as pd
import requests

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXISTING_FILE = os.path.join(PROJECT_ROOT, "data", "raw", "steamspy_games_4000.csv")
OUTPUT_FILE = os.path.join(PROJECT_ROOT, "data", "raw", "steamspy_games_15000_from_4000.csv")

TARGET_ROWS = 15_000
STEAMSPY_URL = "https://steamspy.com/api.php"
ALL_REQUEST_DELAY_SECONDS = 60
DETAIL_REQUEST_DELAY_SECONDS = 1
CHECKPOINT_EVERY = 100


def request_json(params: dict[str, Any]) -> Any:
    response = requests.get(STEAMSPY_URL, params=params, timeout=60)
    response.raise_for_status()
    return response.json()


def load_data() -> pd.DataFrame:
    source = OUTPUT_FILE if os.path.exists(OUTPUT_FILE) else EXISTING_FILE
    df = pd.read_csv(source)
    if "appid" not in df.columns:
        raise ValueError(f"Missing required column 'appid' in {source}")

    df["appid"] = pd.to_numeric(df["appid"], errors="coerce")
    df = df.dropna(subset=["appid"]).drop_duplicates("appid", keep="first")
    print(f"[INFO] Da nạp sẵn {len(df):,} dong tu {source}", flush=True)
    return df.reset_index(drop=True)


def save_checkpoint(df: pd.DataFrame) -> None:
    df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")
    print(f"[CHECKPOINT] Da luu: {len(df):,} dong vao {OUTPUT_FILE}", flush=True)


def main() -> None:
    print("=" * 60, flush=True)
    print("  STEAMSPY PC CRAWLER - EXPANSION TO 15,000 ROWS", flush=True)
    print("=" * 60, flush=True)

    df = load_data()
    if len(df) >= TARGET_ROWS:
        save_checkpoint(df.head(TARGET_ROWS))
        print(f"[HOAN TAT] Muc tieu da dat du: {TARGET_ROWS:,} dong!", flush=True)
        return

    existing_appids = set(df["appid"].astype(int).astype(str))
    new_rows: list[dict[str, Any]] = []

    # Smart resume: start around page = (existing // 1000) - 1 to avoid scanning old pages
    estimated_start_page = max(0, (len(existing_appids) // 1000) - 1)
    page = estimated_start_page
    print(f"[INFO] Bat dau quet nhanh tu trang ung vien {page} (Bo qua {estimated_start_page} trang da co)...", flush=True)

    while len(df) + len(new_rows) < TARGET_ROWS:
        print(f"\n-> Dang tai danh sach SteamSpy trang {page}...", flush=True)
        try:
            candidates = request_json({"request": "all", "page": page})
        except requests.RequestException as exc:
            print(f"[CANH BAO] Loi khi tai trang {page}: {exc}. Thu lai sau 5s...", flush=True)
            time.sleep(5)
            continue

        if not isinstance(candidates, dict) or not candidates:
            print("[INFO] Khong con game nao tra ve tu SteamSpy.", flush=True)
            break

        # Check how many new games are in this page
        new_in_page = [str(aid) for aid in candidates if str(aid) not in existing_appids]
        print(f"   Trang {page} co {len(candidates)} game ({len(new_in_page)} game moi chua co trong dataset).", flush=True)

        if not new_in_page:
            # If all games on this page are already in dataset, skip immediately without 60s delay!
            print(f"   -> Toan bo game tren trang {page} da co, chuyen ngay sang trang tiep theo...", flush=True)
            page += 1
            time.sleep(0.5)
            continue

        # Process games on this page
        for appid in new_in_page:
            try:
                detail = request_json({"request": "appdetails", "appid": appid})
                time.sleep(DETAIL_REQUEST_DELAY_SECONDS)
            except requests.RequestException as exc:
                print(f"   Bo qua appid={appid}: {exc}", flush=True)
                continue

            if not isinstance(detail, dict) or not detail.get("name"):
                continue

            detail["appid"] = int(appid)
            new_rows.append(detail)
            existing_appids.add(appid)

            total = len(df) + len(new_rows)
            print(f"Added {total:,}/{TARGET_ROWS:,}: {detail['name']}", flush=True)

            if len(new_rows) % CHECKPOINT_EVERY == 0:
                df = pd.concat([df, pd.DataFrame(new_rows)], ignore_index=True)
                df = df.drop_duplicates("appid", keep="first")
                new_rows = []
                save_checkpoint(df)

            if len(df) + len(new_rows) >= TARGET_ROWS:
                break

        page += 1
        if len(df) + len(new_rows) < TARGET_ROWS:
            print(f"   -> Tam nghi {ALL_REQUEST_DELAY_SECONDS}s giua 2 trang danh sach de dam bao quy dinh SteamSpy...", flush=True)
            time.sleep(ALL_REQUEST_DELAY_SECONDS)

    if new_rows:
        df = pd.concat([df, pd.DataFrame(new_rows)], ignore_index=True)

    df = df.drop_duplicates("appid", keep="first").head(TARGET_ROWS)
    save_checkpoint(df)
    print("\n" + "=" * 60, flush=True)
    print(f"[HOAN TAT XUAT SAC] Da dat du {len(df):,} dong!", flush=True)
    print(f"File luu tai: {OUTPUT_FILE}", flush=True)
    print("=" * 60, flush=True)


if __name__ == "__main__":
    main()