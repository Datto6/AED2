def greedyInterval(A,L):
    # Ordenar por intervalo de início de forma crescente
    # Pegar o maior final dos que começam com c, começando com 0 
    # O c[i+1] vira o fmax de c[i]
    # Caso c ultrapassar L, conseguimos cobrir [0,L]
    A.sort(key=lambda x: x[0])
    intervalos=[]
    n=len(A)
    i=0
    c=0
    while c < L:
        fmax = c
        imax = -1
        while i < n and A[i][0] <= c:
            if A[i][1] > fmax:
                fmax = A[i][1]
                imax = i
            i += 1
        if imax == -1:
            return -1
        intervalos.append(A[imax])
        c = fmax
    return intervalos

A= [[0, 3], [1, 5], [2, 6], [3, 4], [5, 10], [6, 9]]
print(greedyInterval(A,10))