import sys
import pandas as pd
import numpy as np
import os

if sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
REV_PATH = os.path.join(PROJECT_ROOT, "data", "external", "genre_revenue_2024_2025.csv")
DL_PATH = os.path.join(PROJECT_ROOT, "data", "external", "genre_downloads_2024_2025.csv")
OUTPUT_PATH = os.path.join(PROJECT_ROOT, "data", "processed", "genre_arpu_benchmark.csv")


def calculate_arpu_table():
    if not os.path.exists(REV_PATH):
        raise FileNotFoundError()
    if not os.path.exists(DL_PATH):
        raise FileNotFoundError()

    df_rev = pd.read_csv(REV_PATH)
    df_dl = pd.read_csv(DL_PATH)

    df = pd.merge(
        df_rev,
        df_dl,
        on="Genre",
        how="inner",
        validate="one_to_one",
        suffixes=("_revenue", "_downloads"),
    )

    df["Revenue_per_Download_Mobile"] = (
        df["Mobile_Revenue_2025_USD_Billion"] / df["Mobile_Downloads_2025_Billion"]
    ).round(2)

    df["Revenue_per_Download_PC_Steam"] = np.where(
        df["Steam_Downloads_2025_Million"].fillna(0) > 0,
        (df["Steam_Revenue_2025_USD_Billion"] * 1000) / df["Steam_Downloads_2025_Million"],
        0.0,
    ).round(2)

    return df[
        ["Genre", "Revenue_per_Download_Mobile", "Revenue_per_Download_PC_Steam"]
    ].copy()


def get_arpu(platform="pc"):
    df = calculate_arpu_table()
    p = platform.lower()

    if p in ["pc", "steam"]:
        return df.set_index("Genre")["Revenue_per_Download_PC_Steam"].to_dict()
    elif p == "mobile":
        return df.set_index("Genre")["Revenue_per_Download_Mobile"].to_dict()
    else:
        raise ValueError("platform phai la 'pc', 'steam', hoac 'mobile'")


def get_overall_arpu():
    df_rev = pd.read_csv(REV_PATH)
    df_dl = pd.read_csv(DL_PATH)
    df = pd.merge(df_rev, df_dl, on="Genre")

    overall_mobile = (
        df["Mobile_Revenue_2025_USD_Billion"].sum() / df["Mobile_Downloads_2025_Billion"].sum()
    ).round(2)

    overall_pc = (
        (df["Steam_Revenue_2025_USD_Billion"].sum() * 1000)
        / df["Steam_Downloads_2025_Million"].sum()
    ).round(2)

    return {
        "mobile": float(overall_mobile),
        "pc_steam": float(overall_pc),
    }


def apply_arpu(df, genre_col="Genre", platform="pc", target_col=None):
    df_out = df.copy()
    arpu_map = get_arpu(platform=platform)

    p_name = "PC" if platform.lower() in ["pc", "steam"] else "Mobile"
    col_name = target_col or f"ARPU_{p_name}_USD"

    df_out[col_name] = df_out[genre_col].map(arpu_map)

    # Impute missing genres with median
    median_val = float(pd.Series(list(arpu_map.values())).median())
    df_out[col_name] = df_out[col_name].fillna(median_val)
    return df_out


if __name__ == "__main__":
    df_arpu = calculate_arpu_table()
    overall = get_overall_arpu()

    df_arpu.to_csv(OUTPUT_PATH, index=False, encoding="utf-8-sig")
