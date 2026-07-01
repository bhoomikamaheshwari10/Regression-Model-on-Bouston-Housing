# 🏠 Boston Housing Price Prediction using Linear & Polynomial Regression

## 📌 Project Overview

This project predicts house prices using the Boston Housing dataset. It demonstrates the complete machine learning workflow, including data preprocessing, exploratory data analysis (EDA), feature engineering, model training, evaluation, and model serialization using Python and Scikit-learn.

Two regression models are implemented and compared:

- Linear Regression
- Polynomial Regression (Degree = 2)

The project also compares both models using evaluation metrics and visualization.

---

## 🚀 Features

- Data Exploration (EDA)
- Missing Value Check
- Duplicate Value Detection
- Correlation Analysis
- Outlier Detection & Removal using IQR
- Train-Test Split
- Feature Standardization
- Linear Regression
- Polynomial Regression
- Model Evaluation using R² Score
- Actual vs Predicted Visualization
- Model Comparison
- Save Trained Model using Pickle

---

## 📂 Dataset

The project uses the **Boston Housing Dataset** containing housing-related features such as:

- CRIM
- ZN
- INDUS
- CHAS
- NOX
- RM
- AGE
- DIS
- RAD
- TAX
- PTRATIO
- B
- LSTAT

### Target Variable

- **MEDV** – Median value of owner-occupied homes

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Pickle

---

## 📊 Project Workflow

### 1. Import Libraries

Imported required Python libraries for data analysis and machine learning.

### 2. Data Exploration

- View dataset
- Dataset shape
- Statistical summary
- Missing value analysis
- Duplicate detection

### 3. Correlation Analysis

Correlation matrix was used to identify relationships between features and the target variable.

The **RM** feature showed a strong positive correlation with house price.

### 4. Outlier Removal

Outliers from the **RM** feature were removed using the **Interquartile Range (IQR)** method.

### 5. Data Preprocessing

- Separate features and target
- Train-Test Split
- Feature Standardization using `StandardScaler`

### 6. Model Training

#### Linear Regression

A baseline Linear Regression model was trained.

#### Polynomial Regression

Polynomial Features (Degree = 2) were generated to capture nonlinear relationships before training another Linear Regression model.

### 7. Model Evaluation

Models were evaluated using:

- R² Score
- Actual vs Predicted plots

### 8. Model Serialization

The trained model was saved using Pickle for future deployment.

---

## 📈 Results

The project compares:

- Training R² Score
- Testing R² Score
- Actual vs Predicted Scatter Plot

to evaluate the performance of both models.

---


## ▶️ How to Run

### Clone Repository

```bash
git clone https://github.com/bhoomikamaheshwari10/Regression-Model-on-Bouston-Housing.git
```

### Install Dependencies

```bash
pip install pandas numpy matplotlib scikit-learn
```

### Run Notebook

```bash
jupyter notebook Bouston.ipynb
```

---

## 💾 Saving the Model

```python
import pickle

pickle.dump(model, open("regmodel.pkl", "wb"))
```

Load the model:

```python
import pickle

model = pickle.load(open("regmodel.pkl", "rb"))
```

---

## 📌 Future Improvements

- Ridge Regression
- Lasso Regression
- Random Forest Regressor
- XGBoost Regressor
- Hyperparameter Tuning using GridSearchCV

---

## 📚 Skills Demonstrated

- Exploratory Data Analysis (EDA)
- Feature Engineering
- Outlier Handling
- Standardization
- Regression Modeling
- Polynomial Features
- Model Evaluation
- Data Visualization
- Model Serialization

---
