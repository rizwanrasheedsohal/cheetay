def activitySelection(start,end,n):
    endList, startList = zip(*sorted(zip(end, start)))
    smallest=endList[0]
    conflict=0
    for i in range(n-1):
        if(startList[i+1] <= smallest):
            conflict=conflict+1
        else:
            smallest=endList[i+1]
    return n-conflict