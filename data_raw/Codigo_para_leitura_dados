import pandas as pd
from pathlib import Path

arquivo_programado = Path("horarios_programados.csv")
arquivo_real = Path("horarios_reais.csv")

# Leitura dos arquivos
programado = pd.read_csv(arquivo_programado, dtype={"trip_id": str, "arrival_time": str})
real = pd.read_csv(arquivo_real, dtype={"trip_id": str, "stop_id": str, "horario_real": str, "lotacao": int})

# Limpeza inicial
programado = programado.dropna().drop_duplicates()
real = real.dropna().drop_duplicates()

# Conversão de horários
programado["arrival_time"] = pd.to_datetime(programado["arrival_time"], format="%H:%M:%S")
real["horario_real"] = pd.to_datetime(real["horario_real"], format="%H:%M:%S")

# União dos dados pelo trip_id
dados_unidos = pd.merge(real, programado, on="trip_id", how="left")

# Cálculo do atraso em minutos
dados_unidos["atraso_minutos"] = (dados_unidos["horario_real"] - dados_unidos["arrival_time"]).dt.total_seconds() / 60

# Métricas por viagem
metricas_viagem = dados_unidos.groupby("trip_id").agg(
    media_atraso_minutos=("atraso_minutos", "mean"),
    media_lotacao=("lotacao", "mean")
).reset_index()

# Exporta CSVs
dados_unidos.to_csv("dados_unidos.csv", index=False, encoding="utf-8-sig")
metricas_viagem.to_csv("metricas_viagem.csv", index=False, encoding="utf-8-sig")

print("✅ Dados unidos e métricas calculadas com sucesso!")
print("Arquivo detalhado: dados_unidos.csv")
print("Arquivo de métricas: metricas_viagem.csv")
print(metricas_viagem)
