def minimizeCost(n,arr):
    total_cost =0
    arr.sort()
    while len(arr) != 1:
        s = arr[0]+arr[1]
        arr.append(s), arr.remove(arr[1]), arr.remove(arr[0])
        total_cost += s
    return total_cost
print(minimizeCost(3,[100,1]))