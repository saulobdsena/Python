
grafo_cidades = {
    "Manaus": ["Belém", "Fortaleza"],
    "Belém": ["Manaus", "Recife", "Fortaleza"],
    "Fortaleza": ["Manaus", "Belém", "Recife", "Salvador"],
    "Recife": ["Belém", "Fortaleza", "Salvador", "BH"],
    "Salvador": ["Fortaleza", "Recife", "BH", "Brasília"],
    "BH": ["Recife", "Salvador", "RJ", "Brasília", "SP"],
    "Brasília": ["Salvador", "BH", "SP", "Goiânia"],
    "RJ": ["BH", "SP"],
    "SP": ["BH", "Brasília", "RJ", "Curitiba", "Goiânia"],
    "Goiânia": ["Brasília", "SP", "Curitiba"],
    "Curitiba": ["SP", "Goiânia", "Porto Alegre"],
    "Porto Alegre": ["Curitiba"]
}

def bfs(graph, s):

    color = ["White", "Gray", "Black"]
    distance = []
    no_pai = []

    if u == s:
        color[u] = "Gray"
        distance = 0
        no_pai = None

    if u != s:
        for u in (u != s):
            color[u] = "White"
            no_pai = None

    fila = []

    while len(fila) != 0:
        

        

    
