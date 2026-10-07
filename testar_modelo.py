import joblib
import pandas as pd


# 1. Carregar o modelo treinado
modelo = joblib.load("models/modelo_risco.pkl")


# 2. Dados do novo caso fornecido pela FIAP
novo_caso = pd.DataFrame([{
    "idade_media": 62,
    "carga_sistema": 92,
    "tempo_espera": 75,
    "fc_media": 118,
    "spo2_media": 89,
    "pa_sistolica": 100,
    "temperatura": 37.5,
    "densidade_eventos": 7,
    "eventos_24h": 5,
    "disponibilidade_recursos": 25
}])


# 3. Realizar a previsão
previsao = modelo.predict(novo_caso)[0]

# Probabilidade da classe 1 = pico de risco
probabilidade = modelo.predict_proba(novo_caso)[0][1]


# 4. Classificação textual
if previsao == 1:
    classificacao = "ALTO RISCO"
else:
    classificacao = "BAIXO RISCO"


# 5. Exibir resultado
print("\n--- CARDIOIA | ANÁLISE PREDITIVA ---")
print(f"Probabilidade de pico de risco: {probabilidade:.2%}")
print(f"Classe prevista: {previsao}")
print(f"Classificação: {classificacao}")