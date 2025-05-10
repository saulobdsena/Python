class ConversorRomano:
    def inteiro_para_romano(self, numero):
        valores_romanos = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]

        resultado = ""
        for valor, simbolo in valores_romanos:
            while numero >= valor:
                resultado += simbolo
                numero -= valor

        return resultado


conversor = ConversorRomano()
print(conversor.inteiro_para_romano(99))    
print(conversor.inteiro_para_romano(1999))  
print(conversor.inteiro_para_romano(4))     
print(conversor.inteiro_para_romano(2025))  
