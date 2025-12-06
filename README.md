<p align="center">
  <img src="assets/banner-intercom-dataops.png" width="100%" alt="Intercom DataOps Banner"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python"/>
  <img src="https://img.shields.io/badge/DataOps-Pipeline-orange"/>
  <img src="https://img.shields.io/badge/Status-Ativo-brightgreen"/>
  <img src="https://img.shields.io/badge/Autor-Jonathan_Sienkiewicz-6aa84f"/>
</p>

# Intercom DataOps — Pipeline de Dados Operacionais  
### Autor: Jonathan Santos de Jesus Sienkiewicz  
### Período: 2025  
---

Este projeto implementa um pipeline completo de **DataOps**, desde a ingestão de dados exportados da Intercom até a geração de métricas, séries temporais, análises operacionais e exportação consolidada para um **Data Lake local**.

O objetivo é demonstrar domínio prático em:

- `ETL / Data Cleaning`
- `Métricas Operacionais`
- `Time Series`
- `Design de Pipeline`
- `Data Lake`
- Organização do projeto com boas práticas de Engenharia de Dados

---

# Arquitetura do Pipeline

(ASCII diagram — use como referência visual)

    ┌─────────────────────────┐
    │       Intercom CSVs     │
    └─────────────┬───────────┘
                  │
            Ingestão Manual
                  │
    ┌─────────────▼───────────┐
    │       data/raw/         │
    └─────────────┬───────────┘
                  │
       Limpeza e Padronização
                  │
    ┌─────────────▼───────────┐
    │    data/processed/      │
    └─────────────┬───────────┘
                  │
         Métricas e Time Series
                  │
    ┌─────────────▼───────────┐
    │    data/analytics/      │
    └─────────────┬───────────┘
                  │
            Exportação Final
                  │
    ┌─────────────▼───────────┐
    │     data/datalake/      │
    └─────────────────────────┘

---

# 📁 Estrutura Geral do Projeto

`projeto-intercom-dataops/`

- `data/`
  - `raw/`               → CSVs originais da Intercom
  - `processed/`         → Dados limpos e padronizados
  - `analytics/`
    - `metrics/`         → Métricas operacionais
    - `time_series/`     → Séries temporais
  - `datalake/`          → Data Lake local consolidado
- `data/cleaning/`       → Scripts de limpeza
  - `clean_tickets.py`
- `data/analytics/`      → Scripts analíticos
  - `metrics.py`
  - `time_series.py`
- `data/export/`
  - `export_to_datalake.py`
- `assets/`              → Banner e imagens
- `requirements.txt`
- `README.md`

---

# 🚀 Sprints do Projeto

## Sprint 1 — Configuração Inicial & Ingestão
- Organização da estrutura do repositório.
- Padronização de diretórios no padrão DataOps.
- Ingestão manual dos CSVs exportados da Intercom em `data/raw/`.
- Criação do repositório Git e branch de desenvolvimento.

## Sprint 2 — Data Cleaning (Limpeza e Padronização)
**Arquivo principal:** `data/cleaning/clean_tickets.py`

Principais passos executados:
- Normalização de nomes de colunas (snake_case).
- Conversão rigorosa de tipos (datas, numéricos, strings).
- Padronização de datas com `pd.to_datetime(..., errors='coerce')`.
- Remoção de ruído textual: valores como `"nan"`, `"None"`, `"<NA>"`.
- Trim de campos textuais (`.str.strip()`).

Regra aplicada (exemplo):
- `df[c] = df[c].astype("string").str.strip().replace({"nan": None, "None": None, "<NA>": None})`

Verificações automáticas:
- Checagem de colunas esperadas.
- Identificação de campos críticos vazios.
- Validação de datas.

**Output:** `data/processed/all_tickets_clean.csv`

## Sprint 3 — Métricas Operacionais (KPIs)
**Arquivo:** `data/analytics/metrics.py`

KPIs implementados:
- `total_tickets`
- `tickets por categoria`
- `tickets por canal`
- `tickets por time responsável`
- Validação da coluna `ticket_time_to_resolve_(seconds)` (existência e completude)

**Output:** arquivos em `data/analytics/metrics/`  
Exemplos:
- `total_tickets.txt`
- `tickets_por_categoria.csv`
- `tickets_por_canal.csv`
- `tickets_por_time.csv`

## Sprint 4 — Séries Temporais (Time Series)
**Arquivo:** `data/analytics/time_series.py`

Gera:
- `tickets_por_dia.csv`
- `tickets_por_mes.csv`
- `tempo_resolucao_por_mes.csv` (quando dados de resolução disponíveis)

**Output:** `data/analytics/time_series/`

## Sprint 5 — Exportação para Data Lake Local
**Arquivo:** `data/export/export_to_datalake.py`

Funcionalidade:
- Replica `processed/` e `analytics/` para `data/datalake/`
- Mantém hierarquia e nomes
- Simula um Data Lake (prévia local para S3/GCS)

Estrutura final gerada:
- `data/datalake/processed/`
- `data/datalake/analytics/metrics/`
- `data/datalake/analytics/time_series/`

---

# 🏁 Status Atual do Projeto

- Pipeline funcional de ponta a ponta
- Dados limpos e padronizados
- Métricas consolidadas
- Séries temporais geradas
- Data Lake local atualizado
- Próximo objetivo: **Sprint 6 — Dashboard & Integração com API da Intercom**

---

# 📦 Requisitos

Coloque no `requirements.txt`:

- `pandas`
- `numpy`
- `python-dotenv`

(Instale com `pip install -r requirements.txt`)

---

# 📌 Próximos Passos (Sprint 6+)

- Criar dashboard (Looker Studio / Streamlit / PowerBI)
- Ingestão automática pela API da Intercom
- Modelagem dimensional (fato + dimensões)
- Automatizar pipeline (Cron / Airflow / Prefect)
- Alerts e monitoramento (Slack / Prometheus / Grafana)

---

# 📜 Licença

Projeto de estudo e demonstração técnica.  
Uso livre para fins educacionais.

Todos os datasets utilizados neste repositório são integralmente sintéticos, criados apenas para fins acadêmicos e não representam dados reais de usuários, clientes, empresas ou sistemas. Não há qualquer dado sensível neste repositório.