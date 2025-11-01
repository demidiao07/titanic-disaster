# 🛳️ Titanic Disaster Survival Prediction  
**Northwestern University – MLDS 400: Introduction to Data Engineering**  
**Author:** *Demi Diao*  

This repository demonstrates how to build reproducible **Python** and **R** environments using **Docker** to predict passenger survival aboard the Titanic using logistic regression.  
Both containers load, process, and model the Titanic dataset to produce survival predictions.

---
## 📁 Repository Structure
```markdown
titanic-disaster/
│
├── src/
│ ├── data/ # Empty folder (place Kaggle data here)
│ ├── python_app/ # Python implementation
│ │ ├── Dockerfile
│ │ ├── requirements.txt
│ │ └── titanic_model.py
│ └── r_app/ # R implementation
│ ├── Dockerfile
│ ├── install_packages.R
│ └── titanic_model.R
│
├── .gitignore
└── README.md
```

---

## 🧩 1. Download the Titanic Dataset
1. Visit the official [Kaggle Titanic dataset page](https://www.kaggle.com/c/titanic/data).  
2. Download the following files:
   - `train.csv`
   - `test.csv`
3. Place them in the folder:
```yaml
src/data/
```
The structure should now look like:
```vbent
src/data/train.csv
src/data/test.csv
```
---

## 🐍 2. Run the Python Docker Container

### 🧱 Build the image
From the project root, run:
```bash
docker build -t titanic-python -f src/python_app/Dockerfile .
```

#### ▶️ Run the container: docker run --rm titanic-python
#### 🧾 Expected output: 
```yaml
Loading Titanic training data...
Data loaded successfully!
Data preview:
   PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
1            2         1       1  ...  71.2833   C85         C
2            3         1       3  ...   7.9250   NaN         S
3            4         1       1  ...  53.1000  C123         S
4            5         0       3  ...   8.0500   NaN         S

[5 rows x 12 columns] 

Basic info:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  891 non-null    int64  
 1   Survived     891 non-null    int64  
 2   Pclass       891 non-null    int64  
 3   Name         891 non-null    object 
 4   Sex          891 non-null    object 
 5   Age          714 non-null    float64
 6   SibSp        891 non-null    int64  
 7   Parch        891 non-null    int64  
 8   Ticket       891 non-null    object 
 9   Fare         891 non-null    float64
 10  Cabin        204 non-null    object 
 11  Embarked     889 non-null    object 
dtypes: float64(2), int64(5), object(5)
memory usage: 83.7+ KB
None 

Missing values per column:
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64 

Cleaning and preparing data...
Training Logistic Regression model...
Model trained successfully!

Training Accuracy: 0.8006
Validation Accuracy: 0.8101

Loading test dataset...
Making predictions on test dataset...
Sample predictions (PassengerId → Survived):
892: 0
893: 0
894: 0
895: 0
896: 1
897: 0
898: 1
899: 0
900: 1
901: 0

Prediction complete! Titanic model finished successfully.
```

## 📊 3. Run the R Docker Container
### 🧱 Build the image
```bash
docker build -t titanic-r -f src/r_app/Dockerfile .
```
### ▶️ Run the container
```bash
docker run --rm titanic-r
```

### 🧾 Expected output
```yaml
Data loaded successfully!
Data preview:
  PassengerId Survived Pclass
1           1        0      3
2           2        1      1
3           3        1      3
4           4        1      1
5           5        0      3
                                                 Name    Sex Age SibSp Parch
1                             Braund, Mr. Owen Harris   male  22     1     0
2 Cumings, Mrs. John Bradley (Florence Briggs Thayer) female  38     1     0
3                              Heikkinen, Miss. Laina female  26     0     0
4        Futrelle, Mrs. Jacques Heath (Lily May Peel) female  35     1     0
5                            Allen, Mr. William Henry   male  35     0     0
            Ticket    Fare Cabin Embarked
1        A/5 21171  7.2500              S
2         PC 17599 71.2833   C85        C
3 STON/O2. 3101282  7.9250              S
4           113803 53.1000  C123        S
5           373450  8.0500              S

Basic info:
'data.frame':   891 obs. of  12 variables:
 $ PassengerId: int  1 2 3 4 5 6 7 8 9 10 ...
 $ Survived   : int  0 1 1 1 0 0 0 0 1 1 ...
 $ Pclass     : int  3 1 3 1 3 3 1 3 3 2 ...
 $ Name       : chr  "Braund, Mr. Owen Harris" "Cumings, Mrs. John Bradley (Florence Briggs Thayer)" "Heikkinen, Miss. Laina" "Futrelle, Mrs. Jacques Heath (Lily May Peel)" ...
 $ Sex        : chr  "male" "female" "female" "female" ...
 $ Age        : num  22 38 26 35 35 NA 54 2 27 14 ...
 $ SibSp      : int  1 1 0 1 0 0 0 3 0 1 ...
 $ Parch      : int  0 0 0 0 0 0 0 1 2 0 ...
 $ Ticket     : chr  "A/5 21171" "PC 17599" "STON/O2. 3101282" "113803" ...
 $ Fare       : num  7.25 71.28 7.92 53.1 8.05 ...
 $ Cabin      : chr  "" "C85" "" "C123" ...
 $ Embarked   : chr  "S" "C" "S" "S" ...

Missing values per column:
PassengerId    Survived      Pclass        Name         Sex         Age 
          0           0           0           0           0         177 
      SibSp       Parch      Ticket        Fare       Cabin    Embarked 
          0           0           0           0           0           0 

🔧 Cleaning and preparing data...

Training logistic regression model...
Model trained successfully!
Training Accuracy: 0.8062
Validation Accuracy: 0.7598

Loading test dataset...

Making predictions on test dataset...
Sample predictions (PassengerId → Survived):
   PassengerId Survived_Pred
1          892             0
2          893             0
3          894             0
4          895             0
5          896             1
6          897             0
7          898             1
8          899             0
9          900             1
10         901             0

Prediction complete! Titanic model finished successfully.
```
## ✨ Conclusion
This project demonstrates a complete data engineering workflow from environment setup, data loading, and cleaning to model training and deployment in both Python and R.
