print("--- Salary Column Metrics ---")
import pandas as pd
df = pd.read_csv("data.csv").drop_duplicates()
df['Salary'] = df['Salary'].fillna(df['Salary'].median())

total_salary = df['Salary'].sum()
avg_salary = df['Salary'].mean()
min_salary = df['Salary'].min()
max_salary = df['Salary'].max()
total_count = df['Salary'].count()

print("--- Salary Column Metrics ---")
print(f"Total Sum: ${total_salary:,.2f}")
print(f"Average: ${avg_salary:,.2f}")
print(f"Minimum: ${min_salary:,.2f}")
print(f"Maximum: ${max_salary:,.2f}")
print(f"Total Non-Null Count: {total_count}")

print("\n--- Count of Entries per Column ---")
import pandas as pd
df = pd.read_csv("data.csv")

print("--- Count of Entries per Column ---")
print(df.count())
print("\n--- Summary Table using describe() ---")
print(df.describe())