def sol(i,j,k):
    res = 0
    while i < j:
        res += i
        i +=1
    while j >= k:
        res += j
        j -= 1
    return res

print(sol(0,5,-1))