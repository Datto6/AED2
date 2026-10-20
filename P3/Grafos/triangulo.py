from collections import deque
from basico import Vertice, grafoBuilder
def procura_vizinho(v,alvo):
    procurador=v.next
    while procurador!=None:
        if procurador.index==alvo.index:
            return True
        procurador=procurador.next

def triangulo(G,E):
    #Para toda aresta, checar vizinhos de u e v, para ver se tem um em comum
    #Se tiver, é triangulo(ciclo de comprimento 3)
    resultado = set() #evita repeticoes
    for u,v in E:
        vizinho=G[u].next
        while vizinho!=None:
            if procura_vizinho(G[v],vizinho):
                triangulo = tuple(sorted([u, v, vizinho.index]))
                resultado.add(triangulo) #evita repeticoes
            vizinho=vizinho.next
    return resultado

V=[0,1,2,3,4,5,6,7,8]
E=[[0, 1], [0, 2], [1, 2], [1, 3], [1, 4], [2, 4],[2,5],[3,4],[4,6],[5,6],[7,8]]
G=grafoBuilder(V,E)
print(triangulo(G,E))