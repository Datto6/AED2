from collections import deque
from basico import grafoBuilder,Vertice

def Diametro(G,s):
    #Dado um grafo G e um vertice s, calcular quantos caminhos mínimos únicos para cada v a partir de s
    n=len(G)
    dist=[-1]*n
    pai=[-1]*n
    queue=deque()
    queue.append(s)
    dist[s.index]=0
    vmax=s
    distMax=0
    while len(queue)>0:
        u=queue.popleft()
        v=u.next
        while v!=None:
            if dist[v.index]==-1:
                dist[v.index]=dist[u.index]+1
                queue.append(G[v.index])
                pai[v.index]=u.index
                if dist[v.index]>distMax:
                    distMax=dist[v.index]
                    vmax=G[v.index]
            v=v.next
    dist2=[-1]*n
    pai2=[-1]*n
    queue2=deque()
    queue2.append(vmax)
    dist2[vmax.index]=0
    umax=s
    diametro=0
    while len(queue2)>0:
        u=queue2.popleft()
        v=u.next
        while v!=None:
            if dist2[v.index]==-1:
                dist2[v.index]=dist2[u.index]+1
                queue2.append(G[v.index])
                pai2[v.index]=u.index
                if dist2[v.index]>diametro:
                    diametro=dist2[v.index]
                    umax=G[v.index]
            v=v.next
    return acharCaminho(vmax,umax,pai2)

def acharCaminho(s,u,pai):
    #Retorna string com caminho de s para u
    #Percorremos os pais de u até chegar a s
    atual=u.index
    saida=[]
    while atual!=s.index:
        saida.append(atual)
        atual=pai[atual]
    saida.append(s.index)
    return saida[::-1] #Retorna o oposto

def DiamAux(G,s):
    caminho=Diametro(G,s)
    saida=" -> ".join(map(str,caminho))
    print(f"Diametro de tamanho {len(caminho)-1}")
    print(saida)
V = list(range(10))
E = [[0, 1], [0, 2], [1, 3], [1, 4], [4, 5], [5, 6], [2, 7], [7, 8], [8, 9]]
G=grafoBuilder(V,E)
DiamAux(G,G[0])