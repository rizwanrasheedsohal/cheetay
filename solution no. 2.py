
def pivotSelection(arr,n):
    #special Case
    if(len(arr) == 1):
        return 1
    pivot=1
    for j in range(n-2):
        left=0
        right=0
        for i in range(n):
            if(i<pivot):
                left=left+arr[i]
            elif(i>pivot):
                right=right+arr[i]
        pivot=pivot+1
        if(left==right):
            return pivot
    return -1

