def Consec(A):
    dict={}
    dict[A[0]]=1
    for i in range(1,len(A)):
        elemento=A[i]
        anterior=dict.get(elemento-1) #elemento é key, valor é quantos elementos na subsequencia começando ali
        if anterior!=None:
            dict[elemento]=anterior+1
        else:
            dict[elemento]=1
    max_key=max(dict,key=dict.get)
    B=[]
    for i in range(max_key-dict[max_key]+1,max_key+1): #de max_key-numero de elementos+1 até max_key
        B.append(i)
    return B
A=[2,4,1,5,6,9,10,11,12,7,-7,-6,-5,-4,-3,-2,-1]

print(Consec(A))