def Permutacoes(a, usado, n, i, sol,alice,bob,total):
    if total%2!=0:
        return -1
    if i >= n and alice==bob:
        return sol
    else:
        for v in range(n):
            if not usado[v]:
                usado[v] = True
                sol[i] = a[v] #a[v] é valor de sacola
                alice_added = True
                if alice <= bob: #testa se alice pega ou nao
                    alice += a[v]
                else:
                    bob += a[v]
                    alice_added = False
                if (alice > total//2 or bob > total//2) and alice != bob: #poda
                    usado[v] = False
                    # desfaz
                    if alice_added:
                        alice -= a[v]
                    else:
                        bob -= a[v]
                    continue
                resultado = Permutacoes(a, usado, n, i+1, sol,alice, bob, total) # faz para proximo
                if resultado != -1:
                    return resultado
                # desfaz quem pegou caramelo e escolha 
                usado[v] = False
                if alice_added:
                    alice -= a[v]
                else:
                    bob -= a[v]

    return -1

tamanho=int(input())
array=input().split()
for i in range(tamanho):
    array[i]=int(array[i])
usado = [False] * tamanho
sol = [0] * tamanho
coisa= Permutacoes(array, usado, len(array), 0, sol,0,0,sum(array))
if coisa!=-1:
    for i in range(tamanho):
        coisa[i]=str(coisa[i])
    print(" ".join(coisa))
else:
    print(-1)