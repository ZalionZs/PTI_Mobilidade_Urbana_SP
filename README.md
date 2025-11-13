PoC — Mobilidade Urbana (SP)




Descrição Projeto de prova de conceito para análise de pontualidade do transporte público em São Paulo usando o padrão GTFS. Os dados usados neste repositório são simulados para demonstração.

Status

Dados: simulados

Output principal: data_treated/dados_tratados.csv

Visualização: Power BI (.pbix)

Fontes de Dados (Extração) A fonte primária é o padrão GTFS (General Transit Feed Specification). Exemplo de origem pública:

https://prefeitura.sp.gov.br/web/mobilidade/w/institucional/sptrans/acesso_a_informacao/152415

Tecnologias | Etapa | Tecnologia | Função Detalhada | | :------------------------------- | :------------------------- | :------------------------------------------------------------------------------------------ | | ETL (Extração/Transformação) | Python (pandas) | Limpeza, cruzamento e cálculo da métrica de pontualidade. | | Carga (L) — DDL/DML | CSV no repositório | data_treated/dados_tratados.csv como DWH simplificado. | | OLAP / Visualização | Power BI Desktop | Análises multidimensionais e dashboards. |

Papéis e Responsabilidades (6 membros) | Membro | Etapa Principal | Contribuição | | :-------------------------- | :--------------------------------- | :---------------------------------------------------------- | | Membro 1 (Gerente) | Gestão e Estrutura | Criação do repositório e coordenação. | | Membro 2 (Extração) | Documentação / Fonte | Identificação das fontes e preparo dos dados brutos. | | Membro 3 (T - Limpeza) | Transformação — Limpeza | Remoção de nulos/duplicatas e validação. | | Membro 4 (T - Métricas) | Transformação — Enriquecimento | Cálculo do Índice de Pontualidade. | | Membro 5 (Carga) | Carga (L) | Geração do dados_tratados.csv. | | Membro 6 (Visualização) | OLAP / Dashboards / Vídeo | Desenvolvimento do painel Power BI e vídeo demonstrativo. |

Pré-requisitos

Windows 10/11

Python 3.9+ (recomenda-se 3.11)

Power BI Desktop (para visualização)

Como executar (exemplo PowerShell)

Criar e ativar ambiente:

python -m venv .venv

.venv\Scripts\Activate.ps1

Instalar dependências:

pip install -r requirements.txt

Executar ETL (ajuste o caminho se necessário):

python scripts/etl_scripts.py

Resultado:

data_treated/dados_tratados.csv

Estrutura sugerida do repositório

/scripts — scripts Python (ex.: scripts/etl_scripts.py)

/data_raw — dados GTFS simulados

/data_treated — dados_tratados.csv (resultado)

/reports — Power BI (.pbix) / relatórios

README.md

requirements.txt

Observações importantes

Os dados aqui são simulados; validar e ajustar scripts antes de apontar feeds GTFS reais.

Documentar versão do Python e dependências no requirements.txt.

Contribuição e Issues

Abra issues para problemas/funcionalidades.

Crie PRs contra a branch main; siga um CONTRIBUTING.md (se disponível).

Licença

MIT (adicione um arquivo LICENSE com o texto da licença).

10. Operações OLAP e Dashboards (Responsável: Natalia)

As análises OLAP foram realizadas no Power BI a partir do arquivo data_treated/dados_tratados.csv, resultante do processo de ETL.

Objetivo

Fornecer uma visão multidimensional sobre a pontualidade e a lotação das viagens simuladas, apoiando decisões relacionadas à qualidade do transporte público.

Operações OLAP Implementadas
Tipo de Operação	Descrição	Evidência
ROLL-UP	Cálculo do atraso médio por período do dia (manhã, tarde, noite).	Dashboard 1
SLICE	Filtragem de viagens com lotação alta (índice "Alta").	Dashboard 2
DRILL-DOWN	Detalhamento da análise por trip_id.	Dashboard 3
DICE	Viagens com atraso > 5 minutos e lotação alta.	Dashboard 4
Dashboards Criados no Power BI

Atraso médio por período do dia — gráfico de colunas (ROLL-UP).

Correlação entre lotação e atraso — gráfico de dispersão (SLICE + análise correlacional).

Detalhamento de viagens por trip_id — tabela com drill-down (DRILL-DOWN).

Filtro combinado: atraso > 5 min + lotação alta — análise segmentada (DICE).

As imagens desses dashboards estão disponíveis na pasta /reports/imagens.

Principais Insights

Viagens classificadas como Alta lotação apresentaram maior atraso médio.

O período da manhã concentrou a maior quantidade de atrasos positivos.

Aproximadamente 65% das viagens chegaram pontualmente ou adiantadas.

Viagens com atraso elevado (> 5 min) geralmente apresentam lotações maiores.

Vídeo Demonstrativo (1 minuto)

O vídeo exibindo os dashboards e as operações OLAP está disponível em:

/reports/video_demonstrativo.mp4

Inclui:

Breve visão geral do dataset carregado;

Demonstração de cada gráfico OLAP implementado;

Conclusões extraídas das análises.  
