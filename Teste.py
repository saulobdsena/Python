<<<<<<< HEAD
data = input('Qual a sua data de nascimento? ')  # exemplo: 28/04/2000
dia, mes, ano = data.split('/')

# Transforma mes em número inteiro para buscar no dicionário
mes = int(mes)

dicionario = {
    1: 'Janeiro',
    2: 'Fevereiro',
    3: 'Março',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'Setembro',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro'
}

print(f'{dia} de {dicionario.get(mes)} de {ano}')
=======
print('oi')
>>>>>>> cce494524a57167ef62408106e48d66c55801ead
