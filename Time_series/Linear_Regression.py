import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#print csv file and drop 1 column
df = pd.read_csv("/home/dunggps/Code_đảo_điên/MLOps/MLOps/Time_series/book_sales.csv",
                index_col ='Date',
                parse_dates=['Date'],
                ).drop('Paperback', axis = 1)
print(df.head())

#Add 1 column name Time
df['Time'] = np.arange(len(df.index))

print(df.head())

sns.set(style="whitegrid")  # Sử dụng style whitegrid

# plt.style.use("seaborn-whitegrid")
plt.rc(
    "figure",
    autolayout=True,
    figsize=(11, 4),
    titlesize=18,
    titleweight='bold',
)
plt.rc(
    "axes",
    labelweight="bold",
    labelsize="large",
    titleweight="bold",
    titlesize=16,
    titlepad=10,
)
# %config InlineBackend.figure_format = 'retina'

fig, ax = plt.subplots()
ax.plot('Time', 'Hardcover', data=df, color='0.75')
ax = sns.regplot(x='Time', y='Hardcover', data=df, ci=None, scatter_kws=dict(color='0.25'))
ax.set_title('Time Plot of Hardcover Sales');
plt.show()

df['History'] = df['Hardcover'].shift(1)
df = df.reindex(columns=['Hardcover', 'History'])
print(df.head())

fig, ax = plt.subplots()
ax = sns.regplot(x='History', y='Hardcover', data=df, ci=None, scatter_kws=dict(color='0.25'))
# ax.set_aspect('equal')
ax.set_title('Lag Plot of Hardcover Sales')
plt.show()