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