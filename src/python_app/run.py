print("Hello Titanic!")
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# -----------------------------
# 1. Load training data
# -----------------------------
data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'train.csv')
test_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'test.csv')

df = pd.read_csv(data_path)
print(f"Training data loaded successfully! Shape: {df.shape}")
print("\nFirst 5 rows:")
print(df.head())

# -----------------------------
# 2. Handle missing data
# -----------------------------
print("\nHandling missing data...")
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# -----------------------------
# 3. Feature Engineering
# -----------------------------
print("\nCreating new features...")

df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\\.', expand=False)
rare_titles = df['Title'].value_counts()[df['Title'].value_counts() < 10].index
df['Title'] = df['Title'].replace(rare_titles, 'Rare')

df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
df['IsAlone'] = (df['FamilySize'] == 1).astype(int)
df['CabinKnown'] = (~df['Cabin'].isna()).astype(int)

print("New features added: Title, FamilySize, IsAlone, CabinKnown")
print(df[['Title', 'FamilySize', 'IsAlone', 'CabinKnown']].head())

# -----------------------------
# 4. Prepare for model
# -----------------------------
print("\nPreparing data for logistic regression...")

features = ['Pclass', 'Sex', 'Age', 'Fare', 'Embarked',
            'FamilySize', 'IsAlone', 'CabinKnown', 'Title']
X = pd.get_dummies(df[features], drop_first=True)
y = df['Survived']

# Split into train and validation
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# -----------------------------
# 5. Train Logistic Regression
# -----------------------------
print("\nTraining Logistic Regression model...")
model = LogisticRegression(max_iter=500)
model.fit(X_train, y_train)

train_acc = accuracy_score(y_train, model.predict(X_train))
val_acc = accuracy_score(y_val, model.predict(X_val))

print(f"Training Accuracy: {train_acc:.4f}")
print(f"Validation Accuracy: {val_acc:.4f}")

# -----------------------------
# 6. Predict on test.csv
# -----------------------------
# -----------------------------
# 6. Predict on test.csv
# -----------------------------
if os.path.exists(test_path):
    print("\nLoading test.csv and generating predictions...")
    test_df = pd.read_csv(test_path)

    # Apply same feature engineering
    test_df['Title'] = test_df['Name'].str.extract(' ([A-Za-z]+)\\.', expand=False)
    test_df['Title'] = test_df['Title'].replace(rare_titles, 'Rare')
    test_df['FamilySize'] = test_df['SibSp'] + test_df['Parch'] + 1
    test_df['IsAlone'] = (test_df['FamilySize'] == 1).astype(int)
    test_df['CabinKnown'] = (~test_df['Cabin'].isna()).astype(int)

    # Fill missing values
    test_df['Age'] = test_df['Age'].fillna(df['Age'].median())
    test_df['Fare'] = test_df['Fare'].fillna(df['Fare'].median())
    test_df['Embarked'] = test_df['Embarked'].fillna(df['Embarked'].mode()[0])

    # Align columns and predict
    X_test = pd.get_dummies(test_df[features], drop_first=True)
    X_test = X_test.reindex(columns=X.columns, fill_value=0)
    preds = model.predict(X_test)

    # Evaluate if ground truth exists
    if 'Survived' in test_df.columns:
        test_acc = accuracy_score(test_df['Survived'], preds)
        print(f"Test Accuracy: {test_acc:.4f}")
    else:
        print("No 'Survived' column in test.csv — skipping test accuracy measurement.")

    # Save predictions
    output = pd.DataFrame({'PassengerId': test_df['PassengerId'], 'Survived': preds})
    output_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'predictions_python.csv')
    output.to_csv(output_path, index=False)
    print(f"Predictions saved to {output_path}")
else:
    print("\nNo test.csv found — skipping test predictions.")

print("\nTitanic pipeline complete.")