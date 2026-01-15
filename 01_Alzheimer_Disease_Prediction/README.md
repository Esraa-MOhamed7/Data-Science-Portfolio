


# Alzheimer’s Disease Prediction System 🧠

Alzheimer’s disease doesn’t only affect patients — it deeply impacts families, caregivers, and entire communities.  
Early detection can play a crucial role in slowing disease progression and improving quality of life.

This project focuses on building a machine learning system to predict Alzheimer’s disease using patient health and lifestyle data, and deploying it as an interactive web application.

---

## Problem Statement
Alzheimer’s disease is often diagnosed at advanced stages, where treatment options are limited.  
The goal of this project is to develop a classification model that assists in early detection using structured medical data.

---

## Dataset
- Source: Kaggle  
- Type: Structured medical & lifestyle dataset  
- Target Variable: Alzheimer’s Disease Diagnosis  

---

## Workflow
1. Data Cleaning & Handling Missing Values  
2. Exploratory Data Analysis (EDA)  
3. Feature Encoding & Scaling  
4. Model Training  
5. Model Evaluation  
6. Web Application Deployment using Streamlit  

---

## Models & Performance

| Model | Accuracy |
|------|----------|
| Logistic Regression | 0.81 |
| Random Forest | 0.94 |
| Gradient Boosting | **0.95** |
| XGBoost | 0.94 |

**Best Model:** Gradient Boosting  
**Precision / Recall / F1-score:** 0.95  

---

## Key Insights
- Ensemble models significantly outperformed traditional models.
- Gradient Boosting achieved the best balance between precision and recall.
- Proper feature engineering had a strong impact on model performance.

---

## Web Application
The trained model was deployed using **Streamlit**, allowing real-time interaction with predictions through a user-friendly interface.

---

## Project Links
- Notebook: [alzheimer.ipynb](https://www.kaggle.com/code/esraamoh7med/alzheimer-disease-prediction)
- Streamlit App Code: [app.py](https://github.com/Esraa-MOhamed7/Data-Science-Portfolio/blob/main/Alzheimer_Disease_Prediction/Alzheimer%20Prediction.py)
- Demo Video (LinkedIn): [Watch Here](https://www.linkedin.com/posts/esraa-mohamed-481545357_machinelearning-datascience-healthcareai-activity-7376625499814510596-FSTq?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFjkFGEBgOasy4Bn3a9eAU5i91fj7GZhNfQ)

