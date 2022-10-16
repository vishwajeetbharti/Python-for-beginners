str="Hi i am yukthi"
print(str)

def changeline (string , word):
    newstr= string.replace(word,"")
    return newstr.strip()


print(changeline(str,"Hi"))