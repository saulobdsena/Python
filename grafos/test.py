# Representação do grafo
# O vértice 'A' está conectado a 'B' e 'C'
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}

u = 'A'

# O loop "PARA CADA vizinho DE u"
for vizinho in grafo[u]:
    print(f"Vértice {u} está conectado a {vizinho}")