def ArvIndep(filhos,nos,no,peso):
    #Retorna arvore independente com maior peso, se baseando no fato que o rótulo de n é o peso dele
    inc=peso[no] #no entra, considera o peso dele 
    exc=0 #no não entra
    for filho in filhos[no]: #iterar sobre filhos
        resultado=ArvIndep(filhos,nos,filho,peso) 
        inc=inc+resultado[1] #adicionar valor excluindo o filho atual
        exc=exc+max(resultado) #se no atual sai, escolher maximo de filho, porque não importa qual
    return (inc,exc)


def ArvIndepAux(pai,nos,peso):
    filhos={}
    for i in range(len(pai)):
        filhos[nos[i]]=[]
    for i in range(len(pai)):
        if pai[i] != -1:
            filhos[pai[i]].append(nos[i])
    print(filhos)
    print(ArvIndep(filhos,nos,nos[0],peso))

pai = [-1, 1, 1, 2, 2, 3,3]
nos=[1,2,3,4,5,6,7]
peso=[0,3,4,1,2,5,6,1]
ArvIndepAux(pai,nos,peso) 