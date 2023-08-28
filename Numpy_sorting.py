import numpy as np

arr = np.array([0,np.pi/2,np.pi])
arr1 = np.array([(45,45,6,-6,0,45,3),(45,0,5,-4,56,-2,0),(45,0,5,-4,56,-2,67)])

print(np.sin(arr))
#print(np.sqrt(arr1))
print("array element sorted by\n",np.sort(arr1,axis= 0))
print(np.sort(np.sort(arr1,axis= 0),axis= 1,kind='mergesort'))


datatype = [('name','S10'),('age',int),('state','S10'),]
value = [('setu',21,'Bihar'),('Ram',19,'Mumbai'),('Raj',17,'kolkata')]

voters= np.array(value,dtype= datatype)

print(voters)#adding the ‘b’ character before a string literal creates a bytes literal. This means that the string content should be considered as a series of bytes and not characters
print(np.sort(voters,order= 'state'))