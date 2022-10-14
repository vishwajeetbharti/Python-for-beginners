math=int(input("Enter the maths marks"))
hindi=int(input("Enter the hindi marks"))
english=int(input("Enter the english marks"))
science=int(input("Enter the science marks"))
sst=int(input("Enter the sst marks"))

tMarks=((math+hindi+english+science+sst)/500)*100
if tMarks>35:
    print("pass")
else:
    print("fail")