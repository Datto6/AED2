def possivel(i,cor,V,A):
    for regiao in range(i): #checa todos os anteriores a i
        if (V[i][regiao] or V[regiao][i]) and A[regiao]==cor:
            return False #se forem vizinhos, e a cor da região for igual, não posso incluir esse cara
    return True
def colore(n,k,V,A,i):
    if i==n:
        print(" ".join(str(j) for j in A))
        return
    for cor in range(k):
        if possivel(i,cor,V,A):
            A[i]=cor
            colore(n,k,V,A,i+1)

n = 4
k = 4
V = [
    [False, True,  True,  True],
    [True,  False, True,  True],
    [True,  True,  False, True],
    [True,  True,  True,  False]
]
A = [-1] * n

colore(n, k, V, A, 0)