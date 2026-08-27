def back(M, N, i, j, poti, potj, numi, numj):
    if i < 0 and j < 0:
        if numj != 0 and numi % numj == 0:
            return numi
        return -1
    # Both are *
    if i >= 0 and j >= 0 and M[i] == "*" and N[j] == "*":
        # M=0, N=0
        sol = back(M, N, i-1, j-1,poti*2, potj*2,numi, numj)
        if sol != -1:
            return sol
        # M=1, N=0
        sol = back(M, N, i-1, j-1,poti*2, potj*2,numi+poti, numj)
        if sol != -1:
            return sol
        # M=0, N=1
        sol = back(M, N, i-1, j-1,poti*2, potj*2,numi, numj+potj)
        if sol != -1:
            return sol
        # M=1, N=1
        return back(M, N, i-1, j-1,poti*2, potj*2,numi+poti, numj+potj)

    # Only M is *
    if i >= 0 and M[i] == "*":
        sol = back(M, N, i-1, j,poti*2, potj,numi, numj)
        if sol != -1:
            return sol
        return back(M, N, i-1, j,poti*2, potj,numi+poti, numj)

    # Only N is *
    if j >= 0 and N[j] == "*":
        sol = back(M, N, i, j-1,poti, potj*2,numi, numj)
        if sol != -1:
            return sol
        return back(M, N, i, j-1,poti, potj*2,numi, numj+potj)

    # Neither is *
    if i >= 0 and j >= 0:
        return back(M, N,i-1, j-1,poti*2, potj*2,numi + int(M[i])*poti,numj + int(N[j])*potj)
    # Only M remains
    if i >= 0:
        return back(M, N,i-1, j,poti*2, potj,numi + int(M[i])*poti,numj)
    # Only N remains
    if j >= 0:
        return back(M, N,i, j-1,poti, potj*2,numi,numj + int(N[j])*potj)

    return -1

M=input()
N=input()
saida=back(M,N,len(M)-1,len(N)-1,1,1,0,0)
print(bin(saida)[2:].zfill(len(M)))
