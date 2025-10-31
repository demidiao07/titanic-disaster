library(tidyverse)
library(caret)

cat("Loading Titanic training data...\n")
train <- read.csv("src/data/train.csv")

train$Sex <- ifelse(train$Sex == "male", 0, 1)
train$Embarked[train$Embarked == ""] <- "S"
train$Embarked <- as.numeric(factor(train$Embarked))

features <- c("Pclass","Sex","Age","SibSp","Parch","Fare","Embarked")
train$Age[is.na(train$Age)] <- median(train$Age, na.rm = TRUE)

set.seed(42)
idx <- createDataPartition(train$Survived, p=0.8, list=FALSE)
train_set <- train[idx,]
val_set <- train[-idx,]

cat("Training logistic regression model...\n")
model <- glm(Survived ~ ., data=train_set[,c("Survived", features)], family="binomial")

preds <- ifelse(predict(model, val_set[,features], type="response") > 0.5, 1, 0)
acc <- mean(preds == val_set$Survived)
cat("Validation accuracy:", round(acc,4), "\n")

test <- read.csv("src/data/test.csv")
test$Sex <- ifelse(test$Sex == "male", 0, 1)
test$Embarked[test$Embarked == ""] <- "S"
test$Embarked <- as.numeric(factor(test$Embarked))
test$Age[is.na(test$Age)] <- median(train$Age, na.rm = TRUE)
test$Fare[is.na(test$Fare)] <- median(train$Fare, na.rm = TRUE)

cat("Predictions for test set completed. Sample output:\n")
print(head(ifelse(predict(model, test[,features], type="response")>0.5,1,0)))
