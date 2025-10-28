import pandas as pd
from pathlib import Path

# Caminhos das pastas (como o script está na raiz)
pasta_raw = Path("data_raw")
pasta_clean = Path("data_clean")

# Cria a pasta de saída (caso não exista)
pasta_clean.mkdir(parents=True, exist_ok=True)

# Caminhos dos arquivos de entrada (espera que já existam dentro de data_raw)
arquivo_reais = pasta_raw / "dados_reais_simulados.csv"
arquivo_gtfs = pasta_raw / "gtfs_viagens_simuladas.csv"

# Verificação — garante que os arquivos existem antes de prosseguir
if not arquivo_reais.exists() or not arquivo_gtfs.exists():
    raise FileNotFoundError(
        f"⚠️ Um dos arquivos de entrada não foi encontrado em: {pasta_raw.resolve()}\n"
        f"Esperados:\n - {arquivo_reais.name}\n - {arquivo_gtfs.name}"
    )

# Leitura dos arquivos
reais = pd.read_csv(arquivo_reais)
gtfs = pd.read_csv(arquivo_gtfs)

# Limpeza — remoção de valores nulos e duplicados
reais_limpo = reais.dropna().drop_duplicates()
gtfs_limpo = gtfs.dropna().drop_duplicates()

# Exporta os dados limpos para a pasta data_clean
reais_limpo.to_csv(pasta_clean / "dados_reais_limpos.csv", index=False, encoding="utf-8-sig")
gtfs_limpo.to_csv(pasta_clean / "gtfs_viagens_limpos.csv", index=False, encoding="utf-8-sig")

print("✅ Limpeza concluída com sucesso!")
print(f"Arquivos limpos salvos em: {pasta_clean.resolve()}")
