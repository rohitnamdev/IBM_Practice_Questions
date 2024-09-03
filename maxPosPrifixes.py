def maxPosPrefixes(arr):
    arr.sort(reverse =True)
    count =0
    psum = 0
    for num in arr:
        psum+=num
        if psum>0:
            count+=1
        else:
            break
    return count

print(maxPosPrefixes([-3,0,2,1]))