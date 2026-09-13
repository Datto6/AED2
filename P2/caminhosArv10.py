import math
def caminhosFilho(M,D,filhos,no,k): 
    # M[i][k]= possiveis caminhos consecutivos onde maior nó é i,  com tamanho k
    # D[i][k] possiveis caminhos estritamente descendentes com tamanho k
    if k<=0:
        return 0
    if k==1:
        D[no][k]=1
        M[no][k]=1
        return 1
    if M[no][k]!=None:
        return M[no][k]
    D[no][k]=0
    r=0 #iniciando subsequencia em A[i]
    for filho in filhos[no]: #número de caminhos k-1 de cada filho estritamente descendentes
        r+=caminhosFilho(M,D,filhos,filho,k-1) 
    D[no][k]=r     #Soma simples
    filhos_i = filhos[no]
    if len(filhos_i) == 2: #se tiver dois filhos
        u = filhos_i[0]
        w = filhos_i[1]
        for q in range(1, k-1): #pega caminhos que passam pelo nó i, em todos os cortes possíveis de k
            caminhosFilho(M,D,filhos, u, q)
            caminhosFilho(M,D,filhos, w, k-q-1)
            r += (D[u][q]*D[w][k-q-1]) #multiplicando caminhos estritamente descendentes de um filho,(adicionando pelo principio multiplicativo)
    M[no][k]=r
    return r

def caminhosAux(pai,nos):
    n=len(pai)
    M=[[None for _ in range(n+1)] for _ in range(n+1)]
    D=[[None for _ in range(n+1)] for _ in range(n+1)]
    filhos={}
    for i in range(len(pai)):
        filhos[nos[i]]=[]
    for i in range(len(pai)):
        if pai[i] != -1:
            filhos[pai[i]].append(nos[i])
    print(filhos)
    
    resultado = [0] * (n+1)
    for no in nos:
        for k in range(1, n+1):
            resultado[k] += caminhosFilho(M, D,filhos, no, k)
    for i in range(2,n+1):
        resultado[i]*=2 #podem ter 2 orentações na árvore binária, só estamos calculando descendente 
    for i in M:
        print(i)
    return resultado

pai = [-1, 1, 1, 2, 2, 3,3]
nos=[1,2,3,4,5,6,7]
print(caminhosAux(pai,nos)) 