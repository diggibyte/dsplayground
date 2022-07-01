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

# columns in dataset
column = df.columns
print(column)

# len of dataset
length_dataset = len(df)
print(length_dataset)

# checking data types
data_types = df['agent'].dtypes()
print(data_types)

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

random_col = np.random.randint(100, size=len(df))
df.insert(3, 'Random_col', random_col, allow_duplicates=False)
print(df['Random_col'])

# replacing the values
df['checking'] = df['checking'].replace(to_replace=1, value=10)
print(df['checking'])

# checking the values in it or not
values = [1, 10, 54, 60, 56]
print(df[df['agent'].isin(values)])

# using groupby on columns
df1 = df.sample(n=500)
grpby_hotel = df1.groupby('hotel').groups  # taking groupby sum on sample data
print(grpby_hotel)

# checking count of values in rows
row_count = df.count(0)
print(row_count)

# checking the value count
count_value = df['agent'].value_counts(ascending=True)  # this gives us each unique value count
print(count_value)

# rank
df['rank_cal'] = df['agent'].rank()
print(df['rank_cal'])

# cross tab gives the frequency of two variables
cros_tab = pd.crosstab(df['agent'], df['country'])
print(cros_tab)

largest = df.nlargest(n=5, columns='agent')
print(largest)

# gives n number of rows with smallest day in waiting list
smallest = df.nsmallest(n=10, columns='days_in_waiting_list')
print(smallest)
# filling nan values in rank cal
df['rank_cal'].fillna(df['rank_cal'].median(), inplace=True)
