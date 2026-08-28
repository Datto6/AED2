def comb(vida, poderes,M):
    if M[vida]!=-1:
        return 1
    caminhos = 0
    for poder in poderes:
        dano = poder[0]
        x = poder[1]

        if dano <= vida and vida % (2**x) == 0:
            caminhos += comb(vida - dano, poderes)

    return caminhos % (10**9 + 7)

poderes=[(1,0),(1,1),(4,3),(1,1),(8,0),(5,2)]
print(comb(100,poderes))