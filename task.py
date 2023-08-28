import numpy as np
import pandas as pd
from IPython.display import display, HTML

title = [('student_id','S3'),('math_score',int),('science_score',int),('history_score',int)]
data = [(1,85,78,92),(2,72,65,68),(3,90,88,78),(4,60,70,75),(5,78,92,80)]


students = np.array(data,dtype=title)
df = pd.DataFrame(students)

total = df.sum(axis=1,numeric_only= True)
df = df.assign(total_result=[total[0],total[1],total[2],total[3],total[4]])

avg = np.average(df['math_score'])

df.loc[len(df.index)] = ['avg',avg,np.average(df['science_score']),np.average(df['history_score']),np.average(df['total_result'])]
df.loc[len(df.index)] = ['mean',np.mean(df['math_score']),np.mean(df['science_score']),np.mean(df['history_score']),np.mean(df['total_result'])]
df.loc[len(df.index)] = ['max',np.max(df['math_score']),np.max(df['science_score']),np.max(df['history_score']),np.max(df['total_result'])]
df.loc[len(df.index)] = ['min',np.min(df['math_score']),np.min(df['science_score']),np.min(df['history_score']),np.min(df['total_result'])]

df.rename(columns={'student_id':'id','math_score':'score','science_score':'science_score','history_score':'history','total_result':'total_results'})

display(avg)
# display(df)
print(df)