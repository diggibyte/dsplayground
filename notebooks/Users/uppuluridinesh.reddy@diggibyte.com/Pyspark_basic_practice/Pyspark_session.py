# Databricks notebook source
# MAGIC %md
# MAGIC ### Creating Pyspark Session 

# COMMAND ----------

import pyspark
from pyspark.sql import SparkSession

# creating a spark session
spark = SparkSession.builder.appName("pyspark practice").getOrCreate()

display(spark)

# COMMAND ----------

# MAGIC %fs
# MAGIC ls /mnt/tf-abfss/data/ds/food_inspection_dinesh

# COMMAND ----------

# MAGIC %md
# MAGIC ### Reading a csv file

# COMMAND ----------

csv_file = '/mnt/tf-abfss/data/ds/food_inspection_dinesh/tesla_stocks.csv'
df = spark.read.csv(csv_file)

# COMMAND ----------

# displaying the dataframe without header is true
display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Creating a dataframe with header is true 

# COMMAND ----------

# printing the schema of the data
data = spark.read.csv(
    '/mnt/tf-abfss/data/ds/food_inspection_dinesh/tesla_stocks.csv',
    sep = ',',
    header = True,
    )

data.printSchema()

# COMMAND ----------

display(data)

# COMMAND ----------

# checking the data types
data.dtypes

# COMMAND ----------

# getting the first 3 rows of data from spark dataframe
data.head(3)

# COMMAND ----------

data.show(2)

# COMMAND ----------

data.first()

# COMMAND ----------

data.describe().show()

# COMMAND ----------

data.columns

# COMMAND ----------

data.count()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Creating a new column as stock_Date with the reference of Date column

# COMMAND ----------

data = data.withColumn('stock_Date', data.Date)

data.show(5)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Renaming the column 

# COMMAND ----------

data = data.withColumnRenamed('stock_Date', 'Stock_date')

data.show(5)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Dropping the extra created colun from the spark dataframe

# COMMAND ----------

# after dropping the added column we are having the existing columns
data = data.drop('Stock_date')

data.show(5)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Imputting the missing values

# COMMAND ----------

# Remove Rows with Missing Values

data.na.drop()
data.show(5)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Selecting the single column and multiple column

# COMMAND ----------

## Selecting Single Column

data.select('High').show(5)

## Selecting Multiple columns

data.select(['Open', 'High', 'Low']).show(5)

# COMMAND ----------

# MAGIC %md
# MAGIC ### filtering the column

# COMMAND ----------

from pyspark.sql.functions import col, lit

data.filter((col('Open') >= lit('2010-07-01')) | (col('Open') <= lit('2010-07-31'))).show(5)

# COMMAND ----------

# MAGIC %md
# MAGIC ### filtering the data by using the between condition

# COMMAND ----------

## fetch the data where the adjusted value is between 100.0 and 500.0

data.filter(data.High.between(4.0, 4.5)).show(5)

# COMMAND ----------

# MAGIC %md
# MAGIC ### filtering the data by using the When condition

# COMMAND ----------

from pyspark.sql import functions as f
data.select('open', 'close', 
            f.when(data.High >= 4.0, 1).otherwise(0)
           ).show(5)

# COMMAND ----------

# MAGIC %md
# MAGIC ### filtering the data by using the like condition

# COMMAND ----------

data.select('Open', 
            data.Open.rlike('^[3]').alias('open with 3')
            ).distinct().show(5)

# COMMAND ----------

