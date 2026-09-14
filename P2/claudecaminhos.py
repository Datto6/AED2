def contar_caminhos(pai):
    """
    pai: lista de tamanho n+1 (1-indexada), onde pai[i] é o pai do nó i
         (i = 1..n) e pai[r] = -1 para a raiz r.
    Retorna uma lista `ans` de tamanho n+1, onde ans[k] é a quantidade
    de caminhos de comprimento k (k = 1..n) em T.
    """
    n = len(pai) - 1
    filhos = [[] for _ in range(n + 1)]
    raiz = -1
    for v in range(1, n + 1):
        if pai[v] == -1:
            raiz = v
        else:
            filhos[pai[v]].append(v)

    ans = [0] * (n + 1)
    ans[1] = n  # cada nó isolado é um caminho de comprimento 1

    # Matriz fixa n+1 x n+1: arr[v][d] = nº de nós na subárvore de v à distância d
    arr = [[0] * (n + 1) for _ in range(n + 1)]
    length = [0] * (n + 1)   # length[v] = número de posições válidas em arr[v] (0..length[v]-1)

    it = [0] * (n + 1)
    pilha = [raiz]

    while pilha:
        v = pilha[-1]

        if length[v] == 0:
            arr[v][0] = 1
            length[v] = 1

        # se um filho já foi processado, mescla ele agora
        if it[v] > 0:
            c = filhos[v][it[v] - 1]
            av, ac = arr[v], arr[c]
            lv, lc = length[v], length[c]

            for d1 in range(lv):
                cnt1 = av[d1]
                if cnt1 == 0:
                    continue
                for d2 in range(lc):
                    cnt2 = ac[d2]
                    if cnt2:
                        ans[d1 + d2 + 2] += cnt1 * cnt2

            for d2 in range(lc):
                av[d2 + 1] += ac[d2]

            length[v] = max(lv, lc + 1)

            # limpa a linha do filho (opcional, útil se fosse reutilizar memória)
            for d2 in range(lc):
                ac[d2] = 0
            length[c] = 0

        if it[v] < len(filhos[v]):
            c = filhos[v][it[v]]
            it[v] += 1
            pilha.append(c)
        else:
            pilha.pop()

    return ans


# Exemplo de uso
pai = [None, -1, 1, 1, 2]   # pai[1]=-1, pai[2]=1, pai[3]=1, pai[4]=2
ans = contar_caminhos(pai)
for k in range(1, len(pai) - 1 + 1):
    print(f"caminhos de comprimento {k}: {ans[k]}")