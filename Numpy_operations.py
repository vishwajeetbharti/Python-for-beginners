import numpy as np

a = np.array([(3,5,6),(7,8,5),(3,5,3)])
b = np.array([(1,5,5),(5,9,5),(3,5,2)])

#Basic Operation by Numpy\

print("adding 1 to a value\n",a+1,"\nsubtraction by 1 in a\n",a-1,"\nMultiply by 2 in a\n",a*2,"\nSquaring of each element\n",a**2)
print("The Max element in the a matrix ",a.max(),"in every ROW ",a.max(axis =1))
print("The min element in matrix a ",a.min(),"in every coloumn ",a.max(axis =0))
print("The Sum of an Matrix ",a.sum())# Sum of an Matrix
print("The Cumulative  sum of an matrix\n",a.cumsum(axis=0))# https://www.mathworks.com/help/matlab/ref/cumsum.html

#Matrix Operation 

print("The sum of two matrix a and b is\n",a+b,
      "\nThe subtraction of two matrix a and b is\n",a-b,
      "\nThe multiply of two matrix a and b(element wise multiplication) is\n",a*b,
      "\nThe multiplication of two matrix a and b is\n",a.dot(b))