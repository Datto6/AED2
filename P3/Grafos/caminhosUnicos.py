from collections import deque
from basico import Vertice, grafoBuilder
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
