from collections import deque
def digitoMin(D,k):
    #Cria pilha monotonica de dígitos, cada retirada da pilha decrementando k
    #k retiradas, n-k dígitos restantes, minimiza resultado
    pilha=[]
    for i in range(len(D)):
        if len(pilha)==0:
            pilha.append(D[i])
        else:
            while len(pilha)>0 and k>0 and pilha[-1]>D[i]:
                pilha.pop()
                k-=1
            pilha.append(D[i])
    while k > 0:
        pilha.pop()
        k -= 1
    return pilha

D=[9,9,3,2,9,1,3,9]
k=4
print(digitoMin(D,k))