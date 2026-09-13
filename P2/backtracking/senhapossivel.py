def possivel(A,usado,n,i,j):
    possivel=False
    if i==0:
        possivel=True
    elif i>0:
        anterior=abs(A[i-1]-j)!=1
        possivel=anterior
    possiveis=[]
    for k in range(len(usado)):
        if not usado[k]:
            possiveis.append(k)
    contador=0
    for k in range(len(possiveis)):
        for l in range(k,len(possiveis)):
            if abs(possiveis[l]-possiveis[k])!=1:
                contador+=1
            if contador==n-i-2: #precisa ter no minimo restantes -1 adjacencias válidas
                break
        if contador>=n-i-2:
            break
    return contador>=n-i-2 and possivel

def senhaPos(A,usado,n,i):
    if i==n:
        print("".join(str(j) for j in A))
        return
    for j in range(n):
        if not usado[j]:
            usado[j]=True
            A[i]=j
            if possivel(A,usado, n, i,j):
                senhaPos(A,usado,n,i+1)
            usado[j]=False


def senhaPosAux(n):
    usado=[False]*n
    A=[0]*n
    return senhaPos(A,usado,n,0)

senhaPosAux(6)