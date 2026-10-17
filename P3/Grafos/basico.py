class Vertice:
    def __init__(self,index):
        self.index=index
        self.next=None

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
# 3. Insert after a specific node
def insert_after(prev_node, data):
    if not prev_node:
        print("The given previous node must exist.")
        return
    
    new_node = Vertice(data)
    new_node.next = prev_node.next  # Point new node to the next node
    prev_node.next = new_node       # Point previous node to the new node