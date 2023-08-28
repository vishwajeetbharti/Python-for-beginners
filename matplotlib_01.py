from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

print(plt.style.available)# all available style of Graph
# plt.style.use('seaborn-v0_8-bright')
plt.xkcd() #graph Style
age = [10,11,12,13,14,15,16,18]
math_score = [85,80,87,75,80,66,70,45]
hindi_score = [95,76,70,79,78,86,90,99]
sceince_score = [55,56,60,63,62,71,73,85]


plt.plot(age,math_score,color='r',linestyle='--',marker='.',label='Math')
plt.plot(age,hindi_score,color='b',linestyle=':',marker='.',label='Hindi')
plt.plot(age,sceince_score,color='g',linestyle='-.',marker='.',linewidth=3,label='Science')
plt.axis([8,20,10,100])
plt.xlabel('Age')
plt.ylabel('Marks')
plt.title('Student Scores accro ages')
plt.legend()
# plt.legend(['Math','Hindi']) we can also give hint in graph this way
plt.grid()
# plt.tight_layout() #for padding issues of line  

plt.show()