import math
def binarySearch(arr,x,definitivo):
    ini=0
    fim=len(arr)-1
    while(ini<=fim):
        meio=(ini+fim)//2
        if arr[meio]==x and arr[meio]<=definitivo:
            return True
        elif arr[meio]>x:
            fim=meio-1
        else:
            ini=meio+1
    return False
def calculaprimo(ini,fim):
    primos=[]
    counter=ini
    if counter==1:
        counter=2
    for i in range(ini,fim+1):
        if isPrimo(counter):
            primos.append(counter)
        counter+=1
    return primos

def isPrimo(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False

    return True

def sexyPrimes(ini,fim):
    primos=calculaprimo(ini,fim)
    doubles=0
    triples=0
    quads=0
    quintuples=0
    size=len(primos)
    print(primos)
    for i in range(size):
        if primos[i]>=fim:
            break
        if primos[i]>=ini:
            elem=primos[i]+6
            if(binarySearch(primos,elem,fim)):
                doubles+=1
                elem+=6
                if (binarySearch(primos,elem,fim)):
                    triples+=1
                    elem+=6
                    if (binarySearch(primos,elem,fim)):
                        quads+=1
                        elem+=6
                        if(binarySearch(primos,elem,fim)):
                            quintuples+=1
                            elem+=6
    print(str(doubles)+" "+str(triples)+" "+str(quads)+" "+str(quintuples))

vezes=int(input())
for i in range(vezes):
    numeros=input().split()
    sexyPrimes(int(numeros[0]),int(numeros[1]))