def sol(arr, n):
    for _ in range(n):
        arr = [x-3 if x%2==0 else x+3 for x in arr]
    return arr
print(sol([3,4,9],3))