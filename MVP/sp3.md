# 📌 MVP - [PLATAFORMA DE INTELIGÊNCIA COMERCIAL ESTRATÉGICA]

## 🎯 Objetivo do MVP
Mitigação de Risco Estrutural e Projeção de Cenários
- Qual problema resolve?
  - A vulnerabilidade estrutural da economia brasileira no comércio exterior, decorrente da alta concentração em poucas commodities e mercados-chave (como a China), que gera instabilidade na receita frente a choques de preço ou políticos.
- Qual hipótese será validada?
  - Hipótese: A entrega do painel interativo consolidado (2023–2025) e as análises estratégicas (competitividade, agentes e projeções) fornecerão a base para decisões que promovam ativamente a diversificação de mercados e a agregação de valor aos produtos de exportação.
- Qual valor será entregue ao usuário final?
  - Inteligência Estratégica e Visão de Futuro: Fornecer uma ferramenta de BI completa que não apenas visualiza o histórico de 2023–2025, mas também diagnostica riscos de concentração, avalia a competitividade e inclui projeções macroeconômicas para guiar o planejamento de longo prazo.

---

## 📝 Descrição da Solução
Consolidação dos Dashboards e Geração de Relatórios Preditivos
- Funcionalidades principais incluídas
  - Módulo de Competitividade: Avaliação de preço e qualidade dos produtos exportados em relação a concorrentes.
  - Análise de Vulnerabilidade e Risco: Funcionalidade que identifica a dependência de mercados e produtos e propõe estratégias de mitigação (diversificação, agregação de valor).
  - Mapeamento de Agentes Chave: Identificação dos principais clientes/compradores internacionais e suas sedes.
  - Projeção de Cenários: Inclusão de dados de projeções macroeconômicas (PIB IPEA 2025/2026) para apoiar decisões futuras.
- Limitações conhecidas
  - As projeções futuras são baseadas em fontes externas consolidadas (IPEA, ComexStat), e não em um modelo preditivo matemático desenvolvido internamente.
- Escopo reduzido (somente o essencial para validar a ideia)
  - O escopo desta Sprint 3 é a finalização do sistema de BI e a entrega de todas as análises estratégicas propostas, transformando dados em insights de alto valor.

---

## 👥 Personas / Usuários-Alvo
- **Persona 1:** Gestor Público de Comércio Exterior, precisa monitorar desempenho dos municípios paulistas; dificuldade em acessar dados comparativos regionais e identificar tendências de mercado. 
- **Persona 2:** Analista/Empresa Exportadora, busca entender riscos, tarifas e oportunidades internacionais; falta de clareza sobre impactos tarifários e dificuldade em planejar rotas logísticas eficientes.

---

## 🔑 User Stories (Backlog do MVP - Sprint 3)
| ID | User Story | Prioridade | Estimativa |
|:---|:---|:---|:---|
| US16 | Como tomador de decisões públicas, preciso identificar dependência de mercados específicos, para propor alternativas e mitigar vulnerabilidades. | Alta | 6 horas |
| US17 | Como tomador de decisões públicas, quero projetar o desempenho comercial futuro dos municípios, para apoiar decisões de longo prazo. | Alta | 6 horas |
| US18 | Como tomador de decisões públicas, quero mapear os principais clientes internacionais das empresas locais, para entender como essas relações impactam a economia. | Média | 6 horas |
| US19 | Como tomador de decisões públicas, necessito que todos os dados sejam entregues em inglês, para que possam ser utilizados em relatórios internacionais. | Baixa | 6 horas |

---

## 📅 Sprint(s) Relacionadas
| Sprint | Entregas Principais                          | Status   |
|--------|----------------------------------------------|----------|
| 01     | Base de dados limpa e segmentada (Python), ranking de comércio por município, identificação de mercados emergentes, diagnóstico estratégico (riscos e oportunidades tarifárias) e protótipos/dashboards iniciais no Power BI                       | Concluído|
| 02     | Dashboard completo no Power BI (comparativos, filtros por SH4 e evolução histórica)                           | Concluído |
| 03     | Painel Interativo Final (2023-2025), Análise de Competitividade, Mapeamento de Clientes e Projeções Macroeconômicas | Concluído |

---

## 📊 Critérios de Aceitação
- O MVP deve exibir o painel interativo da balança comercial (2023–2025).
- O módulo de risco deve identificar a dependência da China para as principais commodities e listar as propostas de mitigação (diversificação/agregação de valor).
- O relatório de projeção deve incluir os dados do IPEA (PIB 2025: 2,2% e 2026: 1,6%) e a análise do impacto dessas previsões no cenário comercial.
- O sistema deve mapear corretamente os principais agentes exportadores e seus mercados.

---

## 📈 Métricas de Validação
- Número de usuários que acessaram/testaram o dashboard..
- Feedback qualitativo de gestores e empresas (clareza das informações, usabilidade).
- Comparação dos resultados entre municípios e estados para checar coerência dos indicadores.
- Avaliação do desempenho do painel completo com base real de 2023 a 2025.

---

## 📂 Anexos / Evidências
- Requisitos do Cliente.
- Slides da API.
- Relatório Sprint 3.
- Análise de Dependência de Mercado.
- Relatório de Previsões Macroeconômicas.
- Painel Gráfico Interativo (Balança Comercial 2023–2025) em Execução:<td align="center"><video src="https://github.com/user-attachments/assets/23b673ea-e7a6-42bf-83e0-faa7c945bb69"></video></td>
