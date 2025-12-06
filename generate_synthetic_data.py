import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta
import os
import random

fake = Faker("pt_BR")

# ================================
# CONFIGURAÇÕES
# ================================
NUM_ROWS = 500
OUTPUT_FOLDER = "data/raw/"
APRIL_YEAR = 2024
MAY_YEAR = 2024

# Reproduz o número de colunas Sinalização Operacional detectado no seu arquivo (30+)
SIGNAL_COLS = [
    f"Sinalização Operacional {i+1}" for i in range(30)
]

# Todas as colunas do arquivo real
COLUMNS = [
    "Conversation ID",
    "Ticket created (America/Sao_Paulo)",
    "Channel",
    "Created by",
    "Created via",
    "Current conversation state",
    "Last teammate rating",
    "Resolved by",
    "Started by",
    "Ticket title",
    "Ticket type",
    "Ticket URL",
    "User participant IDs",
    "User participant names",
    "Current ticket custom state",
    "Current ticket state category",
    "Conversation created at (America/Sao_Paulo)",
    "Conversation updated at (America/Sao_Paulo)",
    "Ticket last resolved (America/Sao_Paulo)",
    "Fin AI Agent rating",
    "Fin AI Agent rating remark",
    "Teammate currently assigned",
    "Teammate currently assigned ID",
    "Team currently assigned",
    "Team currently assigned ID",
    "Ticket time to resolve (seconds)",
    "Ticket category",
    "hackwill_llm_response",
    "E como você avalia o seu atendimento?",
    "hackwill_contact",
    "Resultado da análise",
] + SIGNAL_COLS


# ================================
# FUNÇÕES AUXILIARES
# ================================

def random_datetime(month, year):
    """Gera uma data aleatória dentro de um mês."""
    start = datetime(year, month, 1)
    end = datetime(year, month, 28)
    return fake.date_time_between(start_date=start, end_date=end, tzinfo=None)


def generate_row(month, year):
    """Gera uma linha completamente sintética e coerente."""
    created_at = random_datetime(month, year)
    updated_at = created_at + timedelta(minutes=random.randint(5, 200))
    resolved_at = updated_at + timedelta(minutes=random.randint(10, 500))

    conversation_id = fake.unique.random_int(min=100000, max=999999)

    channel = random.choice(["Email", "Chat", "In-App", "Help Center"])
    ticket_type = random.choice(["issue", "question", "task"])
    category = random.choice(["Pagamento", "Conta", "Cartão", "Transferência", "Cadastro"])

    # Tempo de resolução realista
    ttr_seconds = int((resolved_at - created_at).total_seconds())

    signal_values = [random.choice(["OK", "Atenção", None]) for _ in SIGNAL_COLS]

    row = [
        conversation_id,
        created_at,
        channel,
        fake.first_name(),
        random.choice(["customer", "bot", "agent"]),
        random.choice(["open", "closed", "snoozed"]),
        random.choice([None, "positive", "negative", "neutral"]),
        fake.first_name(),
        fake.first_name(),
        fake.sentence(nb_words=5),
        ticket_type,
        f"https://app.intercom.com/tickets/{conversation_id}",
        str(fake.random_int(min=10, max=99)),
        fake.name(),
        random.choice(["Backoffice", "N2", "N1"]),
        random.choice(["Operacional", "Crítico", "Normal"]),
        created_at,
        updated_at,
        resolved_at,
        random.choice([None, 1, 2, 3, 4, 5]),
        random.choice([None, "bom", "ruim", "neutro"]),
        fake.first_name(),
        fake.random_int(min=1000, max=9000),
        random.choice(["Backoffice", "Operações", "Suporte"]),
        fake.random_int(min=1, max=10),
        ttr_seconds,
        category,
        fake.sentence(nb_words=8),
        random.choice([None, "1", "2", "3", "4", "5"]),
        fake.email(),
        random.choice(["Correto", "Incorreto", "Revisar"]),
    ] + signal_values

    return row


def generate_dataset(month, year, filename):
    rows = [generate_row(month, year) for _ in range(NUM_ROWS)]

    df = pd.DataFrame(rows, columns=COLUMNS)

    # Criar pasta caso não exista
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    output_path = os.path.join(OUTPUT_FOLDER, filename)
    df.to_csv(output_path, index=False, encoding="utf-8-sig")

    print(f"✔ Arquivo gerado: {output_path}")


# ================================
# EXECUÇÃO
# ================================

print("\nGerando dados sintéticos profissionais...\n")

generate_dataset(4, APRIL_YEAR, "sintetico_abril.csv")
generate_dataset(5, MAY_YEAR, "sintetico_maio.csv")

print("\n🎉 Dados sintéticos prontos! Segurança 100%.")
