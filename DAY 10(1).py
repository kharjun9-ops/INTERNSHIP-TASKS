import pandas as pd

df = pd.read_csv("data.csv")

df['Age'] = df['Age'].fillna(df['Age'].mean().round())
df['Salary'] = df['Salary'].fillna(df['Salary'].median())
df = df.drop_duplicates()

df.to_csv("cleaned_data.csv", index=False)

print("✅ Cleaned dataset successfully exported to 'cleaned_data.csv'!")