from matplotlib import pyplot as plt
import pandas as pd
from collections import Counter

students = pd.read_csv('amc.csv')

all_data = pd.DataFrame(students)
sem_accr_gen = all_data[['sem','gender']]

sem = {}
for item in range(len(sem_accr_gen)):
    if f'{sem_accr_gen["sem"][item]}_SemMale' not in sem.keys():
        sem[f'{sem_accr_gen["sem"][item]}_SemMale'] = 0
        sem[f'{sem_accr_gen["sem"][item]}_SemFemale'] = 0

    if(sem_accr_gen['gender'][item]=="m"):
        sem[f'{sem_accr_gen["sem"][item]}_SemMale'] +=1
    elif(sem_accr_gen['gender'][item]=="f"):
        sem[f'{sem_accr_gen["sem"][item]}_SemFemale'] +=1

key = []
value = []

for item in sem:
    key.append(item)
    value.append(sem[item])
plt.barh(key, value)
plt.title('population according semesters')
plt.show()