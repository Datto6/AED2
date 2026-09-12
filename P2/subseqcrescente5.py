def searchInsert(nums, target):

    start = 0
    end = len(nums) -1
    mid = 0

    while(start <= end): 
        mid = start + ( end - start)//2
        if(nums[mid] == target): 
            return mid
        elif(nums[mid] < target): 
            start = mid + 1
        else:
            end = mid - 1

    return start

def subseq(B,A):
    for i in range(len(A)):
        elemento=A[i]
        index=searchInsert(B,elemento)
        if index>=len(B):
            B.append(elemento)
        else:
            B[index]=elemento

def subseqAux(A):
    B=[]
    subseq(B,A)
    print(len(B))
A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
subseqAux(A)