# 🛍️ Customer Segmentation using RFM Analysis

## Project Overview
This project applies **RFM (Recency, Frequency, Monetary) Analysis** to segment customers based on their purchasing behavior.  
RFM is a widely used technique in marketing analytics to identify valuable customers, improve retention strategies, and support data-driven business decisions.

The analysis helps answer key business questions such as:
- Who are the most valuable customers?
- Which customers are at risk of churn?
- How should marketing strategies differ across customer groups?

---

## Dataset
- **Name:** Online Retail Dataset
- **Source:** Kaggle
- **Description:** Transaction-level data from a UK-based online retail store, including invoices, products, quantities, prices, and customer IDs.

---

## Methodology

### 1️⃣ Data Cleaning & Preparation
- Removed missing values and duplicate records
- Converted invoice dates to datetime format
- Created `TotalPrice = Quantity × UnitPrice`
- Filtered out customers with zero monetary value

---

### 2️⃣ RFM Feature Engineering
For each customer:
- **Recency:** Days since last purchase
- **Frequency:** Number of unique invoices
- **Monetary:** Total revenue generated

RFM scores were calculated using **quantile-based binning (1–5)**.

---

### 3️⃣ Customer Segmentation
Customers were grouped into meaningful business segments based on RFM scores:

| Segment Name | Description |
|--------------|-------------|
| Champions | Most valuable and loyal customers |
| Loyal Customers | Frequent and recent buyers |
| Frequent Buyers | High purchase frequency |
| Recent Customers | Recently active customers |
| At Risk | Customers likely to churn |
| Others | Average or mixed behavior |

---

## Visualizations
The project includes several visual analyses such as:
- Customer segment distribution
- Revenue contribution by segment
- Recency vs Frequency heatmap
- RFM score combination analysis
- Monetary value comparison across segments

All visualizations are saved inside the `images/` folder.

---

## Key Insights
- A small percentage of customers (Champions & Loyal Customers) contribute a large portion of total revenue
- At-risk customers represent a significant group that could be targeted with re-engagement campaigns
- RFM analysis provides clear, interpretable insights for business and marketing teams

---

## Tools & Libraries
- Python
- Pandas & NumPy
- Matplotlib & Seaborn
- Jupyter Notebook

---

## Kaggle Notebook
You can view the full interactive notebook on Kaggle here:  
👉 **[Kaggle Notebook Link – Click to Open](https://www.kaggle.com/code/esraamoh7med/customer-segmentation-with-rfm-analysis)**

---

## Conclusion
This project demonstrates how **RFM analysis** can be used to transform raw transactional data into actionable business insights.  
It highlights skills in data cleaning, feature engineering, customer analytics, and data visualization.

---
