import pandas as pd
import os
import sys

# Define o caminho base do projeto para encontrar as pastas de dados
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_PATH = os.path.join(BASE_DIR, 'data_raw')
TREATED_PATH = os.path.join(BASE_DIR, 'data_treated')
OUTPUT_FILE = os.path.join(TREATED_PATH, 'dados_tratados.csv')

# ==============================================================================
# TRECHO DO MEMBRO 3: LEITURA, LIMPEZA E PREPARAÇÃO DE DADOS (T)
# ==============================================================================

print("Membro 3: Iniciando leitura, limpeza e preparação de dados...")
try:
    df_reais = pd.read_csv(os.path.join(RAW_PATH, 'dados_reais_simulados.csv'))
    df_viagens = pd.read_csv(os.path.join(RAW_PATH, 'gtfs_viagens_simuladas.csv'))
except FileNotFoundError as e:
    print(f"ERRO CRÍTICO: Arquivo de dados não encontrado. Verifique se os arquivos existem em {RAW_PATH}/. Detalhe: {e}", file=sys.stderr)
    sys.exit(1)
    
# 1. Limpeza Básica: Remoção de Duplicatas e Nulos
df_reais_limpo = df_reais.drop_duplicates()
df_reais_limpo = df_reais_limpo.dropna(subset=['horario_real', 'lotacao', 'trip_id'])

# 2. Conversão de Tempo para Datetime (CRÍTICO para o cálculo)
# Converte a coluna de hora (string) para um objeto datetime, necessário para fazer a subtração
df_reais_limpo['horario_real_dt'] = pd.to_datetime(df_reais_limpo['horario_real'], format='%H:%M:%S', errors='coerce').dt.time

print(f"Membro 3: Limpeza concluída. Total de registros para trabalho: {len(df_reais_limpo)}")
# df_trabalho é a base de dados limpa que será usada pelo Membro 4
df_trabalho = df_reais_limpo 

# ==============================================================================
# TRECHO DO MEMBRO 4: CRUZAMENTO DE DADOS E CÁLCULO DE MÉTRICAS (T)
# ==============================================================================
print("Membro 4: Iniciando cruzamento de dados e cálculo de métricas...")
# 1. Preparação da Tabela de Viagens (Horário Previsto)
df_viagens['arrival_time_dt'] = pd.to_datetime(df_viagens['arrival_time'], format='%H:%M:%S', errors='coerce').dt.time
# 2. Cruzamento (Merge): Junta a tabela REAL com a tabela PREVISTA (schedule)
df_analise = pd.merge(
    df_trabalho, 
    df_viagens[['trip_id', 'arrival_time_dt']], 
    on='trip_id', 
    how='left'
)
# 3. Função Auxiliar para Calcular Tempo Total em Segundos (Necessário para subtração)
def time_to_seconds(t):
    if pd.isna(t):
        return 0
    return t.hour * 3600 + t.minute * 60 + t.second

# Conversão para segundos e cálculo da métrica
df_analise['real_segundos'] = df_analise['horario_real_dt'].apply(time_to_seconds)
df_analise['previsto_segundos'] = df_analise['arrival_time_dt'].apply(time_to_seconds)

# FÓRMULA DO ÍNDICE DE PONTUALIDADE (atraso em minutos)
# Atraso = (Tempo Real - Tempo Previsto) / 60
df_analise['atraso_segundos'] = df_analise['real_segundos'] - df_analise['previsto_segundos']
df_analise['atraso_minutos'] = df_analise['atraso_segundos'] / 60 

# 4. Enriquecimento: Criação da Dimensão "Período do Dia"
# Usaremos 'lotacao' > 40 como um índice de lotação alta
df_analise['indice_lotacao'] = df_analise['lotacao'].apply(lambda x: 'Alta' if x >= 40 else 'Baixa')

# df_final é a base de dados pronta para análise

df_final = df_analise.dropna(subset=['atraso_minutos']) 

print("Membro 4: Cálculo de Pontualidade e enriquecimento concluídos.")


#Gerando data_treated/dados_tratados.csv
# Arredondando colunas numéricas
df_final['atraso_minutos'] = df_final['atraso_minutos'].round(2)
df_final['real_segundos'] = df_final['real_segundos'].round(0)
df_final['previsto_segundos'] = df_final['previsto_segundos'].round(0)
df_final['atraso_segundos'] = df_final['atraso_segundos'].round(0)

#Reorganização para facilitar a leitura 
df_final = df_final[[
    'trip_id', 'stop_id', 'horario_real', 'horario_real_dt',
    'arrival_time_dt', 'lotacao', 'indice_lotacao',
    'real_segundos', 'previsto_segundos', 'atraso_segundos', 'atraso_minutos'
]]

df_final['indice_lotacao'] = df_final['indice_lotacao'].str.strip()

#Transformando a coluna indice_lotação em um tipo categórico ordenado
df_final['indice_lotacao'] = pd.Categorical(df_final['indice_lotacao'], categories=['Baixa','Média','Alta'], ordered=True)

pasta = './data_treated'
os.makedirs(pasta,exist_ok=True)

df_final.to_csv(f'{pasta}/dados_tratados.csv', sep=';', index=False, encoding='utf-8-sig', float_format='%.2f')

print("Membro 5: Geração dos dados_tratados.csv concluida")

