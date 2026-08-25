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


a = [1, 2, 2, 3]
usado = [False] * len(a)
sol = [0] * len(a)
coisa= Permutacoes(a, usado, len(a), 0, sol,0,0,sum(a))
print(coisa)