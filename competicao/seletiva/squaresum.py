import math
vezes=int(input())
for i in range(vezes):
    numeros=input().split()
    quadrado=True
    achados=[]
    tamanho=int(numeros[0])
    for j in range(1,tamanho):
        num1=int(numeros[j])
        num2=int(numeros[j+1])
        quadrado=num1+num2
        if num1<=0 or num2<=0:
            print("N")
            quadrado=False
            break
        raiz=math.sqrt(quadrado)
        if raiz!=math.floor(raiz):
            print("N")
            quadrado=False
            break
        achados.append(num1)
    achados.append(int(numeros[-1]))
    achados.sort()
    if quadrado and len(achados)!=tamanho:
        print("N")
        print(achados)
        quadrado=False
    if quadrado:
        for k in range(int(numeros[0])):
            if achados[k]!=k+1:
                print("N")
                quadrado=False
                break
    if quadrado:
        print("Y")