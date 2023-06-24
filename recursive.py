def factorial(n):
    if n==0 or n==1:
        return 1
    return n * factorial(n-1)

def fabonnaci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fabonnaci(n-1) + fabonnaci(n-2)

i=factorial(4)
j=fabonnaci(10)
print(i)
print(j)