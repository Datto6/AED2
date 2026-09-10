def permEsp(P,A,usado,n,i):
    if i==n:
        print("".join(str(j) for j in A))
        return
    for j in range(n):
        if not usado[j] and (j+1 not in P[i]):
            usado[j]=True
            A[i]=j+1
            permEsp(P,A,usado,n,i+1)
            usado[j]=False


def permEspAux(P):
    n=len(P)
    usado=[False]*n
    A=[0]*n
    return permEsp(P,A,usado,n,0)


P=[[1,3],[2],[3]]
permEspAux(P)