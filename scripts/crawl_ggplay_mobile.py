import os
import sys
import time
import re
import socket
import pandas as pd
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from concurrent.futures import ThreadPoolExecutor, as_completed

# Patch google_play_scraper _urlopen with real browser User-Agent to prevent HTTP 429
import google_play_scraper.utils.request as _gps_req
from google_play_scraper.exceptions import NotFoundError, ExtraHTTPError
from google_play_scraper import search, app

_CHROME_UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

def _custom_urlopen(obj):
    if isinstance(obj, str):
        obj = Request(obj, headers={"User-Agent": _CHROME_UA})
    elif hasattr(obj, "add_header"):
        obj.add_header("User-Agent", _CHROME_UA)
    try:
        resp = urlopen(obj, timeout=10)
    except HTTPError as e:
        if e.code == 404:
            raise NotFoundError("App not found(404).")
        else:
            raise ExtraHTTPError(f"Status code {e.code} returned.")
    return resp.read().decode("UTF-8")

_gps_req._urlopen = _custom_urlopen

socket.setdefaulttimeout(10)

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_FILE = os.path.join(PROJECT_ROOT, "data", "raw", "mobile_playstore_games_10000+.csv")

TARGET_TOTAL_ROWS = 15000
MAX_WORKERS = 8
CHECKPOINT_EVERY = 50


def clean_text(text: str) -> str:
    if not text:
        return ""
    clean = re.sub(r"<[^>]+>", " ", text)
    clean = re.sub(r"\s+", " ", clean).strip()
    return clean[:350]


def get_existing_data():
    if os.path.exists(OUTPUT_FILE):
        df = pd.read_csv(OUTPUT_FILE)

        # STRICT: Chỉ giữ lại ứng dụng thuộc nhóm GAME_ (bắt đầu bằng GAME_)
        if "genre_id" in df.columns:
            df["genre_id"] = df["genre_id"].astype("string").str.strip().str.upper()
            before = len(df)
            df = df[df["genre_id"].str.startswith("GAME_", na=False)].copy()
            if len(df) != before:
                print(f"[INFO] Da loai {before - len(df)} dong khong phai game trong file cu.", flush=True)
                df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")

        df = df.drop_duplicates(subset=["app_id"]).reset_index(drop=True)
        print(f"[INFO] Tim thay file dich {OUTPUT_FILE} co {len(df):,} game hop le.", flush=True)
        return df, set(df["app_id"].dropna().tolist())
    return pd.DataFrame(), set()


def generate_search_queries() -> list[str]:
    themes = [
        "car", "bike", "truck", "bus", "train", "flight", "plane", "helicopter", "boat", "ship",
        "tank", "gun", "sniper", "shooting", "shooter", "war", "battle", "combat", "strike", "army",
        "zombie", "alien", "monster", "dinosaur", "dragon", "ninja", "samurai", "knight", "robot",
        "superhero", "stickman", "warrior", "hunter", "runner", "jump", "parkour", "racing", "drift",
        "parking", "traffic", "crash", "farm", "farming", "ranch", "garden", "animal", "pet", "cat",
        "dog", "horse", "fish", "fishing", "hunting", "cooking", "chef", "restaurant", "cafe", "bakery",
        "burger", "pizza", "hotel", "hospital", "doctor", "police", "builder", "construction", "craft",
        "crafting", "mining", "survival", "horror", "scary", "ghost", "escape", "room", "prison",
        "detective", "mystery", "puzzle", "riddle", "brain", "match 3", "tile", "block", "bubble",
        "ball", "brick", "blast", "pop", "color", "merge", "drawing", "coloring", "card", "poker",
        "solitaire", "blackjack", "casino", "slots", "domino", "ludo", "chess", "checkers", "board",
        "dice", "word", "crossword", "trivia", "quiz", "music", "piano", "magic", "fantasy", "dungeon",
        "tower", "castle", "kingdom", "empire", "city", "island", "idle", "tycoon", "clicker", "simulator",
        "rpg", "mmo", "mmorpg", "strategy", "tactics", "action", "adventure", "arcade", "retro", "classic",
        "sports", "football", "soccer", "basketball", "cricket", "baseball", "tennis", "golf", "pool",
        "billiards", "bowling", "boxing", "wrestling", "mma", "karate", "skate", "ski", "surf"
    ]

    studios = [
        "voodoo", "ketchapp", "saygames", "zynga", "gameloft", "supercell",
        "rovio", "ubisoft", "miniclip", "habby", "netmarble", "krafton",
        "tencent", "mihoyo", "playrix", "king", "bandai namco", "capcom",
        "sega", "konami", "niantic", "nexon", "activision", "riot games",
        "chillingo", "flaregames", "ironhide", "ninja kiwi", "halfbrick",
        "glu mobile", "nordcurrent", "gamevil", "playgendary", "lion studios",
        "outfit7", "moonton", "innogames", "yotta games", "lilith games", "igg",
        "garena", "tomy", "fingersoft", "supercent", "kwalee", "homa games",
        "square enix", "yostar", "nintendo", "level infinite", "devsisters"
    ]

    queries = []

    # 1. Themes x Modifiers (đa dạng hoá truy vấn game thực tế)
    for t in themes:
        for m in ["simulator", "game", "games", "3d", "offline", "multiplayer", "legends", "clash", "quest", "warfare"]:
            queries.append(f"{t} {m}")

    # 2. Studios
    for s in studios:
        queries.append(f"games by {s}")

    # 3. Top / Best
    for t in themes:
        queries.append(f"best {t} games")
        queries.append(f"top {t} games 2024")

    # 4. Quốc tế
    intl = [
        "juegos gratis", "juegos de accion", "juegos de carreras", "juegos de autos",
        "jogos gratis", "jogos de corrida", "jogos de tiro", "jeux gratuits",
        "kostenlose spiele", "game ban sung", "game dua xe", "game chien thuat",
        "tro choi offline", "game vui", "game offline hay", "juegos rpg", "juegos puzzle",
        "jeux de voiture", "jogos de zumbi", "juegos de guerra", "juegos de aventura",
        "juegos de disparos", "jogos de futebol", "juegos de futbol", "giochi gratis",
        "giochi di corse", "jeu de tir", "jeu d action", "jeu de strategie"
    ]
    queries.extend(intl)

    return list(dict.fromkeys(queries))


def fetch_single_app(app_id: str) -> dict | None:
    try:
        info = app(app_id, lang="en", country="us")
        if not info:
            return None

        # BẮT BUỘC: Kiểm tra genreId phải bắt đầu bằng 'GAME_'
        genre_id = str(info.get("genreId") or "").strip().upper()
        if not genre_id.startswith("GAME_"):
            return None

        real_installs = info.get("realInstalls") or 0
        score = info.get("score") or 0.0

        released = info.get("released")
        release_year = None
        if released:
            match = re.search(r"\b(20\d\d|19\d\d)\b", str(released))
            if match:
                release_year = float(match.group(1))

        row = {
            "app_id": str(info.get("appId") or app_id),
            "title": str(info.get("title") or ""),
            "genre": str(info.get("genre") or ""),
            "genre_id": genre_id,
            "realInstalls": int(real_installs),
            "min_installs": int(info.get("minInstalls") or 0),
            "installs_range": str(info.get("installs") or "0+"),
            "score": round(float(score), 2),
            "ratings": int(info.get("ratings") or 0),
            "reviews": int(info.get("reviews") or 0),
            "price_usd": float(info.get("price") or 0.0),
            "is_free": bool(info.get("free", True)),
            "currency": str(info.get("currency") or "USD"),
            "offersIAP": bool(info.get("offersIAP", False)),
            "inAppProductPrice": str(info.get("inAppProductPrice") or ""),
            "developer": str(info.get("developer") or "Unknown"),
            "developer_id": str(info.get("developerId") or ""),
            "released": str(released or ""),
            "release_year": release_year,
            "version": str(info.get("version") or ""),
            "content_rating": str(info.get("contentRating") or "Everyone"),
            "description": clean_text(info.get("description") or ""),
            "playstore_url": str(info.get("url") or f"https://play.google.com/store/apps/details?id={app_id}"),
        }
        return row
    except Exception:
        return None


def save_checkpoint(df_base: pd.DataFrame, new_rows: list[dict]) -> pd.DataFrame:
    if new_rows:
        df_new = pd.DataFrame(new_rows)
        df_combined = pd.concat([df_base, df_new], ignore_index=True)
    else:
        df_combined = df_base

    df_combined = df_combined.drop_duplicates(subset=["app_id"]).reset_index(drop=True)
    df_combined.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")
    print(f"[CHECKPOINT] Da luu: {len(df_combined):,} dong vao {OUTPUT_FILE}", flush=True)
    return df_combined


def main():
    print("=" * 60, flush=True)
    print("  GOOGLE PLAY STORE CRAWLER - STREAMING EXPANSION TO 15,000", flush=True)
    print("=" * 60, flush=True)

    df_base, existing_app_ids = get_existing_data()
    total_count = len(existing_app_ids)

    if total_count >= TARGET_TOTAL_ROWS:
        print(f"[HOAN TAT] Dataset da dat du {total_count:,}/{TARGET_TOTAL_ROWS:,} dong!", flush=True)
        return

    needed = TARGET_TOTAL_ROWS - total_count
    print(f"[INFO] Hien tai: {total_count:,} game. Can cao them: {needed:,} game nua de dat 15,000.", flush=True)

    queries = generate_search_queries()
    print(f"[INFO] Kho truy van gom {len(queries):,} tu khoa.", flush=True)

    new_rows = []
    seen_in_run = set()
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        for q_idx, q in enumerate(queries, 1):
            if total_count >= TARGET_TOTAL_ROWS:
                break

            # Search with custom User-Agent
            try:
                results = search(q, lang="en", country="us", n_hits=30)
            except Exception as e:
                time.sleep(1.0)
                continue

            # Filter candidates not yet in dataset
            candidates = []
            for r in results:
                aid = r.get("appId")
                if aid and aid not in existing_app_ids and aid not in seen_in_run:
                    seen_in_run.add(aid)
                    candidates.append(aid)

            if not candidates:
                time.sleep(0.1)
                continue

            # Fetch details concurrently
            futures = [executor.submit(fetch_single_app, aid) for aid in candidates]
            for f in as_completed(futures):
                row = f.result()
                if row and row["genre_id"].startswith("GAME_") and row["app_id"] not in existing_app_ids:
                    existing_app_ids.add(row["app_id"])
                    new_rows.append(row)
                    total_count += 1

                    elapsed = time.time() - start_time
                    speed = len(new_rows) / elapsed if elapsed > 0 else 0
                    print(
                        f"Added {total_count:,}/{TARGET_TOTAL_ROWS:,}: {row['title'][:32]} "
                        f"({row['genre_id']}) | Installs: {row['realInstalls']:,} | {speed:.1f} g/s",
                        flush=True,
                    )

                    if len(new_rows) % CHECKPOINT_EVERY == 0:
                        df_base = save_checkpoint(df_base, new_rows)
                        new_rows = []

                    if total_count >= TARGET_TOTAL_ROWS:
                        break

            time.sleep(0.2)

    # Final save
    df_final = save_checkpoint(df_base, new_rows)
    print("\n" + "=" * 60, flush=True)
    print(f"[HOAN TAT XUAT SAC] Dataset Play Store da dat: {len(df_final):,} dong hop le!", flush=True)
    print(f"File luu tai: {OUTPUT_FILE}", flush=True)
    print("=" * 60, flush=True)


if __name__ == "__main__":
    main()
