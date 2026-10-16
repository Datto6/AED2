import heapq
def mergeList(A):
    Q=[]
    n=len(A)
    ordem=[]
    total=0
    for i in range(n):
        heapq.heappush(Q,A[i])
    for i in range(n-1):
        x=heapq.heappop(Q)
        y=heapq.heappop(Q)
        z=x+y
        heapq.heappush(Q,z)
        ordem.append(f"{x} + {y}")
        total+=z
    return " -> ".join(ordem)+f" custo total: {total}"

A=[5,9,12,13,16,45]
print(mergeList(A))
