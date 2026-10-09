from collections import deque
class Vertice:
    def __init__(self,index):
        self.index=index
        self.next=None
# 3. Insert after a specific node

def insert_after(prev_node, data):
    if not prev_node:
        print("The given previous node must exist.")
        return
    
    new_node = Vertice(data)
    new_node.next = prev_node.next  # Point new node to the next node
    prev_node.next = new_node       # Point previous node to the new node

def procura_vizinho(v,alvo):
    procurador=v.next
    while procurador!=None:
        if procurador.index==alvo.index:
            return True
        procurador=procurador.next

def CaminhosUnicos(G,E):
    resultado = set() #evita repeticoes
    for u,v in E:
        vizinho=G[u].next
        while vizinho!=None:
            if procura_vizinho(G[v],vizinho):
                triangulo = tuple(sorted([u, v, vizinho.index]))
                resultado.add(triangulo) #evita repeticoes
            vizinho=vizinho.next
    return resultado

def grafoBuilder(V,E):
    n=len(V)
    G=[None]*n
    for i in range(n):
        G[i]=Vertice(i)
    for i in E:
        elem_A=i[1]
        elem_B=i[0]
        insert_after(G[elem_A],elem_B)
        insert_after(G[elem_B],elem_A)
    return G

V=[0,1,2,3,4,5,6,7,8]
E=[[0, 1], [0, 2], [1, 2], [1, 3], [1, 4], [2, 4],[2,5],[3,4],[4,6],[5,6],[7,8]]
G=grafoBuilder(V,E)
print(CaminhosUnicos(G,E))