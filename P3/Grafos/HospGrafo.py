from collections import deque
from basico import grafoBuilder, Vertice

def Hospitais(G,S):
    n=len(G)
    dist=[-1]*n
    queue=deque()
    for i in S:
        queue.append(G[i])
        dist[i]=0
    while len(queue)>0:
        u=queue.popleft()
        v=u.next
        while v!=None:
            if dist[v.index]==-1:
                dist[v.index]=dist[u.index]+1
                queue.append(G[v.index])
            v=v.next
    return dist

V=[0,1,2,3,4,5,6]
E=[[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
S=[0,5]
G=grafoBuilder(V,E)
print(Hospitais(G,S))