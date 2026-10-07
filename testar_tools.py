from tools import analisar_risco, consultar_protocolos


dados = {
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
}


# Analisa o risco
resultado = analisar_risco(dados)

print("\n--- ANÁLISE DE RISCO ---")
print(f"Probabilidade: {resultado['probabilidade']:.2%}")
print(f"Classificação: {resultado['classificacao']}")


# Consulta os protocolos
risco_alto = resultado["previsao"] == 1

protocolos = consultar_protocolos(
    dados,
    risco_alto=risco_alto
)

print("\n--- PROTOCOLOS SUGERIDOS ---")

for protocolo in protocolos:
    print(f"- {protocolo}")