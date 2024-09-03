def findNumOfPairs(lst1,lst2):
    count =0
    for i in lst1:
        for j in lst2:
            if i>j:
                count+=1
                # print(i, lst[j])
    return count

print(findNumOfPairs([1,2,3],[1,21]))

def findNumofpairss(a,b):
    a.sort()
    b.sort()
    i,j,p=0,0,0
    while i <len(a) and j<len(b):
        if a[i]>b[j]:
            p+=1
            j+=1
        i+=1
    return p
print(findNumofpairss([1,2,3],[1,2,1]))

