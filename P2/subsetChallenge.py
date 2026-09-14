def subconjuntos(A,B,n,i,solucoes):
    #Bota todos os subconjuntos no array solucoes
    if i==n:
        solucoes.append(A.copy())
        return 
    A.append(B[i]) #levar o elemento i
    subconjuntos(A,B,n,i+1,solucoes)
    A.pop()
    subconjuntos(A,B,n,i+1,solucoes) #nao levar 

def binarySearchFirst(arr, targetVal):
    #Acha primeira vez que targetVal aparece no array
    left = 0
    right = len(arr) - 1
    resultado = -1

    while left <= right: #só sai quando isso acontece, por isso que é primeira ocorrencia 
        mid = (left + right) // 2

        if len(arr[mid]) == targetVal:
            resultado = mid
            right = mid - 1
        elif len(arr[mid]) < targetVal:
            left = mid + 1
        else:
            right = mid - 1

    return resultado

def subset_sum(C):
    total=sum(C)//2
    n=len(C)
    if len(C)%2!=0 or sum(C)%2!=0:
        return -1
    mid=n//2
    PRIMEIRA_METADE=C[:mid]
    X=[]
    solucoes=[]
    #Pego todos os subconjuntos da primeira metade, 2^n/2, boto em X
    subconjuntos(X,PRIMEIRA_METADE,len(PRIMEIRA_METADE),0,solucoes)
    Y=[]
    SEGUNDA_METADE=C[mid:]
    solucoes2=[]
    #Pego todos os subconjuntos da segunda metade, 2^n/2, boto em Y
    subconjuntos(Y,SEGUNDA_METADE,len(SEGUNDA_METADE),0,solucoes2)
    solucoes2.sort(key=len)
    #ORDENO Y POR TAMANHO
    for i in solucoes:
        #Para cada subconjunto de X, procuro um subconjunto de Y com tamanho para que, juntos, sejam n//2
        somaX=sum(i)
        if somaX>total: #paro aqui se a soma de X já ultrapassar o alvo
            continue
        target=mid-len(i)
        indexo=binarySearchFirst(solucoes2,target) 
        if indexo == -1:
            continue

        while indexo < len(solucoes2) and len(solucoes2[indexo]) == target:
            #Itero sobre todos os subconjuntos com comprimento igual o desejado
            somaY = sum(solucoes2[indexo])
            #calculo soma parcial
            if somaX + somaY == total: #se as somas dao total(o meu alvo) é uma solução
                solucaoA = i + solucoes2[indexo]
                print("Grupo A:" + " ".join(str(j) for j in solucaoA))
                grupoB = C.copy()
                for elemento in solucaoA:
                    grupoB.remove(elemento)
                print("Grupo B:" + " ".join(str(j) for j in grupoB))
                print("")
            indexo += 1

testes = [
    [1, 3, 2, 2],
    [1, 2, 3, 4],
    [1, 2, 3, 4, 5, 5],
    [1, 2, 4, 6],
    [1, 2, 3],
    [5, 5, 5, 5],
    [-3, -1, 2, 4],
    [0, 0, 1, 1],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 10, 11]
]

for C in testes:
    print("\nC =", C)
    print("-" * 30)
    resultado = subset_sum(C)
    if resultado == -1:
        print("Sem solução")