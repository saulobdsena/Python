
from datetime import datetime, timedelta

M = 0.17

TOLERANCIA_MINUTOS = 15
VALOR_FIXO = 10.0
TEMPO_FIXO_HORAS = 3
VALOR_EXTRA_POR_20_MIN = 2 + M

def calcular_valor(entrada_str, saida_str):
    formato = "%H:%M"
    entrada = datetime.strptime(entrada_str, formato)
    saida = datetime.strptime(saida_str, formato)

    if saida < entrada:
        saida += timedelta(days=1)

    duracao = saida - entrada
    minutos = duracao.total_seconds() / 60

    if minutos <= TOLERANCIA_MINUTOS:
        return 0.0
    elif minutos <= TEMPO_FIXO_HORAS * 60:
        return VALOR_FIXO
    else:
        minutos_excedentes = minutos - TEMPO_FIXO_HORAS * 60
        blocos_20min = (minutos_excedentes + 19) // 20
        return VALOR_FIXO + blocos_20min * VALOR_EXTRA_POR_20_MIN
