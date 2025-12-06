import pandas as pd

def load_data():
    print("Carregando data/processed/all_tickets_clean.csv...")
    df = pd.read_csv("data/processed/all_tickets_clean.csv")
    return df


def analyze_basic_metrics(df):
    print("\n===== MÉTRICAS GERAIS =====")

    # Garantir que a coluna seja numérica
    df["ticket_time_to_resolve_(seconds)"] = pd.to_numeric(
        df["ticket_time_to_resolve_(seconds)"], errors="coerce"
    )

    total_tickets = len(df)
    canais = df["channel"].value_counts(dropna=False)
    categorias = df["ticket_category"].value_counts(dropna=False)
    times_assign = df["team_currently_assigned"].value_counts(dropna=False)

    medias_resolucao = df["ticket_time_to_resolve_(seconds)"].mean()
    mediana_resolucao = df["ticket_time_to_resolve_(seconds)"].median()
    max_resolucao = df["ticket_time_to_resolve_(seconds)"].max()
    min_resolucao = df["ticket_time_to_resolve_(seconds)"].min()

    print(f"Total de tickets: {total_tickets}")

    print("\nTickets por canal:")
    print(canais)

    print("\nTickets por categoria:")
    print(categorias)

    print("\nTickets por time responsável:")
    print(times_assign)

    print(f"\nTempo médio de resolução (segundos): {medias_resolucao:.2f}")
    print(f"Mediana: {mediana_resolucao:.2f}")
    print(f"Min: {min_resolucao}")
    print(f"Max: {max_resolucao}")



def analyze_sinalizacoes(df):
    print("\n===== ANÁLISE DE SINALIZAÇÕES =====")

    sinal_cols = [c for c in df.columns if "sinalização" in c]

    print(f"Encontradas {len(sinal_cols)} colunas de sinalização:")

    for col in sinal_cols:
        print(f"\n--- {col} ---")
        print(df[col].value_counts(dropna=False))


def analyze_estados(df):
    print("\n===== ESTADOS DO TICKET =====")
    estados = df["current_ticket_state_category"].value_counts(dropna=False)
    print(estados)


def analyze_tempo_resolucao(df):
    print("\n===== TEMPO DE RESOLUÇÃO =====")
    df["ticket_time_to_resolve_(seconds)"] = pd.to_numeric(
        df["ticket_time_to_resolve_(seconds)"], errors="coerce"
    )
    print(df["ticket_time_to_resolve_(seconds)"].describe())


def main():
    df = load_data()

    analyze_basic_metrics(df)
    analyze_sinalizacoes(df)
    analyze_estados(df)
    analyze_tempo_resolucao(df)


if __name__ == "__main__":
    main()
