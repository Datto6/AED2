def criancasMinDoce(r):
    n=len(r)
    doces=[1]*n
    for i in range(n-1): #Passa de esquerda a direita
        if r[i]<r[i+1]: #É menor que da direita
            doces[i+1]=doces[i]+1
    for i in range(n-1,0,-1): #Passa da direita pra esquerda
        if r[i]<r[i-1]: #É menor que da esquerda
            doces[i-1]=max(doces[i-1],doces[i]+1)
    return doces

r=[1,0,2]
print(criancasMinDoce(r))