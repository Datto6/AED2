numeros=int(input())
numeros_arr=input().split()
for i in range(len(numeros_arr)):
    numeros_arr[i]=int(numeros_arr[i])
numeros_arr.sort(reverse=True)
for i in range(len(numeros_arr)):
    numeros_arr[i]=bin(numeros_arr[i])[2:]
    numeros_arr[i]=list(numeros_arr[i])

for i in range(len(numeros_arr[0])):
    count1=0
    potencia=len(numeros_arr[0])-i-1
    print("Potencia" +str(potencia))
    for j in range(numeros):
        indice=len(numeros_arr[j])-potencia-1
        if indice>=0 and numeros_arr[j][indice]=='1':
            count1+=1
            numeros_arr[j][indice]='0'
            print("Cheguei aqui")
    print(count1)
    for k in range(count1):
        indice=len(numeros_arr[k])-potencia-1
        if indice>=0:
            numeros_arr[k][indice]='1'
saida=["".join(numero) for numero in numeros_arr]
saida = [str(int(numero, 2)) for numero in saida]

print(" ".join(saida))