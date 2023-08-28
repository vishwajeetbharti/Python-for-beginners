import pandas as pd
import numpy as nm

students = pd.read_csv('amc.csv')

df = pd.DataFrame(students['sem'])

fifthSem = df.groupby('sem')

print(df)