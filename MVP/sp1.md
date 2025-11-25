# 📌 Sprint 1 - [Acompanhamento dos Resultados de Exportação e Importação com Foco no Comparativo entre Estados da Federação e de Municípios no Estado de SP ]

## 🎯 Objetivo do MVP  
Desenvolver uma plataforma de Business Intelligence que permita acompanhar os resultados de exportação e importação do Brasil, com foco nos municípios do Estado de São Paulo.
- Qual problema resolve? Falta de acesso intuitivo a dados confiáveis e comparativos de comércio exterior em nível municipal e estadual.  
- Qual hipótese será validada? Uma ferramenta de BI, baseada em dados abertos do MDIC/ComexStat, pode apoiar gestores públicos, empresas e pesquisadores na identificação de tendências, riscos e oportunidades no comércio internacional.  
- Qual valor será entregue ao usuário final? Tomada de decisão embasada em dados claros, segmentados e acessíveis, reduzindo incertezas e aumentando a competitividade regional.

---

## 📝 Descrição da Solução
O MVP consiste em uma plataforma de BI (dashboard interativo no Power BI) integrada a uma base de dados limpa e segmentada por município paulista.  
- Funcionalidades principais incluídas
Segmentação por estado e município.
Ranking de exportação/importação por valor agregado.
Evolução histórica da balança comercial (2023–2025).
Filtros de busca por produto (código SH4).  
- Limitações conhecidas
Visualizações limitadas ao período inicial (2023–2025).
Algumas funcionalidades (sazonalidade, transporte) ainda não implementadas (previstas para os próximos sprints)
- Escopo reduzido   
Validação do painel inicial com segmentação por municípios paulistas e identificação de mercados emergentes.

---

## 👥 Personas / Usuários-Alvo
- **Persona 1:** Gestor Público de Comércio Exterior, precisa monitorar desempenho dos municípios paulistas; dificuldade em acessar dados comparativos regionais e identificar tendências de mercado. 
- **Persona 2:** Analista/Empresa Exportadora, busca entender riscos, tarifas e oportunidades internacionais; falta de clareza sobre impactos tarifários e dificuldade em planejar rotas logísticas eficientes 

---

## 🔑 User Stories (Backlog do MVP)
| ID  | User Story                                                                 | Prioridade | Estimativa |
|-----|-----------------------------------------------------------------------------|------------|------------|
| US1 | Como tomador de decisões públicas, quero que os dados coletados passem por uma limpeza inicial em linguagens de programação, para ter consistência no dashboard..         | Alta       | 8 pontos   |
| US2 | Como tomador de decisões públicas,  preciso comparar o desempenho comercial de municípios paulistas com seus vizinhos, para identificar pontos fortes e fracos regionais.         | Alta      | 5 pontos   |
| US3 | Como tomador de decisões públicas, quero identificar mercados emergentes internacionais, para orientar políticas de incentivo às exportações.         | Alta      | 3 pontos   |
| US4 | Como tomador de decisões públicas, quero segmentar por Estado e Município Paulista para acessar informações detalhadas (principais cargas, ranking de exportação/importação, evolução histórica).         | Alta      | 3 pontos   |
| US5 | Como tomador de decisões públicas, quero avaliar o impacto de políticas tarifárias, para entender riscos e oportunidades das mudanças regulatórias.         | Média      | 5 pontos   |
| US6 | Como tomador de decisões públicas, quero que todos os dados sejam entregues em inglês, para que possam ser utilizados em relatórios internacionais.         | Baixa      | 3 pontos   |

---

## 📅 Sprint(s) Relacionadas
| Sprint | Entregas Principais                          | Status   |
|--------|----------------------------------------------|----------|
| 01     | Base de dados limpa e segmentada (Python), ranking de comércio por município, identificação de mercados emergentes, diagnóstico estratégico (riscos e oportunidades tarifárias) e protótipos/dashboards iniciais no Power BI                       | Concluído|
| 02     | Dashboard completo no Power BI (comparativos, filtros por SH4 e evolução histórica)                         | Planejado |
| 03     | Painel Interativo Final (2023-2025), Análise de Competitividade, Mapeamento de Clientes e Projeções Macroeconômicas                           | Planejado |

---

## 📊 Critérios de Aceitação
- O MVP deve permitir que o usuário ,visualize e compare municípios paulistas em termos de comércio exterior.  
- O sistema deve registrar ,base de dados segmentada por município.
- Métricas coletadas:
Número de acessos ao painel.
Tempo médio de carregamento.
Uso de filtros de análise.  

---

## 📈 Métricas de Validação
- Número de usuários que acessaram/testaram o dashboard.
- Feedback qualitativo de gestores e empresas (clareza das informações, usabilidade).
- Indicadores de negócio:
% de adesão ao uso do painel em sala de aula.
Identificação de novos mercados emergentes nos dados.  

---

## 🚀 Próximos Passos
- Melhorias planejadas após feedback  
- Ajustes de usabilidade  
- Expansão de funcionalidades para próximo incremento  

---

## 📂 Anexos / Evidências
- Requisitos do Cliente 
- Slides da API 
- Relatório Sprint 1
- Análise de Políticas Tarifárias
- Prints/Protótipos do Dashboard (Power BI).
- Repositório GitHub: API-Grupo-3
- Dashboard PowerBI em Execução: <td align="center"><video src="https://github.com/user-attachments/assets/1dfb792c-5485-4664-9cd6-955530c92b22"></video></td>
- Código Python em Execução: <td align="center"><video src="https://github.com/user-attachments/assets/d23b8c75-78b7-4331-aaff-458a78307b17"></video></td>

