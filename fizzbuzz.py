def fizzbuzz(n):
    for i in range(1,n+1):
        print("fizzbuzz") if i %3 ==0 and i%5==0 else print("fizz") if i%3 ==0 else print("buzz") if i%5==0 else print(i)
fizzbuzz(100)
