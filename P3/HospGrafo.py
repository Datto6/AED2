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

V=[0,1,2,3,4,5,6]
E=[[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
S=[0,5]
G=grafoBuilder(V,E)
print(Hospitais(G,S))