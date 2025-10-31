import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

print("Loading Titanic training data...")
df = pd.read_csv("data/train.csv")
print("✅ Data loaded successfully!")
print("Data preview:")
print(df.head())

print("\nBasic info:")
print(df.info())

print("\nMissing values per column:")
print(df.isnull().sum())


train_pred = model.predict(X_train)
val_pred = model.predict(X_val)

print("Training accuracy:", round(accuracy_score(y_train, train_pred), 4))
print("Validation accuracy:", round(accuracy_score(y_val, val_pred), 4))

print("Loading test set...")
test = pd.read_csv("src/data/test.csv")
test['Age'].fillna(df['Age'].median(), inplace=True)
test['Sex'] = test['Sex'].map({'male': 0, 'female': 1})
test['Embarked'].fillna('S', inplace=True)
test['Embarked'] = test['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})
test['Fare'].fillna(df['Fare'].median(), inplace=True)

predictions = model.predict(test[features])
print("Predictions for test set completed. Sample output:")
print(predictions[:10])