from collections import deque
from basico import grafoBuilder, Vertice
def componentes(G):
    n=len(G)
    comp=[0]*n
    c=0
    for i in range(len(G)):
        if comp[i]==0:
            c=c+1
            comp[i]=c
            queue=deque()
            queue.append(G[i])
            while len(queue)!=0:
                u=queue.popleft()
                v=u.next
                while v!=None:
                    if comp[v.index]==0:
                        comp[v.index]=c
                        queue.append(v)
                    v=v.next
    return (c,comp)
#Contar quantos de cada componente conexo e juntar 

def desconexos(saida):
    total=saida[0]
    hist={}
    componentes=saida[1]
    atual=componentes[0]
    hist[atual]=0
    for i in range(len(componentes)): #Contar quantos de cada componente conexo tem 
        if atual!=componentes[i]:
            hist[atual]=0
        else:
            hist[atual]+=1
    pares_desconexos=0
    for componente,contagem in hist.values():
        pares_desconexos+=contagem*(total-contagem)
    return (pares_desconexos,len(hist.keys()))