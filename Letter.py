from dataclasses import replace


Letter='''\tHello,I am Name
Subject:- To leave
Date:<Date>

\tYour respectfull Students
Name
'''
print(Letter)#Before Replaceing Letter
Letter1=Letter.replace("Name","Visheajeet")
Letter2=Letter1.replace("Date","21-07-2002")
print(Letter2)



#OutPut


# Hello,I am Name
# Subject:- To leave
# Date:<Date>

#         Your respectfull Students
# Name

#*********************************************************

#         Hello,I am Visheajeet
# Subject:- To leave
# 21-07-2002:<21-07-2002>

#         Your respectfull Students
# Visheajeet