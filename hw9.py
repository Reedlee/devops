print('Problem9')
def problem9():
    [print(a,b,(1000-a-b),a*b*(1000-a-b)) for a in range(1,1000) for b in range(a + 1, 1000 - a) if a**2 + b**2 == (1000-a-b)**2]
problem9()

print('Problem6')
def problem6(n):
    return (n-1)*(n+1)*n*(3*n+2)/12

print(problem6(100))

print('Problem48')
from functools import reduce
def problem48(n):
    return str(reduce(lambda sum,i: sum + i**i, range(1,1000)))[-10:]

print(problem48(10))

print('Problem40')
def problem40():
    stri = ''
    for i in range(200000):
        stri += str(i)
    
    idx = 1
    multiple = 1
    for i in range(7):
        multiple *= int(stri[idx*10**i])

    return multiple
print(problem40())

