print("--- Filtering rows ---")
import pandas as pd

df = pd.read_csv("data.csv").drop_duplicates()

high_salary = df[df['Salary'] > 60000]
print("--- Employees with Salary > 60,000 ---")
print(high_salary)
filtered = df[(df['Age'] > 25) & (df['Salary'] > 50000)]
print("\n--- Age > 25 & Salary > 50,000 ---")
print(filtered)

print("--- Selecting Columns ---")
import pandas as pd
df = pd.read_csv("data.csv")

names = df['Name']
print("--- Names Column ---")
print(names)

subset = df[['Name', 'Salary']]
print("\n--- Name and Salary Subset ---")
print(subset)

print("--- Sorting Dataset ---")
import pandas as pd
df = pd.read_csv("data.csv").drop_duplicates()

sorted_salary = df.sort_values(by='Salary')
print("--- Sorted by Salary (Ascending) ---")
print(sorted_salary)

sorted_age = df.sort_values(by='Age', ascending=False)
print("\n--- Sorted by Age (Descending) ---")
print(sorted_age)