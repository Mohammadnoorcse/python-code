import numpy as np
import pandas as pd
# dict1  = {
#     'name':['harry','rohan','skillf','shubh'],
#     'marks':[92,34,24,17],
#     'city':['rampur','kolkata','bareilly','antarctica']
# }
# df = pd.DataFrame(dict1)
# # print(df)
# df.to_csv('E:\\python code\\pandas\\aminur.csv')
# # df.to_csv('E:\\python code\\pandas\\aminur_indexFalse.csv', index=False)
# # print(df.head(2))
# # print(df.tail(2))
# print(df.describe()) 


# dict1 = {
#     'Train NO': [12322, 87787889, 454545, 56756765],
#     'speed': [92, 34, 24, 17],
#     'city': ['rampur', 'kolkata', 'bareilly', 'antarctica']
# }
# df = pd.DataFrame(dict1)
# # print(df)
# df.to_csv('E:\\python code\\pandas\\harry.csv') 
# harry = pd.read_csv('E:\\python code\\pandas\\harry.csv')
# harry.index = ['frist','second','third','fourth']
# # print(harry)

# ser = pd.Series(np.random.rand(34))
# print(ser)

newf = pd.DataFrame(np.random.rand(334,5),index=np.arange(334))
# print(newf)
# print(newf.head())
newf[0][0] = 'harry'
# print(newf.dtypes)
# print(newf.head())
# print(newf.index)
# print(newf.columns)

# print(newf.to_numpy)
newf[0][0] = 0.3
# print(newf.T)
# print(newf.head())
# print(newf.sort_index(axis=0,ascending=False))
# print(newf.sort_index(axis=1,ascending=False))

# newf2 = newf
# newf2[0][0] = 9783
# print(newf)

# newf2 = newf.copy()
# newf2[0][0] = 9783
# print(newf)

# newf.loc[0,0] = 654
# print(newf.head(2))

newf.columns = list('ABCDE')
# print(newf)

# print(newf.loc[[1,2],['C','D']])
# print(newf.loc[:,['C','D']])
# print(newf.loc[[1,2],:])
# print(newf.loc[(newf['A']<0.3)])
# print(newf.iloc[0,4])
# print(newf.drop([0]))
# print(newf.drop(['A'],axis = 1))
# print(newf.drop(['A','D'],axis = 1,inplace=True))
# print(newf.reset_index())
# print(newf.reset_index(drop=True))
# print(newf['B'].isnull())
# newf['B'] = None
# print(newf)

# newf.loc[:,['B']] = 34
# print(newf)

# df = pd.DataFrame({
#     'name': ['Alfred', 'Batman', 'Alfred'],
#     'toy' :[np.nan,'Batmobile','Bullwhip'],
#     'born': ['Alfred', pd.Timestamp('1940-04-25'), pd.NaT]
#                    })

# print(df.head())
# print(df.dropna())
# print(df.drop_duplicates(subset=['name']))
# print(df.drop_duplicates(subset=['name'],keep='last'))
# print(df.shape)
# print(df['toy'].value_counts(dropna=False))