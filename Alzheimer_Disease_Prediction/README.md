# 🧠 Alzheimer's Disease Prediction

## Problem Statement
Alzheimer’s Disease is not only a medical condition but a life-changing challenge for patients and their families. Early detection can play a crucial role in improving care, planning, and quality of life.

The goal of this project is to build a machine learning–based classification system that predicts the likelihood of Alzheimer’s Disease using clinical and lifestyle data. To make the solution more accessible, the model was deployed as an interactive web application for real-time predictions.

## Dataset
- Source: Kaggle
- Samples: 2,149
- Features: 35
- Target Variable: Diagnosis (Binary Classification)

## Models Used
- Logistic Regression
- Random Forest
- Gradient Boosting
- XGBoost

## Results
| Model | Accuracy |
|------|----------|
| Logistic Regression | 0.81 |
| Random Forest | 0.94 |
| Gradient Boosting | **0.95** |
| XGBoost | 0.94 |

Gradient Boosting achieved the best overall performance with Precision, Recall, and F1-score of 0.95.

## Web Application
The model was deployed using Streamlit, allowing users to input patient information and receive real-time predictions.

## Links
- Kaggle Notebook: [View Notebook](https://www.kaggle.com/code/esraamoh7med/alzheimer-disease-prediction)
- Web App Demo: [Try the App](https://alzheimer-prediction-app-ntgegk9kgzxqx8ku5yamgu.streamlit.app/)

