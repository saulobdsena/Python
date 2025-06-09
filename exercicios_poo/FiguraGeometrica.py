import math

class Retangulo():

    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def calcular_area(self):
        print(f'A area sera de {self.altura * self.largura}')

    def verificar(self):
        if(self.altura == self.largura):
            print('isso é um quadrado')
        else:
            print('isso é um retangulo')

class Circulo():
    
    def __init__(self, raio):
        self.raio = raio

    def calcular_perimetro(self):
        print(f'a perimetro do circulo é {self.raio * 2 * math.pi:.2f}')

    def calcular_area(self):
        print(f'a area do circulo é {(math.pi * (self.raio ** 2)):.2f}')

def main():

    circulo = Circulo(5)

    retangulo = Retangulo(2, 4)


    retangulo.calcular_area()

    retangulo.verificar()

    circulo.calcular_area()

    circulo.calcular_perimetro()

if __name__ == "__main__":
    main()