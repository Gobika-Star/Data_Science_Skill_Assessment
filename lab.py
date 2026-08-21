import pandas as pd
import numpy as np
#data loading
df=pd.read_csv('Q06_museum_visitors.csv')
print("Data loaded successfully")

#data cleaning
print(df.shape)
print("NUmber of rows:",df.shape[0])
print("NUmber of columns:",df.shape[1])

print("Data types")
print(df.dtypes)

df.describe()

#missing values present in each column
print(df.isnull().sum())

#check duplicate rows
dup=df.duplicated().sum()
print("Number of duplicate rows:",dup)

#remove duplicates
rem_dup=df.drop_duplicates()
print("Rows after removing duplicates:",rem_dup)
print(len(rem_dup))


df["date"] = pd.to_datetime(df["date"])
df["weekday"] = df["date"].dt.day_name()
print(df[["date", "weekday", "visitor_count"]].head())

print(df['weather'].value_counts())

print(df['special_exhibition'].value_counts())

df["special_exhibition"] = df["special_exhibition"].fillna(df["special_exhibition"].mode()[0])

footfall_per_exhibition = df.groupby(
    "special_exhibition"
)["visitor_count"].mean()

print(footfall_per_exhibition)

redefined_csv=df.to_csv('museum_visitors.csv')
print("Data copied sucessfully")
