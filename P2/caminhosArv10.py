import math
def caminhosFilho(M,filhos,no,k): # M[i]= (l,r)(comprimento de caminho de folha até nó )
    if k<=0:
        return 0
    if k==1:
        return 1
    if M[no][k]!=None:
        return M[no][k]
    r=0 #iniciando subsequencia em A[i]
    for filho in filhos[no]:
        r+=caminhosFilho(M,filhos,filho,k-1) #pegando o número de caminhos k-1 de cada filho
    filhos_i = filhos[no]
    if len(filhos_i) == 2: #se tiver dois filhos
        u = filhos_i[0]
        w = filhos_i[1]
        for q in range(1, k-1): #pega caminhos que passam pelo nó i, em todos os cortes possíveis de k
            r += (caminhosFilho(M,filhos, u, q)*caminhosFilho(M,filhos, w, k-q-1)) 
    M[no][k]=r
    return r

def caminhosAux(pai,nos):
    n=len(pai)
    M=[[None for _ in range(n+1)] for _ in range(n+1)]
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
            resultado[k] += caminhosFilho(M, filhos, no, k)
    for i in M:
        print(i)
    return resultado

pai = [-1, 1, 1, 2, 2, 3,3]
nos=[1,2,3,4,5,6,7]
print(caminhosAux(pai,nos)) 