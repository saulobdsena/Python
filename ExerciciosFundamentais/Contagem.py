quantidade = int(input('Informe a quantidade de notas: '))
notas = 0
contador = 0
i = 0

while i < quantidade:
    nota = int(input('Informe a nota: '))
    if nota >= 50 :
        contador += 1
    i = i + 1

print(f'Número de alunos que passaram no exame: {contador}')