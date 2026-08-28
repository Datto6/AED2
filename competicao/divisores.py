import math as m
def isPrimo(n):
    if n<2:
        return False
    i=2
    while(i<=m.floor(m.sqrt(n))):
        if n%i==0:
            return False
        i+=1
    return True

def proximoPrimo(primos):
    n = primos[-1] + 1

    while not isPrimo(n):
        n += 1

    return n

def achar_m(alvo):
    primos=[]
    for i in range(m.floor(m.sqrt(alvo))+1):
        if isPrimo(i):
            primos.append(i)
    poderes=[]
    for i in primos:
        cont=0
        while i!=0 and alvo%i==0:
            alvo=alvo//i
            poderes.append(i)
    if alvo>1:
        primos.append(alvo)
        poderes.append(alvo)
    poderes.sort(reverse=True)
    resultado=1
    for i in range(len(poderes)):
        if i==len(primos):
            primos.append(proximoPrimo(primos))
            
        resultado*=pow(primos[i],poderes[i]-1)
        if resultado>1e18:
            return -1
    return resultado

entrada=int(input())
print(achar_m(entrada))