def possivel(I,v,i,A):
    for j in range(i): #checa todos os anteriores a i
        if I[v][A[j]] or I[A[j]][v]:
            return False #se qualquer um der V, não posso incluir esse cara
    return True
def comite(I,n,k,i,ini,A):
    if i==k:
        print(" ".join(str(j) for j in A))
        return
    achou=False
    for v in range(ini,n-k+i+1): #poda para combinação de n tomada k a k n-(k-i) +1 para incluir o último
        if possivel(I,v,i,A): #checa se posso adicionar esse ao comitê
            A[i]=v
            comite(I,n,k,i+1,v+1,A)
            achou=True
    #consigo podar mais, comparando candidatos possíveis com k-i? 
    if not achou:
        return

def comiteAux(I,n,k):
    A=[0]*k
    return comite(I,n,k,0,0,A)
I=[[False, True,False, False,True,False],
   [True, False, True, False,False, True],
   [False, True, False, True,False, False],
   [False, False, True, False,False, False],
    [False, False, True, False,False, False],
    [False, False, True, False,False, False]]

k=2
n=6
comiteAux(I,n,k)