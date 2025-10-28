import pandas as pd
import os

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
    print(f"ERRO CRÍTICO: Arquivo de dados não encontrado. Verifique se estão na pasta data_raw/. Detalhe: {e}")
    exit()
    
# 1. Limpeza Básica: Remoção de Duplicatas e Nulos
df_reais_limpo = df_reais.drop_duplicates()
df_reais_limpo = df_reais_limpo.dropna(subset=['horario_real', 'lotacao', 'trip_id'])

# 2. Conversão de Tempo para Datetime (CRÍTICO para o cálculo)
# Converte a coluna de hora (string) para um objeto datetime, necessário para fazer a subtração
df_reais_limpo['horario_real_dt'] = pd.to_datetime(df_reais_limpo['horario_real'], format='%H:%M:%S', errors='coerce').dt.time

print(f"Membro 3: Limpeza concluída. Total de registros para trabalho: {len(df_reais_limpo)}")
# df_trabalho é a base de dados limpa que será usada pelo Membro 4
df_trabalho = df_reais_limpo 

# Commit do Membro 3: Salva o arquivo e envia