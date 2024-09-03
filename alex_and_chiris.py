def sol(n,lst):
    vowels = ["a","e","i","o","u"]
    res = []
    for s in lst:
        count =0
        for ch in s:
            if ch in vowels:
                count+=1
        if count%2==0:
            res.append("Chirs")
        else:
            res.append("Alex")
    return res
inp = ["ljis", "lhr","gms"]
print(sol(3,inp))
# Alex  - Odd ->  a,i,u
# chiris - ecen -> e,o