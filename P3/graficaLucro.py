import heapq
def greedyLucro(A):
    A.sort(key=lambda x: x[1],reverse=True)
    t=A[0][1]
    heap=[]
    j=0
    saida=[]
    lucro=0
    n=len(A)
    for i in range(t,0,-1):
        while j<n and A[j][1]>=i:
            heapq.heappush(heap,-A[j][0])
            j+=1
        elemento=-heapq.heappop(heap)
        saida.append(elemento)
        lucro+=elemento
    saida=saida[::-1]
    return (saida,lucro)

A=[(20, 2), (15, 2), (10, 1), (5, 3),(1, 3)]
print(greedyLucro(A))