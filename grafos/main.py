import networkx as nx
import matplotlib.pyplot as plt


# ---------- Linked list node ----------
class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt

# ---------- Helper to add to linked list ----------
def add_neighbor(head, value):
    # insert at head (fast). You could also insert at tail if you prefer.
    return Node(value, head)

def find_degree(uf_name):
    head = adj[uf_name]
    degree = 0
    while head:
        degree += 1
        head = head.next
    return degree

def higher_degree_neighbors(adj):
    max_degree = -1
    uf_max = None
    for uf in states:
        degree = find_degree(uf)
        if degree > max_degree:
            max_degree = degree
            uf_max = uf
    return uf_max, max_degree

def lower_degree_neighbors(adj):
    min_degree = float('inf')
    uf_min = None
    for uf in states:
        degree = find_degree(uf)
        if degree < min_degree:
            min_degree = degree
            uf_min = uf
    return uf_min, min_degree

# ---------- States order (UF codes) ----------
states = [
    "AC","AL","AP","AM","BA","CE","DF","ES","GO","MA","MT","MS",
    "MG","PA","PB","PR","PE","PI","RJ","RN","RS","RO","RR","SC",
    "SP","SE","TO"
]

# Your neighbor dictionary (unchanged)
estados_vizinhos = {
    "AC": {"AM","RO"},
    "AL": {"BA","PE","SE"},
    "AP": {"PA"},
    "AM": {"AC","RO","MT","PA","RR"},
    "BA": {"AL","SE","PE","PI","TO","GO","MG","ES"},
    "CE": {"PI","PE","PB","RN"},
    "DF": {"GO"},
    "ES": {"BA","MG","RJ"},
    "GO": {"DF","MT","MS","MG","BA","TO"},
    "MA": {"PA","TO","PI"},
    "MT": {"RO","AM","PA","TO","GO","MS"},
    "MS": {"MT","GO","MG","SP","PR"},
    "MG": {"BA","ES","RJ","SP","MS","GO"},
    "PA": {"AP","AM","RR","MT","TO","MA"},
    "PB": {"RN","CE","PE"},
    "PR": {"SP","MS","SC"},
    "PE": {"CE","PB","PI","BA","AL"},
    "PI": {"MA","CE","PE","BA","TO"},
    "RJ": {"ES","MG","SP"},
    "RN": {"CE","PB"},
    "RS": {"SC"},
    "RO": {"AC","AM","MT"},
    "RR": {"AM","PA"},
    "SC": {"PR","RS"},
    "SP": {"RJ","MG","MS","PR"},
    "SE": {"AL","BA"},
    "TO": {"PA","MA","PI","BA","GO","MT"},
}

# ---------- Build adjacency "linked lists" ----------
# adj[UF] -> head of linked list of neighbors
adj = {uf: None for uf in states}

# Build from the dict
for uf, neighs in estados_vizinhos.items():
    head = None
    for v in neighs:
        head = add_neighbor(head, v)
    adj[uf] = head

# (Optional) print each UF neighbors by walking the linked list
def iter_list(head):
    cur = head
    while cur:
        yield cur.value
        cur = cur.next

for uf in states:
    print(f"{uf} tem como vizinhos: {', '.join(iter_list(adj[uf]))}")

# ---------- Build adjacency matrix ----------
index = {uf: i for i, uf in enumerate(states)}
n = len(states)
matriz = [[0]*n for _ in range(n)]

for uf in states:
    i = index[uf]
    cur = adj[uf]
    while cur:
        v = cur.value
        j = index[v]
        matriz[i][j] = 1
        matriz[j][i] = 1  # undirected: mirror it
        cur = cur.next

# ---------- Print matrix nicely ----------
print("\nMatriz de Adjacência (0/1):")
print("    " + " ".join(f"{s:>2}" for s in states))
for i, uf in enumerate(states):
    print(f"{uf:>2}  " + " ".join(str(matriz[i][j]).rjust(2) for j in range(n)))

#---------- Find UF with highest degree ----------
print(f"Escolha o UF para calcular o grau: ")
print(f"Grau do UF: {find_degree(input().strip().upper())}")

uf_max, max_degree = higher_degree_neighbors(adj)
print(f"\nUF com maior grau: {uf_max} (grau {max_degree})")

uf_min, min_degree = lower_degree_neighbors(adj)
print(f"UF com menor grau: {uf_min} (grau {min_degree})")

G = nx.Graph()
for uf in states:
    G.add_node(uf)
    cur = adj[uf]
    while cur:
        G.add_edge(uf, cur.value)
        cur = cur.next
plt.figure(figsize=(12, 8))
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500)
plt.title("Grafo dos Estados Brasileiros")
plt.show()