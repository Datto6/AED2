from collections import deque
import heapq
vezes=int(input())
for i in range(vezes):
    tamanho=int(input())
    numeros=input().split()
    heap=[]
    lista={}
    min_index=0
    for j in range(tamanho):
        atual=int(numeros[j])
        while(len(heap)>0) and (heap[0][0]<=atual):
            elemento=heapq.heappop(heap)
            lista[elemento[1]]=atual
        heapq.heappush(heap,(atual,j)) #(elemento,indexo)
    saida=""
    for j in range(tamanho):
        saida+=""
        if j in lista.keys():
            saida+=" "+str(lista[j])
        else:
            saida+=" -1"
    saida=saida.strip()
    print(saida)    
