n = int(input('Número de termos: '))
a = 0
b = 1
i = 2

if n == 1:
    print(a)
else:
    print(f'{a} {b}', end=' ')
    while i < n:
        c = a + b
        print(c, end=' ')
        a = b
        b = c
        i += 1
