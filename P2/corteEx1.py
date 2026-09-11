def corteMem(a,b,c,m,M):
    if M[m] is not None: #se já resolvemos
        return M[m]
    if m==0:
        M[m]=[0,0,0]
        return [0,0,0]
    tuplas=[]
    if m>=c:
        levar_c=corteMem(a,b,c,m-c,M)
        if levar_c is not None:
            levar_c = levar_c.copy()
            levar_c[2] += 1
            tuplas.append(levar_c)
    if m>=b:
        levar_b = corteMem(a,b,c,m-b,M)

        if levar_b is not None:
            levar_b = levar_b.copy() #levar mais um B, adicionar 1 
            levar_b[1] += 1
            tuplas.append(levar_b)
    if m >= a:
        levar_a = corteMem(a,b,c,m-a,M)

        if levar_a is not None:
            levar_a = levar_a.copy()
            levar_a[0] += 1
            tuplas.append(levar_a)

    if len(tuplas) == 0: #se nao consegui levar nenhum, não tem nenhuma resposta valida
        M[m] = None
        return None
    saida=tuplas[0]
    for i in tuplas:
        if sum(saida)<sum(i):
            saida=i
    M[m]=saida
    return saida

def corteMemAux(a,b,c,m):
    M = [None]*(m+1)
    corteMem(a,b,c,m,M)
    if M[m] is not None:
        print(sum(M[m]))
    print(M[m])
    print(M)
m=6
a=1
b=3
c=4
corteMemAux(a,b,c,m)