print("Lodaing Datasets")
import pandas as pd

# Load the CSV dataset
df = pd.read_csv("data.csv")

# Display the first few rows (head) and last few rows (tail)
print("--- First 3 Rows ---")
print(df.head(3))

print("\n--- Last 2 Rows ---")
print(df.tail(2))

print("Info Datasets")

import pandas as pd

df = pd.read_csv("data.csv")

# Get basic details about rows, columns, and data types
print("Columns in dataset:", df.columns.tolist())
print("Shape (Rows, Columns):", df.shape)

print("\n--- Dataset Summary & Info ---")
df.info()

print("\n--- Statistical Summary ---")
print(df.describe())