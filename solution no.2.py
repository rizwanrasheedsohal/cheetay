def activitySelection(s,f,n):
    fList, sList = zip(*sorted(zip(f, s)))
    smallest=fList[0]
    conflict=0
    for i in range(n-1):
        if(sList[i+1] <= smallest):
            conflict=conflict+1
        else:
            smallest=fList[i+1]
    return n-conflict