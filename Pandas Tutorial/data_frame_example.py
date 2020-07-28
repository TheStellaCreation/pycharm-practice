import pandas as pd

# creating a DataFrame using list: DataFrame can be created using a single list or a list of lists
# list of strings
lst = ["Geeks", "For", "Geeks", "is", "portal", "for", "Geeks"]

# Calling DataFrame constructor on list
df = pd.DataFrame(lst)
print(df)

# [2,5] list
print('\n')

lst = [["Geeks", "For", "Geeks",  "portal", "for", "Geeks"],
       ["Geek", "For", "Geek", "portal", "for", "Geek"]]
df = pd.DataFrame(lst)
print(df)

# creating DataFrame form dict of ndarray/lists
# by default addresses
import pandas as pd

# initialise data of lists
print('\n')

data = {'name': ['Tom', 'Nick', 'Kris', 'Jack'],
        'age': [20, 21, 19, 18],
        'major': ['Business', 'Math', 'PM', 'Computer Science']}
# create DataFrame
df = pd.DataFrame(data)

print(df)

# Dealing with Rows abd Columns
# Column Selection: In Order to select a column in Pandas DataFrame,
# we can either access the columns by calling them by their columns name.

import pandas as pd

# define a dictionary containing employee data
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}

'''
dealing with row and columns
'''
# Import pandas package
import pandas as pd

print('\n\n')

# Define a dictionary containing employee data
data = {'Name': ['Jay', 'Prince', 'Gary', 'Annie'],
        'Age': [27, 24, 22, 32],
        'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)


# select two columns
print(df[['Name', 'Qualification']])


# row selection
import pandas as pd

print("\n\n")

# making data frame from csv file
data = pd.read_csv("/Users/stellayoyo/Downloads/nba.csv", index_col="Name")

# retrieving row by loc method
first = data.loc["Avery Bradley"]
second = data.loc["R.J. Hunter"]
third = data.loc["Kobe Bryant"]

print(first, "\n\n\n", second, "\n\n\n", third)

'''
indexing and selecting data = subset selection
'''

# importing pandas package
import pandas as pd

print('\n\n')

# making data frame from csv file
data = pd.read_csv("/Users/stellayoyo/Downloads/nba.csv", index_col="Name")

# retrieving columns by indexing operator
first = data["Age"]

print(first)


# selecting a single row
# indexing a DataFrame using .loc[ ] :

# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("/Users/stellayoyo/Downloads/nba.csv", index_col="Name")

# retrieving row by loc method
first = data.loc["Avery Bradley"]
second = data.loc["R.J. Hunter"]

print(first, "\n\n\n", second)

# Indexing a DataFrame using .iloc[ ] : only uses integer locations to make its selections.
import pandas as pd

print("\n\n\n")

# making data frame from csv file
data = pd.read_csv("/Users/stellayoyo/Downloads/nba.csv", index_col="Name")

# retrieving rows by iloc method
row2 = data.iloc[1]

print(row2)

# working with missing data: refer to as NA values in pandas
# checking for missing values using isnull( ) and notnull( )
import pandas as pd
import numpy as np

print('\n\n\n')

# dictionary of lists
dict = {'first score': [100, 9, np.nan, 95],
        'second score': [30, 45, 56, np.nan],
        "third score": [np.nan, 40, 80, 98]}
# creating a dataframe form list
df = pd.DataFrame(dict)

# using is null ( ) function
df.notnull()

print(df.notnull())
print(df.isnull())

# Filling missing values using fillna(), replace() and interpolate() :
import pandas as pd
import numpy as np
print('\n\n\n')
# dictionary of list
dict = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [100, 45, 56, np.nan],
        'Third Score': [np.nan, 40, 80, 100]}

# creating a dataframe form dictionary
df = pd.DataFrame(dict)
# filling missing value using fillna()
print(df.fillna(0))
print('\n')
print(df.replace(np.nan, "win"))
print('\n')
print(df.interpolate(method='linear', limit_direction='forward'))


# Dropping missing values using dropna() :
# In order to drop a null values from a dataframe,
# we used dropna() function this fuction drop Rows/Columns of datasets with Null values in different ways.

import pandas as pd

# importing numpy as np
import numpy as np
print('\n')

# dictionary of lists
dict = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, np.nan, 45, 56],
        'Third Score': [52, 40, 80, 98],
        'Fourth Score': [np.nan, np.nan, np.nan, 65]}

# creating a dataframe from dictionary
df = pd.DataFrame(dict)

print(df, '\n')
# using dropna() function
print(df.dropna())

# Iterating over rows and columns
# row: In order to iterate over rows, we can use three function iteritems(), iterrows(), itertuples() .
# These three function will help in iteration over rows.
# apply iterrows() function in order to get a each element of rows.

import pandas as pd
print('\n')

# dictionary of lists

dict = {'name': ["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score': [90, 40, 80, 98]}

# creating a dataframe from a dictionary
df = pd.DataFrame(dict)

print(df, '\n')
# iterating over rows using iterrows() function
for i, j in df.iterrows():
    print(i, j)
    print()

# example 2
import pandas as pd

# making data frame from csv file
data = pd.read_csv("/Users/stellayoyo/Downloads/nba.csv")
# for data visulaization we filter first 3 datasets
data = data.head(3)
print(data)
for i, j in data.iterrows():
    print(i, j)
    print()

# apply a iteritems() function in order to retrieve an rows of dataframe.
import pandas as pd

# making data frame from csv file
data = pd.read_csv("/Users/stellayoyo/Downloads/nba.csv")
# for data visulaization we filter first 3 datasets
data = data.head(3)
print(data)
for key, value in data.iteritems():
    print(key, value)
    print()

# apply itertuples () function in order to get tuple for each row

import pandas as pd

# making data frame from csv file
data = pd.read_csv("/Users/stellayoyo/Downloads/nba.csv")
# for data visulaization we filter first 3 datasets
data = data.head(3)
print(data)
for i in data.itertuples():
    print(i)

# Iterating over Columns :
# importing pandas module
import pandas as pd

# making data frame from csv file
data = pd.read_csv("/Users/stellayoyo/Downloads/nba.csv")

# for data visualization we filter first 3 datasets
col = data.head(3)

# creating a list of dataframe columns
clmn = list(col)

for i in clmn:
        # printing a third element of column
        print(col[i][2])















