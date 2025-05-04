class Cachorro(object):

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

domi = Cachorro('Dominique', 10)
print(domi.idade)