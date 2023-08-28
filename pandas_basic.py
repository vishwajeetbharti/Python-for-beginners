import pandas as pd

series = [('ab','g','t','o')]
dic = {'name':('Ran','Ram','Shyam'),'age':(17,35,78)}

arr = pd.DataFrame(series)
disarr = pd.Series(dic)
a = pd.DataFrame(dic)

print(arr)
print(disarr)
print(a)