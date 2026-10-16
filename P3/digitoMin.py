from collections import deque
def digitoMin(D,k):
    pilha=[]
    for i in range(len(D)):
        if len(pilha)==0:
            pilha.append(D[i])
        else:
            while k>0 and pilha[-1]>D[i]:
                pilha.pop()
                k-=1
            pilha.append(D[i])
    return pilha

D=[1,4,3,2,2,1,9]
k=3
print(digitoMin(D,k))