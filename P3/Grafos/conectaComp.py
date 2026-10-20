from collections import deque
from basico import grafoBuilder, Vertice
def componentes(G):
    #Conta quantos componentes conexos e de qual cada um pertence
    n=len(G)
    comp=[0]*n
    c=0 
    for i in range(len(G)): #Fazer BFS para atingir todos
        if comp[i]==0:
            c=c+1
            comp[i]=c
            queue=deque()
            queue.append(G[i])
            while len(queue)!=0:
                u=queue.popleft()
                v=u.next
                while v!=None: #Percorrer vizinhos de u
                    if comp[v.index]==0:
                        comp[v.index]=c
                        queue.append(G[v.index]) #Colocar v na fila somente se ainda nao foi descoberto
                    v=v.next
    return (c,comp)

#Contar quantos de cada componente conexo e juntar 
def desconexos(saida,G):
    hist={}
    componentes=saida[1]
    n=len(G)
    for i in range(len(componentes)): #Contar quantos de cada componente conexo tem 
        atual=componentes[i]
        if hist.get(atual,None)==None:
            hist[atual]=1
        else:
            hist[atual]+=1
    
    pares_desconexos=0
    print(hist)
    for componente,contagem in hist.items():
        pares_desconexos+=(contagem*(n-contagem))/2
    pares_desconexos=int(pares_desconexos)
    return (pares_desconexos,len(hist.keys())-1)

V=[0,1,2,3,4,5,6,7]
E=[[0,1],[1,2],[2,3],[0,3],[4,5],[5,6]]
G=grafoBuilder(V,E)
saida=componentes(G)
print(saida)
print(desconexos(saida,G))