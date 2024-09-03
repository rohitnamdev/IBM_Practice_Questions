def maxTrailing(arr):
    res = -1
    x = arr[0]
    for i in range(1,len(arr)):
        if arr[i] >x:
            d = arr[i]-x
            if d>res:
                res=d
        else:
            x=arr[i]
    return res
print(maxTrailing([9,6,7,6,4,5]))