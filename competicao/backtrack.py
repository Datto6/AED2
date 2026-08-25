
def back(M,N,i,j,poti,potj,numi,numj):
    sol1=-1
    sol2=-1
    sol3=-1
    sol4=-1
    sol5=-1
    sol6=-1
    if i<0 and j<0:
        if numj!=0 and (numi%numj==0): #checar se N divide M
            return numi
        else:
            return -1
    if i>=0 and  M[i]=="*":
        numi2=numi+poti
        next_poti=poti*2
        sol1=back(M,N,i-1,j,next_poti,potj,numi,numj) #testar para * ==0
        sol2=back(M,N,i-1,j,next_poti,potj,numi2,numj) #testar para * == 1
    if j>=0 and N[j]=="*":
        numj2=numj+potj
        next_potj=potj*2
        sol3=back(M,N,i,j-1,poti,next_potj,numi,numj)  #testar para * ==0
        sol4=back(M,N,i,j-1,poti,next_potj,numi,numj2) #testar para * == 1
    if i>=0 and M[i]!="*": #nao preciso abrir nova recursao, não é *
        da_vez=int(M[i])
        numi2=numi+da_vez*poti
        next_poti=poti*2
        sol5=back(M,N,i-1,j,next_poti,potj,numi2,numj)
    if j>=0 and N[j]!="*": #nao preciso abrir nova recursao, não é * 
        da_vez_n=int(N[j])
        numj2=numj+potj*da_vez_n
        next_potj=potj*2
        sol6=back(M,N,i,j-1,poti,next_potj,numi,numj2)
    lista=[sol1,sol2,sol3,sol4,sol5,sol6] #juntar todas as solucoes das chamadas recursivas 
    for k in lista: #retornar a unica valida 
        if k!=-1:
            return k
    return -1 #retorno default invalido se nada rodou


def binario(num):
    if num == 0:
        return "0"
    if num == -1:
        return "-1"
    saida = ""
    while num > 0:
        resto = num % 2
        num //= 2
        saida = str(resto) + saida
    return saida

M=input()
N=input()
saida=back(M,N,len(M)-1,len(N)-1,1,1,0,0)
print(binario(saida).zfill(len(M)))
