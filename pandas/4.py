import numpy as np
import pandas as pd

# fruits = ['Apple','Banana','Pleapple','Berry','Cherry']
# # data = pd.Series(fruits)
# # print(data)
# # print(data[1:])

# data = pd.Series(fruits,index=['f1','f2','f3','f4','f5'])

# # print(data)
# # print(data['f1'])
# # print(data.loc[['f1','f2']])
# # print(data.loc['f1'])
# # print(data.iloc[[0,2,3]])

# #update in a cell

# # data.iloc[0] = 'Apples'
# # print(data)

# # data.loc['f1'] = 'Apple'
# # print(data)

# # data.loc[['f5','f4']] = 'Missing'
# # print(data)

# # data.iloc[1:3] = 'Mango'
# # print(data)


# #updating a multiple row with different value
# data.loc[['f5','f4']] = ['Missing1','Missing2']
# print(data)


# Dictionary as a series object

# car = {
#     'brand':'tata',
#     'engine':'700hp',
#     'model':'Harrier',
#     'year':2020
# }
# # x = pd.Series(car)
# # # print(x)
# # print(x['brand'])
# # x = pd.Series(car,index=['brand','model','type'])
# # print(x)

cars = {
    'Tata':['Nano','Altroz','safari','Harrier'],
    'Mahindra':['Thar','xuv500','Marazzo','Scropio']
}
df = pd.DataFrame(cars)
# print(df)
# print(df.loc[2])
# print(df.loc[2:])
# print(df.iloc[1])
# print(df.loc[[0,3]])
# print(df.Tata[0]) 

# df.Mahindra[2] = 'Bolero'
# print(df)
col_name = ['A','B','C','D']
