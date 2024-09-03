def countPair(lst, target):
    count =0
    for i in lst:
        for j in range(lst.index(i)+1):
            if abs(i-lst[j])==target:
                count+=1
                # print(i, lst[j])
    return count
lst = [2,4,6,8,10,12]
print(countPair(lst,2))
