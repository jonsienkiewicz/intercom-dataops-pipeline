import pandas as pd
import numpy as np


def clean_text_fields(df: pd.DataFrame):
    text_cols = df.select_dtypes(include=["object", "string"]).columns
    print(f"Limpando textos em {len(text_cols)} colunas...")

    for c in text_cols:
        # Converte tudo para string
        df[c] = df[c].astype("string").str.strip()

        # Remove valores "nan" textuais
        df[c] = df[c].replace({"nan": None, "None": None, "<NA>": None})

    return df


def main():
    print("Carregando data/processed/all_tickets.csv...")
    df = pd.read_csv("data/processed/all_tickets.csv")

    # -----------------------------
    # 1. Padronização de nomes
    # -----------------------------
    print("Padronizando nomes de coluna...")
    df.columns = (
        df.columns.str.lower()
        .str.strip()
        .str.replace(" ", "_")
        .str.replace(".", "_")
    )

    print("Removendo colunas duplicadas...")
    df = df.loc[:, ~df.columns.duplicated()]


    # -----------------------------
    # 2. Remoção de colunas vazias
    # -----------------------------
    empty_cols = [c for c in df.columns if df[c].isna().all()]
    if empty_cols:
        print(f"Removendo colunas totalmente vazias: {empty_cols}")
        df = df.drop(columns=empty_cols)

    # -----------------------------
    # 3. Converter datas
    # -----------------------------
    date_cols = [
        c for c in df.columns
        if "created" in c or "updated" in c
    ]
    print(f"Convertendo colunas de data: {date_cols}")

    for c in date_cols:
        df[c] = pd.to_datetime(df[c], errors="coerce")

    # -----------------------------
    # 4. Limpeza de texto
    # -----------------------------
    df = clean_text_fields(df)

    # -----------------------------
    # 5. Salvar
    # -----------------------------
    output_path = "data/processed/all_tickets_clean.csv"
    df.to_csv(output_path, index=False)
    print(f"Arquivo limpo salvo em: {output_path}")


if __name__ == "__main__":
    main()

