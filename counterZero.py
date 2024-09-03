arr = [2,1,3,6,5,4,4,9]
def sol(arr):
    # counter = 0
    result = [0]
    for n in range(1,len(arr)):
        counter = 0
        for i in range(n,0,-1):
            counter = counter+(arr[n]-arr[i-1])
        result.append(counter)
    return result

print(sol(arr))