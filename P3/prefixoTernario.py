import heapq
class Node:
    def __init__(self,valor):
        self.valor=valor
        self.right=None
        self.left=None
        self.middle=None
def mergeList(A):
    #Escolhe os 3 menores nós e junta eles, resolvendo o problema com n-2
    #Auxiliar depois mostra o resultado 
    #Resultado dá código de prefixo ternário ótimo
    Q=[]
    n=len(A)
    total=0
    if n%2==0:
        A.append(0)
        n+=1
    for i in range(n):
        heapq.heappush(Q,(A[i],Node(A[i])))
    for i in range((n-1)//2):
        x=heapq.heappop(Q)
        y=heapq.heappop(Q)
        u=heapq.heappop(Q)
        valorZ=x[1].valor+y[1].valor+u[1].valor
        nodeZ=Node(valorZ)
        nodeZ.right=x[1]
        nodeZ.left=y[1]
        nodeZ.middle=u[1]
        z=(valorZ,nodeZ)
        heapq.heappush(Q,z)
        total+=valorZ
    print(f" custo total: {total}")
    return heapq.heappop(Q)

def printTree(node, nivel=0, lado="Root"):
    if node is None:
        return

    printTree(node.right, nivel + 1, "Right")
    printTree(node.middle, nivel + 1, "Middle")
    printTree(node.left, nivel + 1, "Left")

    print("    " * nivel + f"{lado}: {node.valor}")

A=[5,9,12,13,16,45]

raiz = mergeList(A)
printTree(raiz[1])
