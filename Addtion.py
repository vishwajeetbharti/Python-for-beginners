a=input("Enter the number: ")
b=input("Enter the another Number: ")

print(type(a))
print(type(b))

a=int(a)  #Type caasting- converting it to integer
b=int(b)

print("After converting data type- ",type(a))
print("After converting data type- ",type(b))

print("Result=  ",a+b)


# OutPut

# Enter the number: 9
# Enter the another Number7
# <class 'str'>
# <class 'str'>
# After converting data type-  <class 'int'>
# After converting data type-  <class 'int'>
# Result=   16