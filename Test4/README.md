# Insurance Charges Prediction Using Supervised Machine Learning

## Project Title
- Insurance Charges Prediction Using Supervised Machine Learning

## Problem Statement
- The goal of this project is to predict insurance charges for individuals based on demographic and health-related features using supervised machine learning algorithms.

## Dataset Description
- **Source:** Insurance dataset (`insurance.csv`)  
- **Number of rows:** 1338  
- **Columns:**
  - `age` – Age of the policyholder
  - `sex` – Gender (male/female)
  - `bmi` – Body Mass Index
  - `children` – Number of children
  - `smoker` – Whether the person smokes (yes/no)
  - `region` – Geographical region (northeast, northwest, southeast, southwest)
  - `charges` – Insurance charges (target variable)

## Data Cleaning & Preprocessing
- Missing values: The `bmi` column had 3 missing values, imputed with the mean.
- Duplicates: Removed any duplicate rows (if present).
- Outliers: Outliers in `charges` were treated using the IQR method.
- Categorical variables: `sex`, `smoker`, and `region` were one-hot encoded.
- Feature scaling: Applied standardization to numerical features.
- Target transformation: `charges` was log-transformed to reduce skewness.
- Train-test split: Dataset split into 80% training and 20% testing data.

## Algorithms Used
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- K-Nearest Neighbors Regressor
- Support Vector Regressor (SVR)

## Evaluation Metrics
- R² (Coefficient of Determination)
- Accuracy (%) — R² converted to percentage
- MSE (Mean Squared Error)
- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)

## Model Performance

| Model | Accuracy (%) | R² | MSE | RMSE | MAE |
|-------|--------------|----|-----|------|-----|
| Linear Regression | 80.9 | 0.809 | 0.160 | 0.400 | 0.263 |
| Decision Tree | 69.8 | 0.698 | 0.253 | 0.503 | 0.215 |
| Random Forest | 82.6 | 0.826 | 0.146 | 0.382 | 0.193 |
| K-Nearest Neighbors | 82.0 | 0.820 | 0.151 | 0.388 | 0.244 |
| Support Vector Regressor (SVR) | 87.7 | 0.877 | 0.103 | 0.321 | 0.150 |

## Conclusion / Observations
- **Best model:** Support Vector Regressor (SVR) achieved the highest accuracy (**87.7%**) and lowest errors.
- Non-linear and ensemble methods (SVR, Random Forest, KNN) outperformed Linear Regression and single Decision Tree.
- Feature scaling and target transformation improved model performance.
