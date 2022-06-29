# importing required libraries
import pandas as pd
import numpy as np

# loading the dataset
df = pd.read_csv(r"C:\diggibyte\hotel_bookings.csv")
print(df.head())

# checking the information of dataset
print(df.info())

# checking the null value count
print(df.isnull().sum())

# statistical information for numerical data
print(df.describe())
print(df.describe(include='int'))  # describe integer statistical information
print(df.describe(include='float'))  # describes float statistical information

# statistical information for categorical data
print(df.describe(include='object'))
