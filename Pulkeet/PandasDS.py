import pandas as pd
import numpy as np

hotel = pd.read_csv(r'C:\Users\pulke\OneDrive\Desktop\hotel_bookings.csv')

#Head of the Dataset
print(hotel.head())

#Tails of the Dataset
print(hotel.tail())

#Shape of the Dataset
print(hotel.shape)

#Checking Features Dtype ,Non-null count  part of the dataset
print(hotel.info())

#Printing features names
print(hotel.columns)

#Stats measures of the Numerical features
print(hotel.describe())

#Memory using by each feature
print(hotel.memory_usage())

#Printing group of rows and columns using loc[]
print(hotel.loc[0:4,['hotel', 'lead_time', 'arrival_date_month']])

#Printing group of rows and columns using iloc[]
print(hotel.iloc[0:4])

#Value_Count()
print(hotel['market_segment'].value_counts())

#Group_by()
print(hotel.groupby('distribution_channel').adr.mean())

#Sorting
print(hotel.sort_values('reservation_status_date'))

#Dropping the Features and checking the Feature Again
print(hotel.drop('hotel',axis=1,inplace=True))
print(hotel.columns)

#Inserting new columns
hotel1 = hotel.insert(2,'XYZ',value=1)
print(hotel1)
print(hotel['XYZ'])
#CHecking the col again
print(hotel.columns)

#length of dataset
print(len(hotel))

#Datatypes of feature
print(hotel.dtypes)

#Renaming the columns name
print(hotel.rename(columns = {'meal':'meals','country':'countries'},inplace=True))
print(hotel.columns)

#Checking the missing values
print(hotel.isnull())
print(hotel.isnull().sum())

#Filling the missing value with 1
print(hotel.fillna(1,inplace=True))
print(hotel.isnull().sum())




