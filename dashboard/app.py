import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# Caminhos dos dados
METRICS_PATH = Path("data/analytics/metrics")
TIME_SERIES_PATH = Path("data/analytics/time_series")

st.set_page_config(
    page_title="Intercom DataOps Dashboard",
    layout="wide"
)

st.title("📊 Intercom DataOps — Dashboard Operacional")

st.markdown("Pipeline de análise de tickets com dados sintéticos.")

# ========================
# Carregamento dos arquivos
# ========================

@st.cache_data
def load_data():
    categorias = pd.read_csv(METRICS_PATH / "tickets_por_categoria.csv")
    canais = pd.read_csv(METRICS_PATH / "tickets_por_canal.csv")
    times = pd.read_csv(METRICS_PATH / "tickets_por_time.csv")

    tickets_dia = pd.read_csv(TIME_SERIES_PATH / "tickets_por_dia.csv")
    tickets_mes = pd.read_csv(TIME_SERIES_PATH / "tickets_por_mes.csv")

    return categorias, canais, times, tickets_dia, tickets_mes

categorias, canais, times, tickets_dia, tickets_mes = load_data()

# ========================
# KPIs
# ========================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📦 Categorias", len(categorias))

with col2:
    st.metric("📱 Canais", len(canais))

with col3:
    st.metric("👥 Times", len(times))

st.divider()

# ========================
# Gráficos
# ========================

st.subheader("📌 Tickets por Categoria")
fig_cat = px.bar(
    categorias,
    x="categoria",
    y="quantidade",
    title="Distribuição por Categoria"
)
st.plotly_chart(fig_cat, use_container_width=True)

st.subheader("📌 Tickets por Canal")
fig_canal = px.bar(
    canais,
    x="canal",
    y="quantidade",
    title="Distribuição por Canal"
)
st.plotly_chart(fig_canal, use_container_width=True)

st.subheader("📌 Tickets por Time")
fig_time = px.bar(
    times,
    x="time",
    y="quantidade",
    title="Distribuição por Time"
)
st.plotly_chart(fig_time, use_container_width=True)

st.subheader("📈 Tickets por Dia")
fig_dia = px.line(
    tickets_dia,
    x="ticket_created_(america/sao_paulo)",
    y="tickets",
    title="Volume Diário de Tickets"
)
st.plotly_chart(fig_dia, use_container_width=True)

st.subheader("📆 Tickets por Mês")
fig_mes = px.line(
    tickets_mes,
    x="ticket_created_(america/sao_paulo)",
    y="tickets",
    title="Volume Mensal de Tickets"
)
st.plotly_chart(fig_mes, use_container_width=True)

st.success("✅ Dashboard atualizado com dados do pipeline.")
