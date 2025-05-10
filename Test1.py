class Maquina(object):

    def __init__(self, minimo, maximo):
        self.minimo = minimo
        self.maximo = maximo

    
class Lavadora(Maquina):

    def __init__(self, minimo, maximo):
        super().__init__(minimo, maximo)

    def verificarLavar(self, quantidade):
        if quantidade >= self.minimo and quantidade <= self.maximo:
            return 1
        else:
            return 0


class Secadora(Maquina):

    def __init__(self, minimo, maximo):
        super().__init__(minimo, maximo)

    def verificarSecar(self, quantidade):
        if quantidade >= self.minimo and quantidade <= self.maximo:
            return 1
        else:
            return 0


quantidade = int(input(''))

lineL = input().split()
lineS = input().split()

minL = int(lineL[0])
maxL = int(lineL[1])

minS = int(lineS[0])
maxS = int(lineS[1])


lavadora = Lavadora(minL, maxL)
secadora = Secadora(minS, maxS)


if lavadora.verificarLavar(quantidade) == 1 and secadora.verificarSecar(quantidade) == 1:
    print('possivel')
else:
    print('impossivel')