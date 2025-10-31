print("Hello Titanic!")
import pandas as pd

# Load Titanic training data
data_path = '../data/train.csv'  # because run.py is in src/python_app
df = pd.read_csv(data_path)

# Quick look at the data
print("First 5 rows of the dataset:")
print(df.head())

print("\nColumns in the dataset:")
print(df.columns)

print(f"\nNumber of passengers: {len(df)}")
print(f"Number of survivors: {df['Survived'].sum()}")
