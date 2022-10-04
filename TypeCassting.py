from ast import Str
from tokenize import Double


a="2114" #This is String..
print(type(a))


#Type casting
a=int(a) #convert a to integer(if possible)
c=float(55) #convert c to float(if possible)


print("After converting data type- ",type(a))
print("After converting data type- ",type(c))

print(a)
print(c)


# OutPut

# <class 'str'>
# <class 'int'>
# <class 'float'>
# 2114
# 55.0
