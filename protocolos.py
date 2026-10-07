# Base de conhecimento simulada de protocolos do CardioIA

protocolos = [
    {
        "id": 1,
        "condicao": "spo2_media < 88",
        "protocolo": "Se SPO2 < 88% → iniciar suporte respiratório imediato"
    },
    {
        "id": 2,
        "condicao": "carga_sistema > 85",
        "protocolo": "Se carga do sistema > 85% → abrir unidades temporárias"
    },
    {
        "id": 3,
        "condicao": "fc_media > 120",
        "protocolo": "Se FC > 120 → iniciar monitoramento intensivo"
    },
    {
        "id": 4,
        "condicao": "eventos_24h > 5",
        "protocolo": "Se eventos_24h > 5 → ativar equipe de resposta rápida"
    },
    {
        "id": 5,
        "condicao": "disponibilidade_recursos < 30",
        "protocolo": "Se disponibilidade_recursos < 30% → redistribuir insumos"
    },
    {
        "id": 6,
        "condicao": "tempo_espera > 90",
        "protocolo": "Se tempo_espera > 90 min → priorizar triagem emergencial"
    },
    {
        "id": 7,
        "condicao": "temperatura > 38",
        "protocolo": "Se temperatura > 38°C média → iniciar protocolo infeccioso"
    },
    {
        "id": 8,
        "condicao": "densidade_eventos > 6",
        "protocolo": "Se densidade_eventos > 6 → ativar plano de contingência"
    },
    {
        "id": 9,
        "condicao": "pa_sistolica < 90",
        "protocolo": "Se PA sistólica < 90 → iniciar protocolo de choque"
    },
    {
        "id": 10,
        "condicao": "risco_sistemico == 'alto'",
        "protocolo": "Se risco sistêmico alto → ativar estado de emergência"
    }
]