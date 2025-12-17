# Auditoria do Dataset — Abril

## 1. Visão Geral
O dataset contém registros de tickets resolvidos por um time operacional de uma fintech durante o mês de abril.
Cada linha representa um ticket único, identificado por um ID, e reflete apenas tickets efetivamente resolvidos pela equipe analisada.

## 2. Estrutura do Dataset
O dataset possui colunas relacionadas a:
- Identificação do ticket (ID)
- Datas e horários de criação e resolução
- Responsável pela resolução
- Origem do ticket
- Sinalizações de erro operacional na abertura
- Título do ticket

Essas colunas permitem análises temporais, operacionais, de qualidade de processo e quantidade por tipo de ticket.

## 3. Colunas Relevantes para o Negócio
As colunas consideradas críticas são:
- Data/hora de criação do ticket
- Data/hora de resolução do ticket
- Analista responsável pela resolução
- Origem do ticket
- Indicador de erro operacional
- Título do ticket

Esses campos viabilizam métricas de volume, tempo de resolução, qualidade operacional, origem de demanda e quantidade por tipo de demanda.

## 4. Problemas Estruturais Identificados
Foram observados os seguintes pontos:
- Existência de colunas com nomes semanticamente semelhantes, porém com funções distintas
- Presença de colunas com alto volume de valores nulos
- Campos cujo nome não representa claramente seu significado operacional

Esses fatores exigem padronização e limpeza antes da análise.

## 5. Riscos Analíticos
- O dataset inclui apenas tickets resolvidos, excluindo casos escalados ou não finalizados
- Possível viés humano na marcação de erros operacionais
- Limitação temporal ao mês de abril, impedindo conclusões de longo prazo

## 6. Hipóteses Iniciais de Valor
- Identificação de falhas recorrentes de automação
- Crescimento de determinadas demandas operacionais ao longo do período
- Análise do tempo de resolução como indicador de eficiência operacional da equipe
