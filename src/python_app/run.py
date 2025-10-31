print("Hello Titanic!")
import pandas as pd
import os

# Load Titanic training data
data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'train.csv')
df = pd.read_csv(data_path)

# Quick look at the data
print("First 5 rows of the dataset:")
print(df.head())

print("\nColumns in the dataset:")
print(df.columns)

print(f"\nNumber of passengers: {len(df)}")
print(f"Number of survivors: {df['Survived'].sum()}")
