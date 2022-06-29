# importing required libraries
import pandas as pd
import numpy as np

# loading the dataset
df = pd.read_csv(r"C:\diggibyte\hotel_bookings.csv")
print(df.head())

# checking the information of dataset
print(df.info())
# checking the shape
print(df.shape)

# checking the null value count
print(df.isnull().sum())

# statistical information for numerical data
print(df.describe())
print(df.describe(include='int'))  # describe integer statistical information
print(df.describe(include='float'))  # describes float statistical information

# statistical information for categorical data
print(df.describe(include='object'))

# accessing the columns
print(df.iloc[:25, 1:5])
# inserting the new column with value 1
df.insert(3, 'checking', value=1)
print(df['checking'])

# selecting the data types
print(df.dtypes)
print(df.select_dtypes(['int', 'float']))  # selecting the integer and float data type columns
print(df.select_dtypes('object'))  # selecting the object type columns

print(df.iloc[:25].select_dtypes('object'))  # selecting 25 rows of all object columns
print(df.loc[:5, ['hotel', 'reservation_status', 'arrival_date_month']])  # accessing the 5 rows of three columns

# taking a small amount of sample from dataset
print(df.sample(n=500))
df1 = df.iloc[:500]
print(df1)

# where command
wait_day_less_10 = df['days_in_waiting_list'].where(df['days_in_waiting_list'] < 10)
print(wait_day_less_10)
hotel_wait = df['hotel'][df['days_in_waiting_list'] < 54]
print(hotel_wait)

# finding unique value in a column
unique_values = df['days_in_waiting_list'].unique()
print(unique_values)

not_unique = df['days_in_waiting_list'].nunique()
print(not_unique)  # gives the count of not unique values for particular column
df_non_unique_values = df.nunique()
print(df_non_unique_values)  # it counts not unique values in each column and gives us the count

# filling or replacing the null values
null_value_col = df.columns[df.isnull().sum() > 0]  # finding the columns that are having null values
print(null_value_col)

children_col = df['children']
print(children_col.unique())
df['children'].fillna(method='bfill', inplace=True)  # filled null values with backfill values
print(df['children'].describe())  # checking describe whether there is any change in statistical information

df['country'].fillna(method='ffill', inplace=True)
df['agent'].fillna(method='bfill', inplace=True)  # filling null values with backfill method

# drop column
df.drop(columns='company', axis=1, inplace=True)  # dropped this column because there are above 90% of null values
print(df.isnull().sum())
