
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
    "Porto Alegre": ["Curitiba"],
    "Floripa" : []
}


def bfs(graph, s):

    color = {}
    distance = {}
    no_pai = {}

    for u in graph:
        color[u] = "White"
        distance[u] = float('inf')
        no_pai[u] = None

    color[s] = "Gray"
    distance[s] = 0
    no_pai[s] = None

    fila = []
    fila.append(s)

    while len(fila) != 0:
        
        u = fila.pop(0)

        for vizinho in graph[u]:
            if color[vizinho] == "White":
                color[vizinho] = "Gray"
                distance[vizinho] = distance[u] + 1
                no_pai[vizinho] = u
                fila.append(vizinho)
        
        color[u] = "Black"
    
    return color, distance, no_pai
 

def reconstruir_caminho(no_pai, destino):
    caminho = []
    atual = destino
    while atual != None:
        caminho.append(atual)
        atual = no_pai[atual]
    caminho.reverse()
    return caminho , len(caminho)
     
color, distance, no_pai = bfs(grafo_cidades, "Fortaleza")
caminho, tamanho = reconstruir_caminho(no_pai, "Floripa")

print(color)

if distance["Floripa"] == float('inf'):
    print("Essa rota não existe")
else :
    print(distance)

print(no_pai)
print(caminho)
print(tamanho - 1)    

    

        

        

    
