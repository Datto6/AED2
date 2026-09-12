def mochilaMemo(M,i,w,p,v,sum):
    if i==0:
        return 0
    if w<=sum and M[i][w]!=-1:
        return M[i][w]
    r=mochilaMemo(M,i-1,w,p,v,sum)
    # print(i)
    if p[i-1]<=w:
        r=max(r,v[i-1]+mochilaMemo(M,i-1,w-p[i-1],p,v,sum))
    if w<=sum:
        M[i][w]=r
    return r

def mochilaAux(w,p,v): #v tabela de valores, p tabela de pesos
    somatorio=sum(v)
    n=len(v)
    M=[[-1 for _ in range(somatorio+1)] for _ in range(n+1)]
    valor=mochilaMemo(M,n,w,p,v,somatorio)
    # for j in M:
    #     print(j)
    print(valor)

w = 200
p = [3,4,7,8,9]
v = [10,20,30,40,50]
mochilaAux(w,p,v)