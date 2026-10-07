from pydantic import BaseModel
from agents import Agent, function_tool

from tools import analisar_risco


@function_tool
def ferramenta_analisar_risco(
    idade_media: float,
    carga_sistema: float,
    tempo_espera: float,
    fc_media: float,
    spo2_media: float,
    pa_sistolica: float,
    temperatura: float,
    densidade_eventos: int,
    eventos_24h: int,
    disponibilidade_recursos: float
) -> dict:
    """
    Analisa os dados do caso utilizando o modelo preditivo
    treinado do CardioIA.
    """

    dados = {
        "idade_media": idade_media,
        "carga_sistema": carga_sistema,
        "tempo_espera": tempo_espera,
        "fc_media": fc_media,
        "spo2_media": spo2_media,
        "pa_sistolica": pa_sistolica,
        "temperatura": temperatura,
        "densidade_eventos": densidade_eventos,
        "eventos_24h": eventos_24h,
        "disponibilidade_recursos": disponibilidade_recursos
    }

    return analisar_risco(dados)


agente_risco = Agent(
    name="Analista de Risco",
    instructions=(
        "Você é o Analista de Risco do CardioIA. "
        "Sua função é analisar os dados recebidos utilizando "
        "obrigatoriamente a ferramenta ferramenta_analisar_risco. "
        "Não invente probabilidades ou classificações."
    ),
    tools=[ferramenta_analisar_risco]
)
from tools import consultar_protocolos


@function_tool
def ferramenta_consultar_protocolos(
    carga_sistema: float,
    tempo_espera: float,
    fc_media: float,
    spo2_media: float,
    pa_sistolica: float,
    temperatura: float,
    densidade_eventos: int,
    eventos_24h: int,
    disponibilidade_recursos: float,
    risco_alto: bool
) -> list[str]:
    """
    Consulta a base de conhecimento do CardioIA
    e retorna os protocolos aplicáveis ao caso.
    """

    dados = {
        "carga_sistema": carga_sistema,
        "tempo_espera": tempo_espera,
        "fc_media": fc_media,
        "spo2_media": spo2_media,
        "pa_sistolica": pa_sistolica,
        "temperatura": temperatura,
        "densidade_eventos": densidade_eventos,
        "eventos_24h": eventos_24h,
        "disponibilidade_recursos": disponibilidade_recursos
    }

    return consultar_protocolos(
        dados,
        risco_alto=risco_alto
    )


agente_protocolos = Agent(
    name="Especialista em Protocolos",
    instructions=(
        "Você é o Especialista em Protocolos do CardioIA. "
        "Consulte obrigatoriamente a ferramenta "
        "ferramenta_consultar_protocolos para identificar "
        "os protocolos aplicáveis ao caso. "
        "Não invente protocolos."
    ),
    tools=[ferramenta_consultar_protocolos]
)
class RespostaCardioIA(BaseModel):
    probabilidade_risco: float
    classificacao: str
    protocolos_sugeridos: list[str]
    acoes_operacionais: list[str]


agente_planejador = Agent(
    name="Planejador de Resposta",
    instructions=(
        "Você é o Planejador de Resposta do CardioIA. "
        "Sua função é consolidar a análise de risco e os protocolos "
        "identificados pelos agentes anteriores. "
        "Gere uma resposta final estruturada com a probabilidade de risco, "
        "classificação, protocolos sugeridos e ações operacionais. "
        "Não altere a probabilidade calculada pelo modelo e não invente "
        "protocolos que não tenham sido identificados."
    ),
    output_type=RespostaCardioIA
)
agente_risco.handoffs = [agente_protocolos]

agente_protocolos.handoffs = [agente_planejador]


agente_orquestrador = Agent(
    name="Orquestrador CardioIA",
    instructions=(
        "Você é o Orquestrador do CardioIA. "
        "Sua função é coordenar a análise de novos casos. "
        "Ao receber os dados de um caso, encaminhe a análise "
        "para o Agente Analista de Risco. "
        "O fluxo deve continuar para o Especialista em Protocolos "
        "e depois para o Planejador de Resposta."
    ),
    handoffs=[agente_risco]
)