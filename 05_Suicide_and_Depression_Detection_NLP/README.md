# 🧠 Suicide & Depression Detection using NLP

Mental health struggles often go unseen — and behind every message, there may be someone silently asking for help.  
This project aims to leverage **Natural Language Processing (NLP)** to detect suicidal and non-suicidal expressions from text, helping highlight the potential of AI in mental health awareness and early intervention.

---

## Project Overview

In this project, I built a **text classification system** that analyzes written content and predicts whether it expresses suicidal intent or not.  
The model was trained on a large real-world dataset and later deployed as a **Web Application** for real-time interaction.

---

## Dataset

- **Name:** Suicide and Depression Detection  
- **Source:** Kaggle  
- **Size:** 230k+ text samples  
- **Classes:** Suicide / Non-Suicide (Balanced)

---

##  Workflow

1. **Data Exploration**
   - Class balance analysis
   - Text length distribution
   - Vocabulary analysis

2. **Text Analysis**
   - Word frequency analysis
   - Word clouds per class
   - Linguistic pattern comparison

3. **Modeling & Evaluation**
   - TF-IDF Vectorization
   - Linear SVM
   - Logistic Regression
   - Multinomial Naive Bayes

4. **Model Selection**
   - Best model saved for deployment

---

## Results

| Model | Accuracy | Macro F1 |
|-----|---------|----------|
| TF-IDF + Linear SVM | **95%** | **0.95** |
| TF-IDF + Logistic Regression | 94.6% | 0.94 |
| TF-IDF + Naive Bayes | 86% | 0.86 |

**Linear SVM delivered the best overall performance** and was used in deployment.

---

## Web Application

The trained model was deployed as a simple web application that allows users to input text and receive predictions in real time.

🔗 **Web App:** [Try App](https://suicide-and-depression-detection-akexq8pvnrrubkbgjajgkt.streamlit.app/)

---

## Notebook

🔗 **Kaggle Notebook:** [Kaggle Notebook Link – Click to Open](https://www.kaggle.com/code/esraamoh7med/from-words-to-warnings-suicide-depression)

---

## Key Takeaway

This project demonstrates how NLP and machine learning can be applied responsibly to sensitive domains like mental health, emphasizing the importance of ethical AI and human-centered design.

---

## Tools & Technologies

- Python
- Pandas & NumPy
- Scikit-learn
- TF-IDF
- NLP Pipelines
- Streamlit (Web App)

