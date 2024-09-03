def findMissingInteger(arr,k):
    count=0
    i =1
    while count < k:
        if i not in arr:
            count+=1
            res = i
            i+=1
        else:
            i+=1
    return res
arr = [1,4,7,3,4]
print(findMissingInteger(arr,5))