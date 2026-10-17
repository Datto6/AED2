from collections import deque
from basico import grafoBuilder, Vertice

def bipartido(G):
    n=len(G)
    dist=[-1]*n
    conflitos=[]
    pai=[-1]*n
    for s in G:
        if dist[s.index]==-1:
            #BFS a partir de todos os vertices, acha todos os componentes conexos
            dist[s.index]=0
            queue=deque()
            queue.append(s)
            while len(queue)!=0:
                u=queue.popleft()
                v=u.next
                while v!=None:
                    if dist[v.index]==-1:
                        dist[v.index]=dist[u.index]+1
                        pai[v.index]=u.index
                        queue.append(G[v.index])
                    elif dist[v.index]%2==dist[u.index]%2 and u.index <v.index: 
                        #Checa se tá na mesma paridade, onde seria mesma cor
                        #Compara indexos para nao pegar ciclo repetido
                        conflitos.append((s,v,u))
                    v=v.next
    return [conflitos,pai]

def bipAux(saida):
    #Printa os ciclos impares achados
    conflitos=saida[0]
    pai=saida[1]
    for i in conflitos:
        print(acharCiclo(i[0],i[1],i[2],pai))


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

def acharCiclo(s, v, u, pai):
    caminhoV = acharCaminho(s, v, pai)
    caminhoU = acharCaminho(s, u, pai)
    i = 0
    while (i < len(caminhoV) and i < len(caminhoU) and caminhoV[i] == caminhoU[i]):
        i += 1
    
    # Último ancestral comum
    ancestral = caminhoV[i - 1]

    # Caminho do ancestral até v
    parteV = caminhoV[i - 1:]

    # Caminho de u até o ancestral
    parteU = caminhoU[i - 1:][::-1]

    # Junta os caminhos usando a aresta conflitante (v, u)
    ciclo = parteV + parteU

    return " -> ".join(map(str, ciclo))

V=[0,1,2,3,4,5,6,7,8]
E=[[0,1],[1,2],[2,3],[3,4],[0,4],[3,5],[6,7],[7,8],[8,6]]
G=grafoBuilder(V,E)
saida=bipartido(G)
bipAux(saida)

