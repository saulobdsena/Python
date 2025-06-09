i = 0
contagem = 0
todos = 0 
while i < 6:
    numero = float(input(''))
    if(numero > 0):
        contagem+=1
        todos+=numero
    i+=1

print(f'{contagem} valores positivos')
print(f'{todos/contagem:.1f}')
