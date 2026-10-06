def greedyBoat(A,C):
    A.sort()
    boats=[]
    while len(A)>0:
        elem=A.pop()
        if len(A)>0 and A[0]+elem<=C:
            boats.append((elem,A[0]))
            A.pop(0)
        else:
            boats.append((elem,-1))
    return boats

# Teste 1 — exemplo do enunciado
A = [3, 5, 3, 4, 7, 9]
C = 10
# Esperado: [(9, -1), (7, 3), (5, 3), (4, -1)]
print(greedyBoat(A,C))
# Teste 2 — todos conseguem formar pares
A = [1, 2, 3, 4]
C = 5
# Esperado: [(4, 1), (3, 2)]
print(greedyBoat(A,C))

# Teste 3 — ninguém consegue formar par
A = [4, 4, 4, 4]
C = 5
# Esperado: [(4, -1), (4, -1), (4, -1), (4, -1)]
print(greedyBoat(A,C))

# Teste 4 — uma pessoa
A = [7]
C = 10
# Esperado: [(7, -1)]
print(greedyBoat(A,C))

# Teste 5 — exatamente duas pessoas que cabem
A = [3, 7]
C = 10
# Esperado: [(7, 3)]
print(greedyBoat(A,C))

# Teste 6 — exatamente duas pessoas que não cabem
A = [4, 7]
C = 10
# Esperado: [(7, -1), (4, -1)]
print(greedyBoat(A,C))