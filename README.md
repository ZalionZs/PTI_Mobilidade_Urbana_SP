### 1. Fontes de Dados (Extração)

A fonte primária utilizada para este PoC é o padrão **GTFS** (_General Transit Feed Specification_), que fornece dados de rotas e horários. Para fins de demonstração, os dados foram simulados.

- **Link de Origem (Exemplo):** https://prefeitura.sp.gov.br/web/mobilidade/w/institucional/sptrans/acesso_a_informacao/152415https://prefeitura.sp.gov.br/web/mobilidade/w/institucional/sptrans/acesso_a_informacao/152415

### 2. Definição das Tecnologias

| Etapa                            | Tecnologia                 | Função Detalhada                                                                            |
| :------------------------------- | :------------------------- | :------------------------------------------------------------------------------------------ |
| **ETL (Extração/Transformação)** | **Python com Pandas**      | Utilizado para limpeza, cruzamento de dados e cálculo da métrica de pontualidade.           |
| **Carga (L) (DDL/DML)**          | **Arquivos CSV no GitHub** | O `dados_tratados.csv` serve como Data Warehouse simplificado (DDL: estrutura, DML: dados). |
| **OLAP / Visualização**          | **Power BI Desktop**       | Ferramenta visual para análises multidimensionais (**OLAP**) e criação de _dashboards_.     |

### 3. Detalhamento Técnico (Divisão de 6 Membros)

| Membro                      | Etapa Principal                    | Contribuição e Lógica                                                           |
| :-------------------------- | :--------------------------------- | :------------------------------------------------------------------------------ |
| **Membro 1** (Gerente)      | Gestão e Estrutura                 | Criação do repositório e inclusão dos dados simulados.                          |
| **Membro 2** (Extração)     | Documentação e Fonte               | Finaliza o `README.md` e aponta a origem da extração.                           |
| **Membro 3** (T - Limpeza)  | Transformação (T) - Limpeza        | Código Python para ler dados e garantir a qualidade (remover nulos/duplicatas). |
| **Membro 4** (T - Métricas) | Transformação (T) - Enriquecimento | Código Python para cruzar dados e calcular o **Índice de Pontualidade**.        |
| **Membro 5** (Carga)        | Carga (L)                          | Executa o script final, gera o `dados_tratados.csv` (evidência da Carga).       |
| **Membro 6** (Visualização) | OLAP, Dashboards e Vídeo           | Cria o painel analítico no Power BI e grava o vídeo demonstrativo.              |
