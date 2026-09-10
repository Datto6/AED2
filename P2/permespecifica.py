def possivel(P, usado, n, i):
    for pos in range(i, n): #vamos perguntar para todo i até n 
        encontrou = False

        for j in range(n):
            if not usado[j] and (j+1 not in P[pos]): 
                encontrou = True #achamos um possível elemento que cabe dentro de i
                break

        if not encontrou: #não achamos um possível elemento para i, retornamos falso
            return False

    return True #passamos por todos i até n e nenhum foi falso, logo retornar true

def permEsp(P,A,usado,n,i):
    if i==n:
        print("".join(str(j) for j in A))
        return
    for j in range(n):
        if not usado[j] and (j+1 not in P[i]):
            usado[j]=True
            A[i]=j+1
            # Strong pruning
            if possivel(P, usado, n, i+1):
                permEsp(P,A,usado,n,i+1)
            usado[j]=False


def permEspAux(P):
    n=len(P)
    usado=[False]*n
    A=[0]*n
    return permEsp(P,A,usado,n,0)


P=[[1,3],[2],[3],[4],[5,4,2]]
permEspAux(P)