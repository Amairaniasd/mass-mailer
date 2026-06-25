import pandas as pd

REQUIRED_COLS = {"First Name", "Last Name", "Email", "Email Status"}

def load_contacts(file) -> pd.DataFrame:
    try:
        df = pd.read_csv(file)
    except Exception:
        df = pd.read_excel(file)

    missing = REQUIRED_COLS - set(df.columns)
    if missing:
        raise ValueError(f"El archivo no tiene las columnas requeridas: {missing}")

    df = df[df["Email Status"].str.strip().str.lower() == "verified"].copy()
    df = df.dropna(subset=["Email"])
    df = df[df["Email"].str.contains("@", na=False)]
    df = df.reset_index(drop=True)

    return df


def preview_contacts(df: pd.DataFrame) -> pd.DataFrame:
    cols = ["First Name", "Last Name", "Email", "Company Name"]
    available = [c for c in cols if c in df.columns]
    return df[available].head(10)