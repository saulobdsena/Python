def somar(*args):
    soma = 0
    
    for elem in args:
        soma+=elem
    print(soma)

somar(1,2,3,4)