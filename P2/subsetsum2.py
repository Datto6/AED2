def SomaSub(M,i,t,s):
#M[i][t] já é o problema resolvido
    if t==0: #caso trivial, soma 0 podemos assumir verdade
        return True
    if i==0: #caso base
        return False
    if M[i][t]!=-1:
        return M[i][t]
    r=SomaSub(M,i-1,t,s) #nao levar s[i]
    if r==False and s[i-1]<=t:
        r=SomaSub(M,i-1,t-s[i-1],s) #levar s[i]
    M[i][t]=r
    return r

#isso é complexidade i*t, ou seja, n*sigma, onde sigma é metade da soma de A
def pegaSols(M, i, t, s, A, solucoes): #isso percorre por exatamente todas as soluções, isso muda a complexidade?
    if t == 0:
        solucoes.append(A.copy())
        return

    if i == 0:
        return
    
    # Take s[i-1]
    if s[i-1] <= t and SomaSub(M, i-1, t-s[i-1], s):
        A.append(s[i-1])

        pegaSols(M, i-1, t-s[i-1], s, A, solucoes)

        A.pop()

    # Don't take s[i-1]
    if SomaSub(M, i-1, t, s):
        pegaSols(M, i-1, t, s, A, solucoes)



def caramelos(entrada):
    total=sum(entrada)//2
    if sum(entrada)%2!=0:
        print(-1)
        return
    M=[[-1 for _ in range(total+1)] for _ in range(len(entrada)+1)]
    SomaSub(M,len(entrada),total,entrada)
    solucoes=[]
    A=[]
    pegaSols(M,len(entrada),total,entrada,A,solucoes)
    achou=False
    for i in solucoes:
        if len(solucoes)==len(entrada)//2:
            print("Grupo B: " +" ".join(map(str, i)))
            print("Grupo C: " +" ".join(str(j) for j in entrada if j not in i ))
            print("")
            achou=True
    if not achou:
        print(-1)

entrada=[2, 3, 5, 7]
caramelos(entrada)