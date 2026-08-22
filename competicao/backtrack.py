
def back(M,N,i,j,poti,potj,numi,numj):
    sol1=-1
    sol2=-1
    sol3=-1
    sol4=-1
    sol5=-1
    sol6=-1
    if i<0 and j<0:
        if (numi%numj==0): #checar se N divide M
            return numi
        else:
            return -1
    elif i>=0 and  M[i]=="*":
        i=i-1
        numi2=numi+poti
        poti*=2
        sol1=back(M,N,i,j,poti,potj,numi,numj) #testar para * ==0
        sol2=back(M,N,i,j,poti,potj,numi2,numj) #testar para * == 1
    elif j>=0 and N[j]=="*":
        j=j-1
        numj2=numj+potj
        potj*=2
        sol3=back(M,N,i,j,poti,potj,numi,numj)  #testar para * ==0
        sol4=back(M,N,i,j,poti,potj,numi,numj2) #testar para * == 1
    elif i>=0 and M[i]!="*": #nao preciso abrir nova recursao, não é *
        da_vez=int(M[i])
        i=i-1
        numi2=numi+da_vez*poti
        poti*=2
        sol5=back(M,N,i,j,poti,potj,numi2,numj)
    elif j>=0 and N[j]!="*": #nao preciso abrir nova recursao, não é * 
        da_vez_n=int(N[j])
        j=j-1
        numj2=numj+potj*da_vez_n
        potj*=2
        sol6=back(M,N,i,j,poti,potj,numi,numj2)
    lista=[sol1,sol2,sol3,sol4,sol5,sol6] #juntar todas as solucoes das chamadas recursivas 
    for i in lista: #retornar a unica valida 
        if i!=-1:
            return i
    return -1 #retorno default invalido se nada rodou


def binario(num):
    saida=""
    while(num>0):
        resto=num%2
        num=num//2
        saida=str(resto)+saida
    return saida
M=input()
N=input()
saida=back(M,N,len(M)-1,len(N)-1,1,1,0,0)
print(binario(saida))
