import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

print("Loading Titanic training data...")
df = pd.read_csv("data/train.csv")
print("Data loaded successfully!")

print("Data preview:")
print(df.head(), "\n")

print("Basic info:")
print(df.info(), "\n")

print("Missing values per column:")
print(df.isnull().sum(), "\n")

# -----------------------------
# Clean and preprocess the data
# -----------------------------
print("🔧 Cleaning and preparing data...")

# Fill missing Age and Embarked values
df["Age"].fillna(df["Age"].median(), inplace=True)
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)

# Encode categorical variables
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
df = pd.get_dummies(df, columns=["Embarked"], drop_first=True)

# Select features and target
features = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked_Q", "Embarked_S"]
X = df[features]
y = df["Survived"]

# Split for validation
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# -----------------------------
# Build and train model
# -----------------------------

print("Training Logistic Regression model...")
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)
print("Model trained successfully!\n")

# -----------------------------
# Evaluate on training and validation data
# -----------------------------
train_pred = model.predict(X_train)
val_pred = model.predict(X_val)

print(f"Training Accuracy: {accuracy_score(y_train, train_pred):.4f}")
print(f"Validation Accuracy: {accuracy_score(y_val, val_pred):.4f}\n")

# -----------------------------
# Load test data and predict
# -----------------------------
print("Loading test dataset...")
test_df = pd.read_csv("data/test.csv")

# Fill missing values in test set
test_df["Age"] = test_df["Age"].fillna(df["Age"].median())
test_df["Fare"] = test_df["Fare"].fillna(df["Fare"].median())

# Encode categorical variables in test data
test_df["Sex"] = test_df["Sex"].map({"male": 0, "female": 1})
test_df = pd.get_dummies(test_df, columns=["Embarked"], drop_first=True)

# Ensure test_df has all required columns (some test files miss Embarked_Q)
for col in features:
    if col not in test_df.columns:
        test_df[col] = 0

X_test = test_df[features]

print("Making predictions on test dataset...")
test_pred = model.predict(X_test)

# Display first few predictions
print("Sample predictions (PassengerId → Survived):")
for pid, pred in zip(test_df["PassengerId"][:10], test_pred[:10]):
    print(f"{pid}: {pred}")

print("\nPrediction complete! Titanic model finished successfully.")