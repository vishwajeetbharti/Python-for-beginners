is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]

# iterate on each lambda function
# and invoke the function to get the calculated value
for item in is_even_list:
	print(item())
print(is_even_list)


isEven = lambda x: x if (x % 2 ==0) else 0
for r in range(10):
	print(isEven(r))


# filter() function is used to filter the false function example 
li=[4,65,7,8,45,7,345,567,45,76,34,54]
isOdd= list(filter(lambda x:(x%2!=0),li))
print(isOdd)


# sorted function with lambda 
sort= sorted(li , key= lambda x: x)
print(sort)