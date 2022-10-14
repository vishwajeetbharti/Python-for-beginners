list=["setu","sonu","betu","beru"]

for nami in list:
    if nami.startswith("b"):
        print("very good",nami)

prime=int(input("Enter to check th number is prime or not"))
check =True
for i in range(2,prime):
    if(prime%i==0):
        check=False
        break
else:
    print("Successful termination")


if check:
    print("This is prime number")
else:
    print("This is prime number")
