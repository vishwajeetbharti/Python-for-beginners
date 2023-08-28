import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from IPython.display import display, HTML

# Generate sample data
np.random.seed(42)
n_rows = 10
dates = [datetime(2023, 1, 1) + timedelta(days=i) for i in range(n_rows)]
regions = np.random.choice(['North', 'South', 'East', 'West'], n_rows)
products = np.random.choice(['A', 'B', 'C'], n_rows)
sales = np.random.randint(50, 500, n_rows)
prices = np.random.randint(10, 100, n_rows)

# Create a pandas DataFrame
data = {'Date': dates, 'Region': regions, 'Product': products, 'Sales': sales, 'Price': prices}
df = pd.DataFrame(data)


proDetails = df.groupby('Product')['Sales'].sum()
proDetRes = df.groupby(['Product','Region'])['Sales'].sum()
avgDaily = df.groupby(['Date'])['Sales'].max()

new = pd.DataFrame(avgDaily)
# display(proDetails)
# display(proDetRes)
display(new['Sales'].mean())
display(avgDaily)