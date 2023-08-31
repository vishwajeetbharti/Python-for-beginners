from matplotlib import pyplot as plt
import pandas as pd
from collections import Counter

stu_data = pd.read_csv('amc.csv')

addmi_count = Counter()
addmission_kotta= []
no_Of_Students= []

addmission_data = stu_data['admittedQuota']

for item in addmission_data:
    addmi_count.update([item])

for item in addmi_count:
    addmission_kotta.append(item)
    no_Of_Students.append(addmi_count[item])

plt.barh(addmission_kotta,no_Of_Students,color='green')
plt.xlabel('Number of student')
plt.title('Students addmision Lists')
plt.show()