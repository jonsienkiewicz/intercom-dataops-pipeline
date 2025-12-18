# Schema Canônico — Tickets Intercom (Processed)

## 1. Objetivo do Dataset
O objetivo primário do dataset é proporcionar uma apresentação mensal de produtividade da equipe. Como objetivos secundários, analisaremos que tipo de demanda/ticket demonstra sinais de crescimento e também quais são os desvios operacionais mais frequentes. Tudo isso para melhorar a tomada de decisão dos times de CS e de desenvolvimentro do bot de atendimento do chat.

## 2. Granularidade

- A granularidade do dataset é de 1 linha por ticket resolvido.


## 3. Colunas do Dataset Processado

| Coluna | Tipo | Origem (raw) | Descrição | Justificativa |
|------|------|-------------|-----------|---------------|
| ticket_id | string | ID do ticket | Identificador único do ticket | Chave primária |
| created_at | datetime | Data criação | Momento de abertura do ticket | Cálculo de SLA |
| resolved_at | datetime | Data resolução | Momento de resolução | Tempo de resolução |
| resolution_time | float | resolved_at - created_at | Diferença entre resolved_at e created_at (dias/horas, minutos e segundos) | Métrica central |
| resolved_by | string | Quem resolveu | Analista responsável | Performance |
| origin | string | Origem do ticket | Canal de entrada | Volume por canal |
| ticket_title | string | Título / categoria | Tipo de demanda | Análise de demanda |
| operational_error_flag | boolean | Sinalização Operacional | Indica erro operacional | Qualidade |
| operational_error_type | string | Sinalização Operacional | Tipo do erro | Análise de causa |

## 4. Colunas Explicitamente Excluídas
Fin AI Agent rating,Fin AI Agent rating remark, hackxxxx_llm_response, E como você avalia o seu atendimento?,hackxxxx_contact. Essas colunas não tem células preenchidas e não agregam valor analítico. Uma delas possui referência sensível / irrelevante para análise.

## 5. Decisões e Trade-offs
- Todas as colunas de sinalização operacional são importantes e devem ser cuidadosamente analisadas. 
- Esses arquivos, embora não reflitam como uma empresa de verdade analisa dados no intercom, servem como caso de estudo. A intercom fornece API para as empresas que pagam a assinatura de seus serviços e ela oferece dados históricos em tempo real, sem necessidade de download ou separação de arquivos csv por mês.
- perda de tempo baixando arquivo csv.
- evoluir para uso da API da intercom como fonte de dados.
- possibilidade de analisar um ambiente real.
