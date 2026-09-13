import math
def EncMerge(M,i,j,p,s):
    #Preenche uma tabela M[i][j], onde M[i][j] representa o menor custo de concatenar as listas encadeadas ordenadas no intervalo inclusivo (i,j)
    #No final, é só pegar M[0][n-1], representante do intervalo inteiro das listas encadeadas
    if i==j: #corte dele mesmo retorna 0 
        return 0
    if M[i][j]!=-1: #se ja resolvemos retornamos isso
        return M[i][j]
    r=math.inf
    for k in range(i,j): #iteramos sobre o intervalo i,j para achar melhor ponto de corte entre as listas encadeadas
        somaL=sum(p[i:k+1]) #soma de custo de corte à esquerda
        somaR=sum(p[k+1:j+1]) #o mesmo para a direita
        c=EncMerge(M,i,k,p,s)+EncMerge(M,k+1,j,p,s)+somaL+somaR  #custo do corte k
        if c<r:
            r=c
            s[i][j]=k #anotamos o melhor corte nessa tabela
    M[i][j]=r
    return r

def ImprimeOrdem(M,i,j,s):
    if i==j:
        return f"L{i}"
    else:
        return f"({ImprimeOrdem(M,i,s[i][j],s)} + {ImprimeOrdem(M,s[i][j]+1,j,s)})"

def EncAux(p):
    n=len(p) #Alocamos o suficiente para caber todas as listas encadeadas
    M=[[-1 for _ in range(n)] for _ in range(n)] #alocando valores não inicializados
    s=[[-1 for _ in range(n)] for _ in range(n)]
    EncMerge(M,0,n-1,p,s)
    print(ImprimeOrdem(M,0,n-1,s))
    print(M[0][n-1])

p=[1]*20
EncAux(p)