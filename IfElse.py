a=input("Enter the number to check the max value")
b=input("Enter the 2nd number to check the max value")

a=int(a)
b=int(b)

if(a>b):
    print(a)

elif(b>a):
    print(b)

num=[17,15,19]
ret=[]
bol=[19,10,15]
if(bol[0]>num[0]):
    print(bol[0]+num[0])
    ret=True
elif(bol[1]>num[1]):
    print(bol[1]+num[1])
    ret=True
elif(bol[2]>num[2]):
    print(bol[2]+num[2])
    ret=True
elif(bol[2]<num[2]):
    print(bol[2]+num[2])
    ret=False
elif(bol[1]<num[1]):
    print(bol[1]+num[1])
    ret=False
elif(bol[0]<num[0]):
    print(bol[0]+num[0])
    ret=False
else:
    print(ret)
    

if(bol[0]>num[0]):
    print(bol[0]+num[0])
    ret=True
if(bol[1]>num[1]):
    print(bol[1]+num[1])
    ret=True
if(bol[2]>num[2]):
    print(bol[2]+num[2])
    ret=True
if(bol[2]<num[2]):
    print(bol[2]+num[2])
    ret=False
if(bol[1]<num[1]):
    print(bol[1]+num[1])
    ret=False
if(bol[0]<num[0]):
    print(bol[0]+num[0])
    ret=False
else:
    print(ret)