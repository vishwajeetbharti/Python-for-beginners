from matplotlib import pyplot as plt
import pandas as pd
from collections import Counter

gender = []
people= []

students = pd.read_csv('amc.csv')


addm_q = students['admittedQuota']
gen = students['gender']
gen_counter = Counter()
for row in gen:
    gen_counter.update([row])



for item in gen_counter.most_common(2):
    gender.append(item[0])
    people.append(item[1])
print(gender)
plt.barh(gender, people, color='maroon')
plt.title('Total population in College(male and Female)')
plt.xlabel('Gender')
# plt.ylabel('population')
plt.show()

