# 🔋 Energy Consumption Forecasting (Time Series)

Accurate energy demand forecasting plays a crucial role in ensuring power grid stability, reducing operational costs, and supporting sustainable energy planning.

In this project, I built a complete **Time Series Forecasting pipeline** to predict hourly electricity consumption using historical demand data from the PJME region.

---

## Project Overview

- **Problem Type:** Time Series Forecasting  
- **Target Variable:** Hourly Energy Consumption (MW)  
- **Dataset Size:** 145,000+ hourly records  
- **Data Source:** Kaggle – PJME Hourly Energy Consumption  

---

## Workflow

### 1️⃣ Data Exploration & Cleaning
- Converted timestamps to datetime format
- Set datetime as index
- Ensured data consistency with no missing values

### 2️⃣ Feature Engineering
Extracted time-based and lag features to capture seasonality and temporal patterns:
- Year, Quarter, Month, Day of Week, Hour
- Weekend indicator
- Lag features (t-1, t-24)
- Rolling statistics (24-hour mean & standard deviation)

### 3️⃣ Exploratory Data Analysis
- Analyzed consumption trends over years
- Studied seasonality by month, quarter, and hour
- Visualized demand distribution across time components

### 4️⃣ Modeling & Forecasting
Trained and compared multiple regression models:
- Linear Regression
- Ridge Regression
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor

### 5️⃣ Evaluation Metrics
Models were evaluated using:
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R² Score

---

## Results

| Model | RMSE | R² |
|------|------|----|
| XGBoost | 596.12 | 0.991 |
| Random Forest | 607.90 | 0.991 |
| Gradient Boosting | 849.84 | 0.983 |
| Ridge Regression | 1362.83 | 0.955 |
| Linear Regression | 1362.83 | 0.955 |

 **XGBoost achieved the best performance**, demonstrating the strength of ensemble models in time series forecasting tasks.

---

## Web Application
An interactive **Streamlit Web App** was developed to visualize energy consumption trends and generate real-time predictions.

---

## 🔗 Project Links
- Kaggle Notebook: [View Notebook](https://www.kaggle.com/code/esraamoh7med/alzheimer-disease-prediction)
- Web App Demo: [Try the App](https://hourly-energy-demand-forecasting-rubwwegrx7zehfdbaqpc6q.streamlit.app/)

##  Tech Stack
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- XGBoost
- Streamlit

---

## Key Takeaways
- Time-based features and lag variables significantly improve forecasting accuracy
- Tree-based ensemble models outperform linear models for complex temporal patterns
- Proper time-aware train-test splitting is essential in time series problems


