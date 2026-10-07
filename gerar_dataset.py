import numpy as np
import pandas as pd

# Mantém a geração dos dados reproduzível
np.random.seed(42)

# Quantidade de registros
n = 5000

# Geração da base sintética fornecida pela FIAP
df = pd.DataFrame({
    "idade_media": np.random.normal(55, 12, n).clip(18, 90),
    "carga_sistema": np.random.uniform(30, 100, n),
    "tempo_espera": np.random.normal(45, 20, n).clip(5, 180),
    "fc_media": np.random.normal(85, 15, n).clip(50, 150),
    "spo2_media": np.random.normal(95, 3, n).clip(70, 100),
    "pa_sistolica": np.random.normal(125, 20, n).clip(80, 200),
    "temperatura": np.random.normal(24, 5, n).clip(10, 40),
    "densidade_eventos": np.random.poisson(3, n),
    "eventos_24h": np.random.poisson(2, n),
    "disponibilidade_recursos": np.random.uniform(20, 100, n)
})

# Construção do score de risco
risk_score = (
    (df["carga_sistema"] > 80).astype(int)
    + (df["tempo_espera"] > 60).astype(int)
    + (df["spo2_media"] < 92).astype(int)
    + (df["fc_media"] > 110).astype(int)
    + (df["eventos_24h"] > 4).astype(int)
    + (df["disponibilidade_recursos"] < 40).astype(int)
)

# Variável-alvo
df["pico_risco"] = (risk_score >= 2).astype(int)

# Salva a base gerada
df.to_csv("data/dataset_cardioia.csv", index=False)

print("Dataset criado com sucesso!")
print(f"Quantidade de registros: {len(df)}")
print("\nDistribuição da variável pico_risco:")
print(df["pico_risco"].value_counts())
print("\nPrimeiros registros:")
print(df.head())