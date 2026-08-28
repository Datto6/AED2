def SomaSub(M,i,t,s):
    if t==0:
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

def pegaSol(M, i, t, s):
    A = []
    B = []
    while i > 0:
        if t == 0:
            # Everything remaining goes to B
            B.append(s[i-1])
            i -= 1
            continue

        if SomaSub(M, i-1, t, s) == False:
            A.append(s[i-1])
            t -= s[i-1]
        else:
            B.append(s[i-1])

        i -= 1
    return [A, B]

def caramelos(entrada):
    i=0
    j=0
    alice=0
    bob=0
    total=sum(entrada)//2
    if sum(entrada)%2!=0:
        print(-1)
        return
    M=[[-1 for _ in range(total+1)] for _ in range(len(entrada)+1)]
    SomaSub(M,len(entrada),total,entrada)
    grupos=pegaSol(M,len(entrada),total,entrada)
    if len(grupos[0])==0 or len(grupos[1])==0:
        print(-1)
        return
    saida=[]
    while(i<len(grupos[0]) or j<len(grupos[1])):
        if alice<=bob:
            alice+=grupos[0][i]
            saida.append(grupos[0][i])
            i+=1
        else:
            bob+=grupos[1][j]
            saida.append(grupos[1][j])
            j+=1
    print(" ".join(map(str, saida)))
fodase=int(input())
array_entrada=input().split()
for i in range(fodase):
    array_entrada[i]=int(array_entrada[i])
caramelos(array_entrada)