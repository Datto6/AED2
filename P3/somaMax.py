def greedyMax(A,B):
    n=len(A)
    A_order=[]
    for i in range(n):
        A_order.append((A[i],i)) 
    B_order=[]
    for i in range(n):
        B_order.append((B[i],i))
    A_order.sort()
    B_order.sort()
    saida=[0]*n
    for i in range(n):
        index_saida=A_order[i][1]
        saida[index_saida]=(B_order[i][1])
    return saida
def greedyMin(A,B):
    n=len(A)
    A_order=[]
    for i in range(n):
        A_order.append((A[i],i)) 
    B_order=[]
    for i in range(n):
        B_order.append((B[i],i))
    A_order.sort()
    B_order.sort()
    saida=[0]*n
    for i in range(n):
        index_saida=A_order[i][1]
        saida[index_saida]=(B_order[n-i-1][1])
    return saida

def valor(A, B, pi):
    return sum(A[i] * B[pi[i]] for i in range(len(A)))