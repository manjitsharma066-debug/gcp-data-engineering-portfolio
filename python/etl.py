import pandas as pd

# Read CSV file
df = pd.read_csv("data/raw/sales.csv")

print("===== FIRST 5 RECORDS =====")
print(df.head())

print("\n===== DATASET INFORMATION =====")
df.info()

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== DUPLICATE RECORDS =====")
print(df.duplicated().sum())

print("\n===== TOTAL ROWS & COLUMNS =====")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

# Create Revenue column
df["Revenue"] = df["Quantity"] * df["Price"]

print("\n===== DATA WITH REVENUE =====")
print(df.head())

# Save cleaned data
df.to_csv("data/processed/cleaned_sales.csv", index=False)
print("\nCleaned file saved successfully!")