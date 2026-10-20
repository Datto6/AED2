def servidorMinCusto(A):
    A.sort(key=lambda x: x[0]/x[1])
    return A
def servidorAux(A):
    #Ordena servidor de acordo com t/w ordem de prioridade
    #Fazer os processos nessa ordem garante custo agregado t*w mínimo
    t=0
    custo=0
    saida=[]
    for i in range(len(A)):
        t+=A[i][0]
        custo+=t*A[i][1]
        saida.append(f"{A[i][1]}*{t}")
    print(custo)
    print(" + ".join(saida))

A=[[3,1],[1,2],[2,2]]
A=servidorMinCusto(A)
servidorAux(A)