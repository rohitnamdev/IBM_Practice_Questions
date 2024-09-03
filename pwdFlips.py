inp = "100110"

def countFlip(pwd):
    count =0
    for i in range(0,len(pwd)-1,2):
        count +=1 if pwd[i] != pwd[i+1] else None
    return count
print(countFlip(inp))