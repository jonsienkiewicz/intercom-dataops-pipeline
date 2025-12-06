import pandas as pd
from pathlib import Path

PROCESSED = Path("data/processed")
OUTPUT = Path("data/analytics/metrics")
OUTPUT.mkdir(parents=True, exist_ok=True)


def load_data():
    df = pd.read_csv(PROCESSED / "all_tickets_clean.csv")
    return df


def compute_basic_metrics(df: pd.DataFrame):
    metrics = {}

    metrics["total_tickets"] = len(df)

    metrics["tickets_por_categoria"] = (
        df["ticket_category"]
        .value_counts(dropna=False)
        .rename_axis("categoria")
        .reset_index(name="quantidade")
    )

    metrics["tickets_por_canal"] = (
        df["channel"]
        .value_counts(dropna=False)
        .rename_axis("canal")
        .reset_index(name="quantidade")
    )

    metrics["tickets_por_time"] = (
        df["team_currently_assigned"]
        .value_counts(dropna=False)
        .rename_axis("time")
        .reset_index(name="quantidade")
    )

    return metrics


def save_metrics(metrics: dict):
    for name, df in metrics.items():
        if isinstance(df, pd.DataFrame):
            df.to_csv(OUTPUT / f"{name}.csv", index=False)
        else:
            with open(OUTPUT / f"{name}.txt", "w") as f:
                f.write(str(df))


def check_resolution_time(df: pd.DataFrame):
    col = "ticket_time_to_resolve_(seconds)"

    if col not in df.columns:
        print(f"⚠ Coluna '{col}' não existe!")
        return

    if df[col].isna().all():
        print("⚠ Todos os valores de tempo de resolução estão vazios (NaN).")
    else:
        print("✔ Coluna de tempo de resolução tem dados válidos.")


def main():
    print("Carregando dados...")
    df = load_data()

    check_resolution_time(df)

    print("Calculando métricas...")
    metrics = compute_basic_metrics(df)

    print("Salvando métricas...")
    save_metrics(metrics)

    print("✔ Sprint 3 concluída: métricas geradas em data/analytics/metrics/")


if __name__ == "__main__":
    main()
