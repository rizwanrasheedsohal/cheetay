
def longestSubstring(str,n):
    temp=[]
    index=0
    divider=0
    maxLength=1
    while(index<=n-1):
        if(str[index] not in temp):
            temp.append(str[index])
            if(len(temp) > maxLength):
                maxLength=len(temp)
        elif(str[index] in temp):
            divider=index-1
            index= str.index(str[index],divider)
            temp=[]
        index=index+1
    return maxLength