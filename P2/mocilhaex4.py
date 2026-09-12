def mochilaMemo(M,i,w,p,v):
    if M[i][w]!=None:
        return M[i][w]
    r=tuple(0 for _ in range(len(p))) #não levar nenhum, caso base 
    qntd=0
    # print(i)
    for j in range(i): #iteramos sobre todos os itens possiveis, não alteramos i porque sempre podemos levar qualquer um
        if p[j]<=w:
            r1=mochilaMemo(M,i,w-p[j],p,v)
            r1=r1[:j]+(r1[j]+1,)+r1[j+1:] #somo um pois levei o valor j, isso é só slice de tupla aqui p compor a nova tupla
            qntd1=0
            # print(r1)
            for index in range(len(r1)): #procura o máximo de valor
                qntd1+=r1[index]*v[index]
            if qntd1>qntd: #achamos um novo máximo
                qntd=qntd1
                r=r1
    M[i][w]=r
    return r

def mochilaAux(w,p,v): #v tabela de valores, p tabela de pesos
    n=len(v)
    M=[[None for _ in range(w+1)] for _ in range(n+1)]
    valor=mochilaMemo(M,n,w,p,v)
    # for j in M:
    #     print(j)
    print(valor)

w = 5
p = [10, 2]
v = [100, 3]
mochilaAux(w,p,v)