# -----------------------------
# Titanic Logistic Regression (Base R)
# -----------------------------
cat("Loading Titanic training data...\n")
train <- read.csv("data/train.csv")
cat("Data loaded successfully!\n")

cat("Data preview:\n")
print(head(train, 5))

cat("\nBasic info:\n")
str(train)

cat("\nMissing values per column:\n")
print(colSums(is.na(train)))

# -----------------------------
# Clean and preprocess data
# -----------------------------
cat("\n🔧 Cleaning and preparing data...\n")

train$Age[is.na(train$Age)] <- median(train$Age, na.rm = TRUE)
train$Embarked[is.na(train$Embarked)] <- "S"
train$Sex <- ifelse(train$Sex == "male", 0, 1)

# Convert Embarked to dummy variables manually
train$Embarked_C <- ifelse(train$Embarked == "C", 1, 0)
train$Embarked_Q <- ifelse(train$Embarked == "Q", 1, 0)
train$Embarked_S <- ifelse(train$Embarked == "S", 1, 0)

# Select relevant columns
features <- c("Pclass", "Sex", "Age", "SibSp", "Parch", "Fare",
              "Embarked_C", "Embarked_Q", "Embarked_S")
train_data <- train[, c("Survived", features)]

# Split training and validation data (80/20)
set.seed(42)
n <- nrow(train_data)
train_idx <- sample(seq_len(n), size = 0.8 * n)
train_set <- train_data[train_idx, ]
val_set <- train_data[-train_idx, ]

# -----------------------------
# Train logistic regression
# -----------------------------
cat("\nTraining logistic regression model...\n")
model <- glm(Survived ~ ., data = train_set, family = binomial)
cat("Model trained successfully!\n")

# -----------------------------
# Evaluate performance
# -----------------------------
train_pred <- ifelse(predict(model, train_set, type = "response") > 0.5, 1, 0)
val_pred <- ifelse(predict(model, val_set, type = "response") > 0.5, 1, 0)

train_acc <- mean(train_pred == train_set$Survived)
val_acc <- mean(val_pred == val_set$Survived)

cat(sprintf("Training Accuracy: %.4f\n", train_acc))
cat(sprintf("Validation Accuracy: %.4f\n", val_acc))

# -----------------------------
# Predict on test data
# -----------------------------
cat("\nLoading test dataset...\n")
test <- read.csv("data/test.csv")
test$Age[is.na(test$Age)] <- median(train$Age, na.rm = TRUE)
test$Fare[is.na(test$Fare)] <- median(train$Fare, na.rm = TRUE)
test$Sex <- ifelse(test$Sex == "male", 0, 1)
test$Embarked[is.na(test$Embarked)] <- "S"
test$Embarked_C <- ifelse(test$Embarked == "C", 1, 0)
test$Embarked_Q <- ifelse(test$Embarked == "Q", 1, 0)
test$Embarked_S <- ifelse(test$Embarked == "S", 1, 0)

X_test <- test[, features]

cat("\nMaking predictions on test dataset...\n")
test$Survived_Pred <- ifelse(predict(model, X_test, type = "response") > 0.5, 1, 0)

cat("Sample predictions (PassengerId → Survived):\n")
print(head(test[, c("PassengerId", "Survived_Pred")], 10))

cat("\nPrediction complete! Titanic model finished successfully.\n")
