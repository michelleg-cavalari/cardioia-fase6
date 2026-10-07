import os
from dotenv import load_dotenv

load_dotenv()
from agents import Runner

from agents_cardioia import agente_orquestrador
if not os.getenv("OPENAI_API_KEY"):
    print("ATENÇÃO: OPENAI_API_KEY não configurada no arquivo .env")

caso = """
Analise o seguinte caso no CardioIA:

idade_media: 62
carga_sistema: 92
tempo_espera: 75
fc_media: 118
spo2_media: 89
pa_sistolica: 100
temperatura: 37.5
densidade_eventos: 7
eventos_24h: 5
disponibilidade_recursos: 25

Siga obrigatoriamente o fluxo multiagente definido no sistema.
"""


def main():
    print("\n--- CARDIOIA | SISTEMA MULTIAGENTE ---\n")

    # Histórico inicial da conversa
    historico = [
        {
            "role": "user",
            "content": caso
        }
    ]

    # Executa o fluxo multiagente
    resultado = Runner.run_sync(
        agente_orquestrador,
        historico
    )

    # Atualiza o histórico com todas as mensagens
    # e interações produzidas durante a execução
    historico = resultado.to_input_list()

    print("\n--- RESPOSTA FINAL ---")
    print(resultado.final_output)

    print("\n--- HISTÓRICO DE MENSAGENS ---")
    print(f"Itens registrados no histórico: {len(historico)}")

if __name__ == "__main__":
    main()