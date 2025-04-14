n = int(input('Informe o numero: '))
fatorial = 1
i = n

while i >= 1:
    fatorial *= i
    i = i - 1

print(f'O fatorial de {n} é {fatorial}')
