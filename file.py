import os

f= open("string.txt",'a')
f.write("please write somthing to file")
f.close

with open("string.txt","r")as k:
    g= k.read()
    #g=k.readline() for reading a line in file string.txt
    print(g)
    if 'pleaso' in g:
        print("this is present in the text")
    else:
        print("this is not present")

def rename(oldname , othername):
    with open(oldname,"r") as f:
        context = f.read()
    with open(othername,'w')as f:
        f.write(context)

rename("string.txt","NotePad.txt")
os.remove("string.txt")
