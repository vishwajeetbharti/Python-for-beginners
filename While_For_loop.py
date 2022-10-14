toys=["boll","bat","wicket","cap"]
i=0
while i<len(toys):
    print(toys[i])
    i=i+1


for item in toys:
    print(item)


for i in range(11):
    print(i)

for i in range(2,21,2):# range(start,stop,step_size): step_size means gapeing
    print("\n",i)
    if i==10:
        break
else:
    print("successful terminatation, 2nd table has written")# for else loop ,else is optional


for i in range(2,21,2):# range(start,stop,step_size): step_size means gapeing
    print("\n",i)
    if i==11:
        break
else:
    print("successful terminatation, 2nd table has written")# for else loop ,else is optional...OUTPUT :-successful terminatation, 2nd table has written

