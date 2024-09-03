def sol(n,d,arr):
    result = 0
    for i in range(0, n-2):
        for j in range(i+1,n-1):
            for k in range(j+1, n):
                if (arr[i]+arr[j]+arr[k]) % 5 ==0:
                    result +=1
    return result

print(sol(5,5,[3,3,4,7,8]))