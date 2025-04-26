comida = 'arroz'

def func():
    global comida
    comida = 'batata'
    print(comida)

func()
print(comida)