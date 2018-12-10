def fib(n):
    fib = [0]*n
    fib[0] = 1
    fib[1] = 1
    for i in range(2,n):
        print(fib)
        print(i)
        if fib[i] == 0:
            fib[i] = fib[i-1] + fib[i-2]
    
    return fib

print(fib(5))
