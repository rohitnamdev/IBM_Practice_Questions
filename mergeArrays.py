def mergeArray(arr1,arr2):
    res = []
    for i in arr1:
        res.append(i)
    for j in arr2:
        res.append(j)
    res.sort()
    return res

def sol(arr1,arr2):
    return sorted(arr1+arr2)

print(sol([1,2,3],[2,5,5]))