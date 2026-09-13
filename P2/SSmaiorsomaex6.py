def LiSSUM(M,A,i):
    if M[i]!=None:
        return M[i]
    r=(1,A[i]) #iniciando subsequencia em A[i]
    for j in range(i):
        if A[j]<A[i]:
            r1=LiSSUM(M,A,j)
            r1=(r1[0]+1,r1[1]+A[i]) #levamos o elemento A[i]
            if r[0]<=r1[0]:
                if r1[0]>r[0] or r[1]>r1[1]: #se tamanho é maior, vai direto, mas se tamanho for igual, tem que olhar soma
                    r=r1
    M[i]=r
    return r

def LISAUX(A):
    n=len(A)
    M=[None]*n
    LiSSUM(M,A,0) #inicializar primeiro, só pra iniciar
    r=M[0]

    for i in range(1,len(M)): #chamo para todos os valores de i porque quero maior LiS para toda a lista, não só a que termina no último valor
        r1=LiSSUM(M,A,i)
        if r[0]<=r1[0]:
            if r1[0]>r[0] or r[1]>r1[1]: #se tamanho é maior, vai direto, mas se tamanho for igual, tem que olhar soma
                r=r1
    print(r)

A = [1,2,3,0]
LISAUX(A)

testes = [
    ([1, 2, 3, 4, 5], (5, 15)),
    ([5, 4, 3, 2, 1], (1, 1)),
    ([2, 4, 1, 5, 6], (4, 17)),
    ([1, 2, 3, 4, 0, 10], (5, 20)),
    ([-5, -4, -3, -2, -1], (5, -15)),
    ([-10, -5, -8, -3, -6, -1], (4, -25)),
    ([1, 1, 1, 1, 2], (2, 3)),
    ([1, 2, 3, 0], (3, 6)),
    ([10, 1, 2, 3, 4], (4, 10)),
    ([3, 1, 2, 4, 5], (4, 12)),
    ([2, 4, 1, 5, 6, -4, -3, -2, -1], (4, -10)),
    ([5, 1, 6, 2, 3, 4, 0, 7], (5, 17))
]

for A, esperado in testes:
    M = [None] * len(A)
    resultado = LiSSUM(M, A, len(A)-1)
    print(A)
    print("Resultado:", resultado)
    print("Esperado: ", esperado)
    print()