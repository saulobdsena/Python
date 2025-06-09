
from prefixos_sp import PrefixosSP
from prefixos_rj import PrefixosRJ # type: ignore
from prefixos_es import PrefixosES # type: ignore

class IdentificadorEstado:
    def __init__(self):
        self.estados = {
            "São Paulo": PrefixosSP(),
            "Rio de Janeiro": PrefixosRJ(),
            "Espírito Santo": PrefixosES()
        }

    def identificar(self, placa):
        for nome_estado, classe in self.estados.items():
            if classe.pertence(placa):
                return nome_estado
        return "Outro Estado"
