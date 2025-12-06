import pandas as pd
import os
from pathlib import Path

# Diretórios
RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

def load_raw_data():
    csv_files = list(RAW_DIR.glob("*.csv"))

    if not csv_files:
        print("Nenhum arquivo CSV encontrado em data/raw/.")
        return None

    dataframes = []

    for file in csv_files:
        print(f"Carregando {file}...")
        df = pd.read_csv(file)
        df["source_file"] = file.name  # ajuda no debug
        dataframes.append(df)

    combined_df = pd.concat(dataframes, ignore_index=True)
    return combined_df

def save_processed_data(df):
    output_path = PROCESSED_DIR / "all_tickets.csv"
    df.to_csv(output_path, index=False)
    print(f"Arquivo salvo em: {output_path}")

if __name__ == "__main__":
    df = load_raw_data()
    if df is not None:
        save_processed_data(df)
