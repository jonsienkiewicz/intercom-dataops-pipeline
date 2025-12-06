import pandas as pd
from pathlib import Path

PROCESSED = Path("data/processed")
OUTPUT = Path("data/analytics/time_series")
OUTPUT.mkdir(parents=True, exist_ok=True)

def load_data():
    df = pd.read_csv(PROCESSED / "all_tickets_clean.csv")
    return df

def make_time_series(df: pd.DataFrame):
    # Converter a coluna de data
    col = "ticket_created_(america/sao_paulo)"
    df[col] = pd.to_datetime(df[col], errors="coerce")

    # Criar agrupamentos
    ts_day = df.groupby(df[col].dt.date).size().reset_index(name="tickets")
    ts_month = df.groupby(df[col].dt.to_period("M")).size().reset_index(name="tickets")
    ts_month["ticket_created_(america/sao_paulo)"] = ts_month["ticket_created_(america/sao_paulo)"].astype(str)

    # Tempo médio de resolução por mês
    if "ticket_time_to_resolve_(seconds)" in df.columns:
        df["ticket_time_to_resolve_(seconds)"] = pd.to_numeric(
            df["ticket_time_to_resolve_(seconds)"], errors="coerce"
        )

        tempo_mes = (
            df.groupby(df[col].dt.to_period("M"))["ticket_time_to_resolve_(seconds)"]
            .mean()
            .reset_index(name="tempo_medio_resolucao")
        )
        tempo_mes["ticket_created_(america/sao_paulo)"] = tempo_mes["ticket_created_(america/sao_paulo)"].astype(str)
    else:
        tempo_mes = pd.DataFrame()

    return ts_day, ts_month, tempo_mes

def save(df, name):
    df.to_csv(OUTPUT / f"{name}.csv", index=False)

def main():
    print("Carregando dados...")
    df = load_data()

    print("Gerando séries temporais...")
    ts_day, ts_month, tempo_mes = make_time_series(df)

    print("Salvando arquivos...")
    save(ts_day, "tickets_por_dia")
    save(ts_month, "tickets_por_mes")

    if not tempo_mes.empty:
        save(tempo_mes, "tempo_resolucao_por_mes")

    print("✔ Sprint 4 concluída: time series geradas em data/analytics/time_series/")

if __name__ == "__main__":
    main()
