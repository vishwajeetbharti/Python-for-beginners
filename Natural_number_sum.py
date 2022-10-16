n=int(input("Enter an number: "))
def sum(n):
    s=0
    for i in range(0,n+1):
        s=s+i
    return s

print(sum(n))

i=0
while i in range(n):
    print("*"*n)
    n=n-1
    