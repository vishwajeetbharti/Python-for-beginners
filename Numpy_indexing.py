import numpy

arr = numpy.array([(45,45,6,-6,0,45,3),(45,0,5,-4,56,-2,0),(45,0,5,-4,56,-2,67)])
temp = arr[1:,5:]#Slicing in python
temp1= arr[[1,0,2],[5,4,6]]
a= arr>0
b= arr<45
temp2 = (a&b).any()



print("array Shape is ",arr.shape)
print("Using Slice\n",temp)
print("Using indexing ",temp1)
print("Boolean array indexing (greater then zero and smaller then 45\n)", arr[temp2])
print("Original matrix\n",arr,"\nTranspose Matrix\n",arr.T)