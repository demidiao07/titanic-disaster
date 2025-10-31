cat("Hello Titanic from R!\n")

# Load required libraries
library(tidyverse)
library(caret)

# Load training data
data_path <- "../data/train.csv"
df <- read.csv(data_path)
cat("Training data loaded successfully! Rows:", nrow(df), "Cols:", ncol(df), "\n")

# Handle missing data
df$Age[is.na(df$Age)] <- median(df$Age, na.rm = TRUE)
df$Embarked[is.na(df$Embarked)] <- "S"

# Feature engineering
df$IsAlone <- ifelse(df$SibSp + df$Parch == 0, 1, 0)
df$Sex <- ifelse(df$Sex == "male", 1, 0)

cat("Missing values handled and new feature added: IsAlone\n")

# Train/test split
set.seed(42)
train_index <- createDataPartition(df$Survived, p = 0.8, list = FALSE)
train_df <- df[train_index, ]
val_df <- df[-train_index, ]

# Train logistic regression model
model <- glm(Survived ~ Pclass + Sex + Age + Fare + IsAlone, data = train_df, family = binomial)
cat("Model trained successfully!\n")

# Evaluate accuracy on validation set
pred_probs <- predict(model, val_df, type = "response")
preds <- ifelse(pred_probs > 0.5, 1, 0)
accuracy <- mean(preds == val_df$Survived)
cat("Validation Accuracy:", round(accuracy, 4), "\n")

# -----------------------------
# Predict on test.csv
# -----------------------------
test_path <- "../data/test.csv"
if (file.exists(test_path)) {
  cat("\nLoading test.csv and generating predictions...\n")
  test_df <- read.csv(test_path)

  # Apply same cleaning
  test_df$Age[is.na(test_df$Age)] <- median(df$Age, na.rm = TRUE)
  test_df$Fare[is.na(test_df$Fare)] <- median(df$Fare, na.rm = TRUE)
  test_df$IsAlone <- ifelse(test_df$SibSp + test_df$Parch == 0, 1, 0)
  test_df$Sex <- ifelse(test_df$Sex == "male", 1, 0)

  # Predict
  test_preds <- predict(model, test_df, type = "response")
  test_df$Survived <- ifelse(test_preds > 0.5, 1, 0)

  # Save predictions
  write.csv(test_df[, c("PassengerId", "Survived")],
            file = "../data/predictions_r.csv", row.names = FALSE)

  cat("Predictions saved to ../data/predictions_r.csv\n")
} else {
  cat("No test.csv found — skipping test predictions.\n")
}

cat("Titanic R pipeline complete!\n")
