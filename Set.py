b= {}# it is empty Dictionary
print(type(b))# OUTPUT 'DICT'

c=set() #it is empty set
print(type(c))# OUTPUT 'set'

c.add(55)
c.add(88)
c.add(99)
c.add(77)
c.add(88)
# set is collection of non-repeatble element
c.add((88,55,22))# we can add tuple in set
#c.add({7:8}) we cannot add list or dictionary in set,because they are not hashable

print(c)
c.remove(99)
#c.remove(11) when we remove the element from set which is not in the set then it will throw KeyError

print(c.pop())
print(c)

print("\n",c.union({14,15}))# it will print the union of given value and the set value's
print(c.intersection({88,55}))# it will print the intersection of given value and the set value's