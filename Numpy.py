import numpy as ns
#Numpy is ais a general-purpose array-processing package,
#provides a high-performance multidimensional array object and tools for working with these arrays.

arr = ns.array([('ab','g','t','o'),('n','e','j','u')])
arr1 = ns.array(([1,4,6,3,7,3],[6,784,8,45,9,3]),dtype= 'double')
a= ns.zeros((3,3))
b = ns.full((3,3), 6,dtype='int')# we can also use complex data type like (3+5i) using {dtype='complex'}
randomValue= ns.random.random((3,3))
c= arr.reshape(2,2,2)
d= arr1.flatten()

print(ns.version.version)
print(arr)
print("Size of array",arr.size)
print("array dimension axis",arr.ndim)
print("array Shape",arr.shape)
print("array data type",arr.dtype) #it will print <U2, U stands for unicode, a type of string encoding and the number indicates the length of the string.
print(arr1)
print(a)
print(b)
print(randomValue)
print("Orignal shape\n",arr,"\n reshaped\n",c)
print(d)