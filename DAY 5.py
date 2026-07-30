print("\n--- Handling Missing Data ---")
import pandas as pd
df = pd.read_csv("data.csv")

print("Missing values count:\n", df.isnull().sum())

df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].median())

print("\n--- After Filling Missing Values ---")
print(df)

print("\n--- Removing Duplicate Rows ---")

import pandas as pd
df = pd.read_csv("data.csv")

print("Duplicate rows count:", df.duplicated().sum())

df = df.drop_duplicates()

print("\n--- After Removing Duplicates ---")
print(df)

print("\n--- Correcting Data Types ---")
import pandas as pd

df = pd.read_csv("data.csv")
df['Age'] = df['Age'].fillna(df['Age'].mean())
df = df.drop_duplicates()

df['Age'] = df['Age'].astype(int)
df['Join_Date'] = pd.to_datetime(df['Join_Date'])
print("--- Data Types After Correction ---")
print(df.dtypes)
print("\nFinal Cleaned DataFrame:\n", df)