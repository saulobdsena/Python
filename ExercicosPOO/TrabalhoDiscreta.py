import numpy as np
import pandas as pd

# Estações conforme imagem
stations = ["Shopping", "Parque", "Terminal", "Centro", "Praça", "Avenida"]

# MATRIZ DE ADJACÊNCIA DO METRÔ (imagem final)
metro_adj_matrix = np.array([
    [1, 1, 0, 0, 0, 0],  # Shopping
    [0, 1, 1, 1, 0, 0],  # Parque
    [0, 1, 1, 0, 0, 0],  # Terminal
    [1, 0, 0, 1, 1, 0],  # Centro
    [0, 0, 0, 0, 1, 0],  # Praça
    [1, 0, 0, 1, 1, 1],  # Avenida
])

# MATRIZ DAS LINHAS DE ÔNIBUS (fornecida)
bus_matrix = np.array([
    [0, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0],
])

# Funções de propriedades
def is_reflexive(matrix):
    return all(matrix[i][i] == 1 for i in range(len(matrix)))

def is_symmetric(matrix):
    return np.array_equal(matrix, matrix.T)

def is_antisymmetric(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j] == 1 and matrix[j][i] == 1:
                return False
    return True

def is_asymmetric(matrix):
    return np.all((matrix + matrix.T) <= 1) and np.all(np.diag(matrix) == 0)

def is_transitive(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j]:
                for k in range(n):
                    if matrix[j][k] and not matrix[i][k]:
                        return False
    return True

# Fechos
def reflexive_closure(matrix):
    closure = matrix.copy()
    for i in range(len(matrix)):
        closure[i][i] = 1
    return closure

def symmetric_closure(matrix):
    return np.maximum(matrix, matrix.T)

def transitive_closure(matrix):
    closure = matrix.copy()
    n = len(matrix)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                closure[i][j] = closure[i][j] or (closure[i][k] and closure[k][j])
    return closure

# Verificação das propriedades
reflexive = is_reflexive(metro_adj_matrix)
symmetric = is_symmetric(metro_adj_matrix)
asymmetric = is_asymmetric(metro_adj_matrix)
antisymmetric = is_antisymmetric(metro_adj_matrix)
transitive = is_transitive(metro_adj_matrix)

# Fechos, se necessário
reflexive_cl = None if reflexive else reflexive_closure(metro_adj_matrix)
symmetric_cl = None if symmetric else symmetric_closure(metro_adj_matrix)
transitive_cl = None if transitive else transitive_closure(metro_adj_matrix)

# Verificações adicionais
is_equivalence = reflexive and symmetric and transitive
is_partial_order = reflexive and antisymmetric and transitive

# ELEMENTOS ESPECIAIS
def find_maximal_elements(matrix):
    n = len(matrix)
    maximals = []
    for i in range(n):
        if all(matrix[i][j] == 0 for j in range(n) if i != j):
            maximals.append(i)
    return maximals

def find_minimal_elements(matrix):
    n = len(matrix)
    minimals = []
    for j in range(n):
        if all(matrix[i][j] == 0 for i in range(n) if i != j):
            minimals.append(j)
    return minimals

def find_greatest_element(matrix):
    n = len(matrix)
    for i in range(n):
        if all(matrix[i][j] == 1 or i == j for j in range(n)):
            return i
    return None

def find_least_element(matrix):
    n = len(matrix)
    for j in range(n):
        if all(matrix[i][j] == 1 or i == j for i in range(n)):
            return j
    return None

maximal_indices = find_maximal_elements(metro_adj_matrix)
minimal_indices = find_minimal_elements(metro_adj_matrix)
greatest_index = find_greatest_element(metro_adj_matrix)
least_index = find_least_element(metro_adj_matrix)

# COMPOSIÇÃO METRÔ ∘ ÔNIBUS
def boolean_matrix_composition(A, B):
    n = len(A)
    result = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if A[i][k] and B[k][j]:
                    result[i][j] = 1
                    break
    return result

composition_matrix = boolean_matrix_composition(metro_adj_matrix, bus_matrix)

# RESULTADOS (exibição em console)
print("Propriedades:")
print("Reflexiva:", reflexive)
print("Simétrica:", symmetric)
print("Assimétrica:", asymmetric)
print("Antissimétrica:", antisymmetric)
print("Transitiva:", transitive)
print("Equivalência:", is_equivalence)
print("Ordem Parcial:", is_partial_order)

print("\nElementos Maximais:", [stations[i] for i in maximal_indices])
print("Elementos Minimais:", [stations[i] for i in minimal_indices])
print("Maior Elemento:", stations[greatest_index] if greatest_index is not None else "Não existe")
print("Menor Elemento:", stations[least_index] if least_index is not None else "Não existe")

print("\nComposição Metrô ∘ Ônibus:")
print(pd.DataFrame(composition_matrix, index=stations, columns=stations))
