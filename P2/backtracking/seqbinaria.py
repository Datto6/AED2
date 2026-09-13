def seq(A,n,k,i):
    if i==n: 
        if k==0:
            print("".join(str(j) for j in A))
        return
    if i==0 or A[i-1]!=1:
        A[i]=1
        seq(A,n,k-1,i+1)
    A[i]=0
    seq(A,n,k,i+1)
def seqAux(n,k):
    A=[0]*n
    return seq(A,n,k,0)
seqAux(5,2)