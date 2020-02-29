import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series([1, 3, 5, np.nan, 6, 8])

print(s)

#Creating a Dataframe

dates = pd.date_range(20130101, periods=6)

print(dates)


df = pd.DataFrame(np.random.randn(6, 4))
# the first number is how many rows its gonna produce and the second number is how many columns it is gonna produce ( both startint with 0 .... )

print(df)

# Creating a data frame with diictionaries(make sure to match up the collums and rows)

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(5)), dtype='float32'),
                    'D': np.array([3] * 5, dtype='float32'),
                    'E': pd.Categorical(["test", "train", "test", "train", "test"]),
                    'F': 'foo'})

print(df2)
print(df2.dtypes)
print(df.head())# how to view the top row of the frame
print(df.tail(3))#how to view the bottom row of the frame
print(df.describe())#shows a quick statistic summary of your data
print(df.T)
print(df.sort_index(axis=1, ascending=False))#(1 makes it 0-... 0 makes it ...-0)
print(df2.sort_values(by='E'))#aranges the list by coulumn/ row index
print(df2['A'])#prints the index value only
print(df2[0:3])#prints the sliced index values
print(df.loc[[1]])
#df2.to_excel('foo.xlsx', sheet_name='sheet1')
plt.close('all')

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))

ts = ts.cumsum()

ts.plot()

#plt.show()

