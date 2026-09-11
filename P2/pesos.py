def peso_subc(A,n,i,P,t):
    saida=False
    if i==n:
        if t==0:
            print("Grupo A: "+ " ".join(str(j) for j in A) )
            print("Grupo B: "+ " ".join(str(j) for j in P if j not in A))
        return t==0
    if P[i]<=t: #checo se posso levar ele, essa é a poda
        A.append(P[i])
        saida=peso_subc(A,n,i+1,P,t-P[i]) #levo
        A.pop() #retiro
    if peso_subc(A,n,i+1,P,t): #não levo
        return True
    return saida

def pesoaux(P):
    total=sum(P)
    n=len(P)
    A=[]
    if total%2==0:
        return peso_subc(A,n,0,P,total//2)
P = [2, 3, 7, 8]
pesoaux(P)

