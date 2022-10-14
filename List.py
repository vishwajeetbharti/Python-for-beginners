list=["sonu","setu","betu","raju"]
print(list)

print(list[-3])
print(list[-3:])
list.sort() # sorting the same list ,doesn't return anything... 
print(list) # OUTPUT :-['betu', 'raju', 'setu', 'sonu'] =list;
list.reverse()
print(list) # reverse the data of list


list.append("Sita") # it will insert "sita" at the end of list
print(list)

list.insert(2,"Raja") # it will insert "Raja" at the given index
print(list)

list.pop() # element will poped out from last of index
print(list)

list.remove("Raja") #it will find element and remove from the list
print(list)
