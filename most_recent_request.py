def sol(arr,n):
    rev = arr[::-1]
    res = []
    for i in rev:
        if len(res)<=n and i not in res: res.append(i)
    return res
request = ["item1", "item2", "item3", "item1", "item3"]
res = sol(request,3)
print(res) 