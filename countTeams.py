def countTeams(t1,t2,p):
    m=float('inf')
    for x in range( p // t1 +1):
        r=p-t1*x
        if r%t2==0:
            y=r//t2
            m=min(m,x+y)
    return m if m!=float('inf') else -1

print(countTeams(3,4,6))