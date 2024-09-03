def breakPalindrome(str):
    lstr = list(str)
    res = False
    for i in range(int(len(lstr)/2)):
        if lstr[i]!='a':
            lstr[i] ='a'
            res= True
            break
    return ''.join(lstr) if res==True else "IMPOSSIBLE"
print(breakPalindrome("aaaa"))