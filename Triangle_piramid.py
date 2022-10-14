n=3

for i in range(n):
    print(" "*(n-i-1),end="")
    print("*"*(2*i+1))
    print(" "*(n-i-1))


for i in range(n+2):
    print("*"*i)

for i in range(n-1):
    if(i==1):
        print("* *")
    print("*"*n)