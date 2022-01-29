import numpy as np
import pandas as pd

dict1 = {
    'name':['aminur','harry','shubh','rohan'],
    'marks':[92,34,24,17],
    'city' :['rampur','kolkata','bareilly','antarctica']
}

# df = pd.DataFrame(dict1)
# # df.to_csv(' friends.csv')
# # df.to_csv('friends.csv',index=False)
# # print(df)  
# # print(df.head(2))
# # print(df.tail(2))
# # print(df.describe())

# harry = pd.read_csv('friends.CSV')
# # print(harry)
# # print(harry['marks'][0])
# harry.to_csv('friends.CSV')
# harry.index = ['first','second','third','fourth']
# print(harry)

# ser = pd.Series(np.random.rand(34))
# print(type(ser))

newf = pd.DataFrame(np.random.rand(334,5),index=np.arange(334))
# print(newf)
# print(type(newf))
# newf[0][0] = 'harry'
# print(newf)
# print(newf.head())
# print(newf.index)
# print(newf.columns)
# print(newf.to_numpy())
newf[0][0] = 0.3
# print(newf.head())
# print(newf.T)
# print(newf.sort_index(axis=0,ascending=False))
# print(newf[0])
# print(type(newf[0]))
newf.loc[0,0] = 654
# print(newf.head(2))
newf.columns = list("ABCDE")
# print(newf)
newf.loc[0,'A'] = 65445
# print(newf.head())
# print(newf.drop(0,axis=1))
# print(newf.loc[[1, 2], ['C', 'D']])
