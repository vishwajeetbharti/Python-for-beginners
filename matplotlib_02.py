from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# print(plt.style.available)# all available style of Graph
# # plt.style.use('seaborn-v0_8-bright')
# plt.xkcd() #graph Style
age = [10,11,12,13,14,15,16,18]
math_score = [85,80,87,75,80,66,70,45]
hindi_score = [95,76,70,79,78,86,90,99]
sceince_score = [55,56,60,63,62,71,73,85]

X_axis = np.arange(len(age))
width = 0.25


print(age)
plt.bar(X_axis+10 ,math_score,0.2,label='Math')
plt.bar(X_axis+10.2,hindi_score,0.2,label='Hindi')
plt.bar(X_axis+10.4,sceince_score,0.2,label='Science')
plt.xticks(X_axis+10.2, age)
plt.xlabel('Age')
plt.ylabel('Marks')
plt.title('Student Scores accro ages')
plt.legend()
# plt.legend(['Math','Hindi']) we can also give hint in graph this way
plt.grid()
# plt.tight_layout() #for padding issues of line  
plt.show()