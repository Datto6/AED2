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

def CaminhosUnicos(G,s):
    n=len(G)
    dist=[-1]*n
    caminhos=[-1]*n
    queue=deque()
    queue.append(s)
    caminhos[s.index]=1
    dist[s.index]=0
    while len(queue)>0:
        u=queue.popleft()
        v=u.next
        while v!=None:
            if dist[v.index]==-1:
                dist[v.index]=dist[u.index]+1
                caminhos[v.index]=caminhos[u.index] #Adiciona possíveis caminhos de u para v agora
                queue.append(G[v.index])
            elif dist[v.index]==dist[u.index]+1: #Isso mantém que é um caminho único
                caminhos[v.index]+=caminhos[u.index]
            v=v.next
    for i in range(len(caminhos)):
        if caminhos[i]==-1:
            caminhos[i]=0
    return caminhos

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
s=G[0]
print(CaminhosUnicos(G,s))

testes = [
    ("Vertice isolado", [0], [], 0, [1]),
    ("Dois vertices", [0, 1], [[0, 1]], 0, [1, 1]),
    ("Grafo linear", [0, 1, 2, 3],
     [[0, 1], [1, 2], [2, 3]], 0, [1, 1, 1, 1]),
    ("Triangulo", [0, 1, 2],
     [[0, 1], [0, 2], [1, 2]], 0, [1, 1, 1]),
    ("Dois caminhos minimos", [0, 1, 2, 3],
     [[0, 1], [0, 2], [1, 3], [2, 3]], 0, [1, 1, 1, 2]),
    ("Componentes desconexas", [0, 1, 2, 3, 4],
     [[0, 1], [1, 2], [3, 4]], 0, [1, 1, 1, 0, 0]),
    ("Tres caminhos minimos", [0, 1, 2, 3, 4, 5],
     [[0, 1], [0, 2], [0, 3], [1, 4],
      [2, 4], [3, 4], [4, 5]], 0, [1, 1, 1, 1, 3, 3]),
    ("Grafo original", list(range(9)),
     [[0, 1], [0, 2], [1, 2], [1, 3], [1, 4],
      [2, 4], [2, 5], [3, 4], [4, 6], [7, 8]],
     0, [1, 1, 1, 1, 2, 1, 2, 0, 0]),
]

for nome, V, E, s, esperado in testes:
    G = grafoBuilder(V, E)
    resultado = CaminhosUnicos(G, G[s])
    status = "OK" if resultado == esperado else "FALHOU"
    print(f"{nome}: {status}")
    if status == "FALHOU":
        print("  Esperado:", esperado)
        print("  Obtido:  ", resultado)
