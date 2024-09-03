def missing_prisoner(lst):
    m ={}
    n ={}
    for i in lst:
        x,y =i
        if x in m:
            m[x]+=1
        else:
            m[x] =1
        if y in n:
            n[y]+=1
        else:
            n[y]=1
    t=None
    for i,j in m.items():
        if j==1:
            t=1
            break
    l=None
    for j,j in n.items():
        if j==1:
            k=1
            break
    return [t,k]

loc = [[1,1],[5,1],[5,6]]
print(missing_prisoner(loc))
