import numpy as np
import pandas as pdimp



# fruits = ['Apple','Banana','Pieapple','Berry','Cherry']
# # data = pd.Series(fruits)
# # print(data)
# # print(data[1:])
# data = pd.Series(fruits,index=['f1','f2','f3','f4','f5'])
# # print(data)
# # print(data.loc[['f1','f2','f4']])
# # print(data.iloc[[0,2,3]])

# # update in cell 

# # data.iloc[0] = 'Apples'
# # print(data)

# # data.loc['f1'] = 'Apple'
# # print(data)

# #updating a multiple row

# # data.loc[['f1','f4']] = 'Missing'
# # print(data)

##Dictionary as a series object
  
# car = {'brand':'tata','engine':'700hp','Model':'Harrier','year':2020}
# x = pd.Series(car)
# print(x)

# car = {'brand':'tata','engine':'700hp','Model':'Harrier','year':2020}
# x = pd.Series(car,index=['brand','model','type'])
# print(x)


# DataFrames
#  is a collection of row and columns
# is 2-D array structure


# cars = {
#     'Tata':['Nano','Altroz','safari','Harrier'],
#     'Mahindra':['Thar','Xuv500','Marazzo','Scropio']
# }
# df = pd.DataFrame(cars)
# # print(df)
# # loc
# # print(df.loc[2])
# # print(df.loc[2:])
# # print(df.iloc[1])

# # print(df.loc[[0,3]])

# # print(df.Tata[0])

# #updating a cell in a pricular column

# df.Mahindra[2] = 'Bolero'
# print(df)

# col_name = ['A','B','C','D']
# values = [[1,2,3,4],[11,20,31,44],[13,23,53,42],[17,285,33,24]]
# df1 = pd.DataFrame(values, columns=col_name)
# # print(df1)

# #display the indexes
# # print(df1.index)
# # print(df1.columns)
# print(df1.drop('A',axis=1))

# reading a csv file

# df = pd.read_csv('E:\\python code\\pandas\\Aminur.csv')
# print(df)
# print(df.head(2))
# print(df.tail(2)) 
# print(df.to_string()) #to display all the rows of the data

# print(df.head(-2))  #it will exclude the last 2 rows from our dataset
# print(df.tail(-3)) #it will exclude the frist 3 rows from our dataset


dirty = pd.read_csv('E:\\python code\\pandas\\Book1.csv')
print(dirty)

# print(dirty.shape)
# print(dirty.columns)
# print(dirty.info())

# print(dirty.describe()) #it only takes numerical columns

#numeric data: quantitaive data
#categorical data: qualitative data
# print(dirty.duplicated())

# print[dirty[dirty.duplicated()]]
# print(dirty.drop(12))

# print(dirty.drop(12,inplace=True))

#dirty.drop_duplicates(inplace = True) #other option to drop the duplicate rows
