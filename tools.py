import joblib
import pandas as pd

from protocolos import protocolos


# Carrega o modelo treinado
modelo = joblib.load("models/modelo_risco.pkl")


def analisar_risco(dados):
    """
    Recebe os dados de um novo caso e retorna
    a previsão e a probabilidade de pico de risco.
    """

    novo_caso = pd.DataFrame([dados])

    previsao = int(modelo.predict(novo_caso)[0])
    probabilidade = float(modelo.predict_proba(novo_caso)[0][1])

    classificacao = "ALTO RISCO" if previsao == 1 else "BAIXO RISCO"

    return {
        "probabilidade": probabilidade,
        "previsao": previsao,
        "classificacao": classificacao
    }


def consultar_protocolos(dados, risco_alto=False):
    """
    Consulta a base de protocolos e retorna
    somente os protocolos aplicáveis ao caso.
    """

    protocolos_sugeridos = []

    if dados["spo2_media"] < 88:
        protocolos_sugeridos.append(protocolos[0]["protocolo"])

    if dados["carga_sistema"] > 85:
        protocolos_sugeridos.append(protocolos[1]["protocolo"])

    if dados["fc_media"] > 120:
        protocolos_sugeridos.append(protocolos[2]["protocolo"])

    if dados["eventos_24h"] > 5:
        protocolos_sugeridos.append(protocolos[3]["protocolo"])

    if dados["disponibilidade_recursos"] < 30:
        protocolos_sugeridos.append(protocolos[4]["protocolo"])

    if dados["tempo_espera"] > 90:
        protocolos_sugeridos.append(protocolos[5]["protocolo"])

    if dados["temperatura"] > 38:
        protocolos_sugeridos.append(protocolos[6]["protocolo"])

    if dados["densidade_eventos"] > 6:
        protocolos_sugeridos.append(protocolos[7]["protocolo"])

    if dados["pa_sistolica"] < 90:
        protocolos_sugeridos.append(protocolos[8]["protocolo"])

    if risco_alto:
        protocolos_sugeridos.append(protocolos[9]["protocolo"])

    return protocolos_sugeridos