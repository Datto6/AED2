def ArvIndep(filhos,nos,no):
    #Retorna número de arvores independentes
    inc=1 #no entra, apenas uma subarvore independente
    exc=1 #no não entra, conjunto vazio
    for filho in filhos[no]: #iterar sobre filhos
        resultado=ArvIndep(filhos,nos,filho) 
        inc=inc*resultado[1] #somar as possibilidades por princ multiplicativo no caso de exclusao do filho atual
        exc=exc*(sum(resultado)) #se nó atual sai, somar as possibilidades em ambos os casos do filho, pois agora ele tem liberdade total
    return (inc,exc)


def ArvIndepAux(pai,nos):
    filhos={}
    for i in range(len(pai)):
        filhos[nos[i]]=[]
    for i in range(len(pai)):
        if pai[i] != -1:
            filhos[pai[i]].append(nos[i])
    print(filhos)
    resultado=ArvIndep(filhos,nos,nos[0])
    print(resultado)
    print(sum(resultado))

pai = [-1, 1, 1, 2, 2, 3,3]
nos=[1,2,3,4,5,6,7]
ArvIndepAux(pai,nos) 