from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt # plotting
import numpy as np # linear algebra
import os # accessing directory structure
import pandas as pd # data pr


sentiData = pd.read_csv('tweet-sentiment-data.csv',delimiter=',', )
nRow, nCol = sentiData.shape
print(f'There are {nRow} rows and {nCol} columns')
# print(sentiData.head(10))

for col in sentiData.columns:
    print(col)

data = pd.DataFrame(sentiData)

data['tweet'] = data['tweet'].replace({'@':''},regex=True).str.lower()

data = data.assign(tweet_len=data['tweet'].str.len())# data['tweet_len'] = data['tweet'].str.len()
count = data['sentiments'].value_counts()
print(count)
print(data.head())
duplicates = data.duplicated()
print(duplicates)
