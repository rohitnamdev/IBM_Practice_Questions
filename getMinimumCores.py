def getMinimumCores(starts,ends):
    e =[]
    for i in range(len(starts)):
        e.append((starts[i], 'start'))
        e.append((ends[i]+1, 'end'))
    e.sort(key=lambda x:(x[0],x[1]=='start'))
    m,c=0,0
    for x in e:
        if x[1]=='start':
            c+=1
            if c>m:
                m=c
        else:
            c=c-1
    return m
        
print(getMinimumCores([1,3,4],[3,5,6]))