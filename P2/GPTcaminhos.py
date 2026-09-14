def caminhos(pai):
    n = len(pai)

    # Transformar pai[] em lista de filhos
    filhos = [[] for _ in range(n)]

    raiz = -1

    for i in range(n):
        if pai[i] == -1:
            raiz = i
        else:
            filhos[pai[i]].append(i)

    # --------------------------------------------------
    # Gerar uma ordem dos nós.
    # O pai sempre aparece antes do filho.
    # --------------------------------------------------

    ordem = []
    pilha = [raiz]

    while pilha:
        v = pilha.pop()
        ordem.append(v)

        for filho in filhos[v]:
            pilha.append(filho)

    # --------------------------------------------------
    # D[v][k] = quantidade de caminhos descendentes
    # de k nós começando em v
    #
    # Usaremos índices:
    # D[v][0] = 0
    # D[v][1] = 1
    # --------------------------------------------------

    D = [[0] * (n + 1) for _ in range(n)]

    # Resposta[k] = quantidade de caminhos
    # contendo exatamente k nós
    resposta = [0] * (n + 1)

    # Precisamos processar filhos antes dos pais
    for v in reversed(ordem):

        D[v][1] = 1

        # ----------------------------------------------
        # Calcula D[v]
        # ----------------------------------------------

        for c in filhos[v]:
            for k in range(2, n + 1):
                D[v][k] += D[c][k - 1]

        # ----------------------------------------------
        # Conta caminhos cujo nó mais alto é v
        # ----------------------------------------------

        # vistos[d] =
        # quantidade de nós a distância d de v
        # nos filhos já processados + o próprio v
        vistos = [0] * n
        vistos[0] = 1

        for c in filhos[v]:

            # e = número de arestas de c até o nó
            # Portanto, a distância até v é e + 1.
            for e in range(0, n):
                qtd = D[c][e + 1]

                if qtd == 0:
                    continue

                distancia_c = e + 1

                # Combina com todos os nós já vistos
                for d in range(n - distancia_c):
                    if vistos[d] == 0:
                        continue

                    # número de nós no caminho
                    k = d + distancia_c + 1

                    resposta[k] += vistos[d] * qtd

            # Agora os nós deste filho passam a estar
            # disponíveis para combinar com os próximos filhos
            for e in range(0, n):
                qtd = D[c][e + 1]

                if qtd == 0:
                    continue

                distancia = e + 1

                if distancia < n:
                    vistos[distancia] += qtd

    return resposta[1:]