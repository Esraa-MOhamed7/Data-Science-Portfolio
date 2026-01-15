
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import confusion_matrix, classification_report
import pandas as pd
import streamlit as st
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
import joblib
try:
    data=pd.read_csv(r"E:\ML Projects\Alzheimer's Disease Dataset\alzheimers_disease_data.csv")
    print("done")
except FileNotFoundError:
    print("not found")
    exit()

X=data.drop(["DoctorInCharge","PatientID","Diagnosis"],axis=1)
y=data["Diagnosis"]
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)
model=GradientBoostingClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
joblib.dump(model,'alzheimer_GradientBoostingClassifier.joblib')
#print("done joblib")

st.title("Alzheimer's Risk Assessment Form")
st.sidebar.header("Feature Selecting ")
st.sidebar.info("Simple Appliction to Predicting Alzheimer Disease")
st.image("https://assets.delveinsight.com/blog/wp-content/uploads/2023/10/04173629/alzheimers-disease-diagnostics-market-analysis.webp")

# Create a dictionary of inputs
# 🎂 Demographics
age = st.slider("Age", min_value=60, max_value=90, value=75)
gender = st.radio("Gender", ["Male (0)", "Female (1)"])
ethnicity = st.slider("Ethnicity (0–3)", 0, 3, 1)
education = st.slider("Education Level (0–3)", 0, 3, 2)

# 🩺 Lifestyle & Health
bmi = st.slider("BMI", 15.0, 39.0, 22.0)
smoking = st.radio("Smoking", ["No (0)", "Yes (1)"])
alcohol = st.slider("Alcohol Consumption", 0.0, 19.9, 5.0)
physical_activity = st.slider("Physical Activity", 0.0, 9.9, 3.0)
diet_quality = st.slider("Diet Quality", 0.0, 9.99, 5.0)
sleep_quality = st.slider("Sleep Quality", 0.0, 9.99, 5.0)
family_history = st.radio("Family History of Alzheimer's", ["No (0)", "Yes (1)"])
heart_disease = st.radio("Cardiovascular Disease", ["No (0)", "Yes (1)"])
diabetes = st.radio("Diabetes", ["No (0)", "Yes (1)"])
depression = st.radio("Depression", ["No (0)", "Yes (1)"])
head_injury = st.radio("Head Injury", ["No (0)", "Yes (1)"])
hypertension = st.radio("Hypertension", ["No (0)", "Yes (1)"])
systolic_bp = st.slider("Systolic Blood Pressure", 90, 200, 120)
diastolic_bp = st.slider("Diastolic Blood Pressure", 60, 120, 80)
total_chol = st.slider("Total Cholesterol", 100.0, 300.0, 180.0)
ldl = st.slider("LDL Cholesterol", 50.0, 200.0, 120.0)
hdl = st.slider("HDL Cholesterol", 20.0, 100.0, 50.0)
triglycerides = st.slider("Triglycerides", 50.0, 300.0, 150.0)

# 🧠 Cognitive & Behavioral
mmse = st.slider("MMSE Score", 0, 30, 25)
functional_assessment = st.slider("Functional Assessment", 0.0, 9.9, 5.0)
memory_complaints = st.radio("Memory Complaints", ["No (0)", "Yes (1)"])
behavioral_problems = st.radio("Behavioral Problems", ["No (0)", "Yes (1)"])
adl = st.slider("ADL (Activities of Daily Living)", 0.0, 9.9, 5.0)
confusion = st.radio("Confusion", ["No (0)", "Yes (1)"])
disorientation = st.slider("Disorientation", 0.0, 9.9, 5.0)
personality_changes = st.radio("Personality Changes", ["No (0)", "Yes (1)"])
difficulty_tasks = st.radio("Difficulty Completing Tasks", ["No (0)", "Yes (1)"])
forgetfulness = st.radio("Forgetfulness", ["No (0)", "Yes (1)"])

data = {
    "Age": age,
    "Gender": int(gender.split("(")[-1][0]),
    "Ethnicity": ethnicity,
    "EducationLevel": education,
    "BMI": bmi,
    "Smoking": int(smoking.split("(")[-1][0]),
    "AlcoholConsumption": alcohol,
    "PhysicalActivity": physical_activity,
    "DietQuality": diet_quality,
    "SleepQuality": sleep_quality,
    "FamilyHistoryAlzheimers": int(family_history.split("(")[-1][0]),
    "CardiovascularDisease": int(heart_disease.split("(")[-1][0]),
    "Diabetes": int(diabetes.split("(")[-1][0]),
    "Depression": int(depression.split("(")[-1][0]),
    "HeadInjury": int(head_injury.split("(")[-1][0]),
    "Hypertension": int(hypertension.split("(")[-1][0]),
    "SystolicBP": systolic_bp,
    "DiastolicBP": diastolic_bp,
    "CholesterolTotal": total_chol,
    "CholesterolLDL": ldl,
    "CholesterolHDL": hdl,
    "CholesterolTriglycerides": triglycerides,
    "MMSE": mmse,
    "FunctionalAssessment": functional_assessment,
    "MemoryComplaints": int(memory_complaints.split("(")[-1][0]),
    "BehavioralProblems": int(behavioral_problems.split("(")[-1][0]),
    "ADL": adl,
    "Confusion": int(confusion.split("(")[-1][0]),
    "Disorientation": disorientation,
    "PersonalityChanges": int(personality_changes.split("(")[-1][0]),
    "DifficultyCompletingTasks": int(difficulty_tasks.split("(")[-1][0]),
    "Forgetfulness": int(forgetfulness.split("(")[-1][0])
}

input_df = pd.DataFrame([data])
if st.button("Predict"):
    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.error("High Risk Prediction")
        st.markdown("""
        Based on the information provided, the model suggests a higher risk of Alzheimer's disease.

        This result is not a medical diagnosis. Please consult a healthcare professional for further evaluation and personalized advice.
        """)
    else:
        st.success("Low Risk Prediction")
        st.markdown("""
        Based on the information provided, the model suggests a lower risk of Alzheimer's disease.

        This result does not replace medical advice. Regular checkups and healthy lifestyle habits are still recommended.
        """)

