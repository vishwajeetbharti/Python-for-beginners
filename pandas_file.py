import pandas as pd


data = pd.read_csv('amc.csv')
data1 = pd.read_csv('nba.csv')

a = pd.DataFrame(data)
# fn = pd.Series(a['studentName'])



#print(a)
#print(fn.head(20))
data.dropna(inplace=True)# removing null value
b = data['sem'].describe()
#print(b)
print(a[['studentName','usn']].head())

allName = pd.read_csv('amc.csv',index_col='studentName')
mydata = allName.loc[['Vishwajeet Bharti']]
print(mydata)

