class Maquina(object):
    def __init__(self, minimo, maximo):
        self.__minimo = minimo
        self.__maximo = maximo

    def get_minimo(self):
        return self.__minimo

    def set_minimo(self, minimo):
        self.__minimo = minimo

    def get_maximo(self):
        return self.__maximo

    def set_maximo(self, maximo):
        self.__maximo = maximo


class Lavadora(Maquina):
    def __init__(self, minimo, maximo):
        super().__init__(minimo, maximo)

    def verificarLavar(self, quantidade):
        return self.get_minimo() <= quantidade <= self.get_maximo()


class Secadora(Maquina):
    def __init__(self, minimo, maximo):
        super().__init__(minimo, maximo)

    def verificarSecar(self, quantidade):
        return self.get_minimo() <= quantidade <= self.get_maximo()


# Entrada de dados
quantidade = int(input())

lineL = input().split()
lineS = input().split()

minL = int(lineL[0])
maxL = int(lineL[1])

minS = int(lineS[0])
maxS = int(lineS[1])

# Instanciando os objetos
lavadora = Lavadora(minL, maxL)
secadora = Secadora(minS, maxS)

# Verificação e saída
if lavadora.verificarLavar(quantidade) and secadora.verificarSecar(quantidade):
    print('possivel')
else:
    print('impossivel')
