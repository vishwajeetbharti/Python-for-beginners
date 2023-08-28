import pandas as pd
import numpy as np

arr = np.array([45,45,6,-6,0,45,67])

a = pd.Series(arr,index = [9,8,7,4,5,6,1])# 9,8,7,4,5,6,1 assigned index to given values

print(a[9])