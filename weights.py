import math
def check_log(n):
    logaritmo=math.log2(n)
    return logaritmo==math.floor(logaritmo)
def weights(n):
    if (check_log(n)):
        return 1
    ceiling=1
    while(ceiling<n):
        ceiling=ceiling*2
    second=ceiling/2
    if (check_log(n-second)):
        return 2
    return weights(ceiling-n)+1
vezes=int(input())
for i in range(vezes):
    num=int(input())
    print(weights(num))