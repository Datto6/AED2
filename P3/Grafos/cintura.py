from basico import grafoBuilder, Vertice
from collections import deque
def cintura(G):
    #Calcular a cintura de um grafo
    n=len(G)
    cintura=n+1
    for i in range(n): #Comecar BFS a partir de todos
        s=G[i]
        queue=deque()
        dist=[-1]*n
        pai=[-1]*n
        queue.append(s)
        dist[s.index]=0
        while len(queue)>0:
            u=queue.popleft()
            v=u.next
            while v!=None:
                if dist[v.index]==-1: #Não descobrimos, BFS com preenchimento de distancias normal
                    dist[v.index]=dist[u.index]+1
                    pai[v.index]=u.index
                    queue.append(G[v.index])
                elif pai[u.index]!=v.index: #v já foi descoberto e não é pai de u
                    cintura=min(cintura, dist[v.index]+dist[u.index]+1) #Manter cintura minima
                v=v.next
    if cintura==n+1:
        return -1
    return cintura

def cinturaAux(G):
    retorno=cintura(G)
    if retorno==-1:
        print("Nenum Ciclo encontrado")
        return
    print(f"Cintura de comprimento {retorno}")

V=[0,1,2,3,4,5,6,7]
E=[[0, 1], [1, 2], [2, 3], [0, 3], [4, 5], [5, 6], [6, 7], [4, 7], [0, 4], [1, 5], [2, 6], [3, 7]]
G=grafoBuilder(V,E)
cinturaAux(G)

V=[0,1,2,3,4,5,6,7,8]
E=[[0, 1], [0, 2], [1, 2], [1, 3], [1, 4], [2, 4],[2,5],[3,4],[4,6],[5,6],[7,8]]
G=grafoBuilder(V,E)
cinturaAux(G)

from basico import grafoBuilder, Vertice
from collections import deque
def cintura(G):
    n=len(G)
    cintura=n+1
    for i in range(n): #Comecar BFS a partir de todos
        s=G[i]
        queue=deque()
        dist=[-1]*n
        pai=[-1]*n
        queue.append(s)
        dist[s.index]=0
        while len(queue)>0:
            u=queue.popleft()
            v=u.next
            while v!=None:
                if dist[v.index]==-1: #Não descobrimos, BFS com preenchimento de distancias normal
                    dist[v.index]=dist[u.index]+1
                    pai[v.index]=u.index
                    queue.append(G[v.index])
                elif pai[u.index]!=v.index: #v já foi descoberto e não é pai de u
                    cintura=min(cintura, dist[v.index]+dist[u.index]+1) #Manter cintura minima
                v=v.next
    if cintura==n+1:
        return -1
    return cintura

def cinturaAux(G):
    retorno=cintura(G)
    if retorno==-1:
        print("Nenum Ciclo encontrado")
        return
    print(f"Cintura de comprimento {retorno}")

V=[0,1,2,3,4,5,6,7]
E=[[0, 1], [1, 2], [2, 3], [0, 3], [4, 5], [5, 6], [6, 7], [4, 7], [0, 4], [1, 5], [2, 6], [3, 7]]
G=grafoBuilder(V,E)
cinturaAux(G)

V=[0,1,2,3,4,5,6,7,8]
E=[[0, 1], [0, 2], [1, 2], [1, 3], [1, 4], [2, 4],[2,5],[3,4],[4,6],[5,6],[7,8]]
G=grafoBuilder(V,E)
cinturaAux(G)
def testarCintura():
    casos = [
        # 1. Triângulo: cintura 3
        ([0, 1, 2],
         [[0, 1], [1, 2], [2, 0]],
         3),

        # 2. Quadrado: cintura 4
        ([0, 1, 2, 3],
         [[0, 1], [1, 2], [2, 3], [3, 0]],
         4),

        # 3. Grafo sem ciclos: -1
        ([0, 1, 2, 3],
         [[0, 1], [1, 2], [2, 3]],
         -1),

        # 4. Quadrado com diagonal: cintura 3
        ([0, 1, 2, 3],
         [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2]],
         3),

        # 5. Dois triângulos desconectados: cintura 3
        ([0, 1, 2, 3, 4, 5],
         [[0, 1], [1, 2], [2, 0],
          [3, 4], [4, 5], [5, 3]],
         3),

        # 6. Grafo com ciclo de comprimento 5
        ([0, 1, 2, 3, 4],
         [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]],
         5),

        # 7. Cubo: cintura 4
        (list(range(8)),
         [[0, 1], [1, 2], [2, 3], [0, 3],
          [4, 5], [5, 6], [6, 7], [4, 7],
          [0, 4], [1, 5], [2, 6], [3, 7]],
         4),
    ]

    for i, (V, E, esperado) in enumerate(casos, start=1):
        G = grafoBuilder(V, E)
        obtido = cintura(G)

        status = "OK" if obtido == esperado else "FALHOU"

        print(
            f"Teste {i}: {status} | "
            f"Esperado: {esperado} | Obtido: {obtido}"
        )
testarCintura()