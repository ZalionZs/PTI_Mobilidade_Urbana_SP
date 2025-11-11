# PoC — Mobilidade Urbana (SP)

[![Status](https://img.shields.io/badge/status-draft-orange)]()
[![License](https://img.shields.io/badge/license-MIT-blue)]()

Descrição
Projeto de prova de conceito para análise de pontualidade do transporte público em São Paulo usando o padrão GTFS. Os dados usados neste repositório são simulados para demonstração.

Status

- Dados: simulados
- Output principal: data_treated/dados_tratados.csv
- Visualização: Power BI (.pbix)

1. Fontes de Dados (Extração)
   A fonte primária é o padrão GTFS (General Transit Feed Specification). Exemplo de origem pública:

- https://prefeitura.sp.gov.br/web/mobilidade/w/institucional/sptrans/acesso_a_informacao/152415

2. Tecnologias
   | Etapa | Tecnologia | Função Detalhada |
   | :------------------------------- | :------------------------- | :------------------------------------------------------------------------------------------ |
   | ETL (Extração/Transformação) | Python (pandas) | Limpeza, cruzamento e cálculo da métrica de pontualidade. |
   | Carga (L) — DDL/DML | CSV no repositório | `data_treated/dados_tratados.csv` como DWH simplificado. |
   | OLAP / Visualização | Power BI Desktop | Análises multidimensionais e dashboards. |

3. Papéis e Responsabilidades (6 membros)
   | Membro | Etapa Principal | Contribuição |
   | :-------------------------- | :--------------------------------- | :---------------------------------------------------------- |
   | Membro 1 (Gerente) | Gestão e Estrutura | Criação do repositório e coordenação. |
   | Membro 2 (Extração) | Documentação / Fonte | Identificação das fontes e preparo dos dados brutos. |
   | Membro 3 (T - Limpeza) | Transformação — Limpeza | Remoção de nulos/duplicatas e validação. |
   | Membro 4 (T - Métricas) | Transformação — Enriquecimento | Cálculo do Índice de Pontualidade. |
   | Membro 5 (Carga) | Carga (L) | Geração do `dados_tratados.csv`. |
   | Membro 6 (Visualização) | OLAP / Dashboards / Vídeo | Desenvolvimento do painel Power BI e vídeo demonstrativo. |

4. Pré-requisitos

- Windows 10/11
- Python 3.9+ (recomenda-se 3.11)
- Power BI Desktop (para visualização)

5. Como executar (exemplo PowerShell)
1. Criar e ativar ambiente:
   - python -m venv .venv
   - .venv\Scripts\Activate.ps1
1. Instalar dependências:
   - pip install -r requirements.txt
1. Executar ETL (ajuste o caminho se necessário):
   - python scripts/etl_scripts.py
1. Resultado:

   - data_treated/dados_tratados.csv

1. Estrutura sugerida do repositório

- /scripts — scripts Python (ex.: `scripts/etl_scripts.py`)
- /data_raw — dados GTFS simulados
- /data_treated — dados_tratados.csv (resultado)
- /reports — Power BI (.pbix) / relatórios
- README.md
- requirements.txt

7. Observações importantes

- Os dados aqui são simulados; validar e ajustar scripts antes de apontar feeds GTFS reais.
- Documentar versão do Python e dependências no requirements.txt.

8. Contribuição e Issues

- Abra issues para problemas/funcionalidades.
- Crie PRs contra a branch main; siga um CONTRIBUTING.md (se disponível).

9. Licença

- MIT (adicione um arquivo LICENSE com o texto da licença)
