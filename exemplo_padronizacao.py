from abc import ABC, abstractmethod

class nomeDaClasseDeveSerObjetivoEClaroParaOLeitorMesmoQueSejaLongo:
    """
    Aqui você colocará uma descrição detalhada da classe, explicando seu propósito e como ela deve ser utilizada.
    Não econimize nas palavras, pois a clareza é fundamental para a manutenção futura do código.
    """
    
    def __init__(self, parametro1: str, parametro2: str) -> None:
        """
        Inicializa a classe com os parâmetros fornecidos.

        Args:
            parametro1 (str): Descrição do primeiro parâmetro.
            parametro2 (str): Descrição do segundo parâmetro.
        """
        self.parametro1 = parametro1
        self.parametro2 = parametro2
    
    def exemploDeFuncao(self, parametroA: int, parametroB: int) -> float:
        """
        Descrição detalhada da função, explicando o que ela faz, seus parâmetros e o valor retornado.

        Args:
            parametroA (int): Descrição do primeiro parâmetro.
            parametroB (int): Descrição do segundo parâmetro.
        """
        # Implementação da função
        resultado = parametroA + parametroB  # Exemplo de operação
        return resultado  # Retorna o resultado da operação


class ClasseSuperior(ABC):
    """
    Se uma classe possuir características ou comportamentos que podem ser reutilizados por outras classes,
    é recomendável criar uma classe superior (superclasse) para encapsular essas funcionalidades comuns.
    Siga o mesmo padrão de documentação detalhada para a superclasse e suas subclasses.
    """
    
    @abstractmethod
    def metodo_abstrato(self):
        """
        Descrição do método abstrato que deve ser implementado por todas as subclasses.
        """
        pass
    
    @abstractmethod
    def outro_metodo_abstrato(self, parametroX: str) -> None:
        """
        Descrição do segundo método abstrato que deve ser implementado por todas as subclasses.

        Args:
            parametroX (str): Descrição do parâmetro.
        """
        pass


class ClasseDerivada(ClasseSuperior):
    """
    Descrição detalhada da classe derivada, explicando como ela estende a funcionalidade da superclasse.
    """
    
    def metodo_abstrato(self):
        """
        Implementação do método abstrato definido na superclasse.
        """
        # Implementação específica para esta classe
        return "A Resposta sobre a vida, o universo e tudo mais é 42."
    
    def outro_metodo_abstrato(self, parametroX: str) -> None:
        """
        Implementação do segundo método abstrato definido na superclasse.

        Args:
            parametroX (str): Descrição do parâmetro.
        """
        # Implementação específica para esta classe
        print(f"Processando o parâmetro: {parametroX}")
    
    
            