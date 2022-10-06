name=input("Enter Your Name.\n")
print("Good Morning, "+name)

name ="vishwajeet Bharti"
print(name[0])
# String slicing
print(name[0:6])# here printing of name from index 0 to 6...{Initial index:finalindex}
print(name[0:6:2])# here printing of name from index 0 to 6 *skiping* of 2 letter....
print(name[:10])# other advance slicing techniques
print(name[0:])# other advance slicing techniques
print(name[-6:-1])#Negative Index also can used
#String Function
print(len(name))#Length of String
print(name.endswith("Bharti"))# this Function tells weather string ends with given words
print(name.count("e"))# count function is used to count given character in the string
print(name.capitalize())#  capitalize function is used  to capitalize the first character of string
print(name.find("B"))# fing function is  used to find the word and return the index
print(name.replace("vishwajeet","Yukthi"))# Replace function is used to find the word and replce with given word