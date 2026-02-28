import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import joblib

from sklearn.preprocessing import LabelEncoder

# -----------------------------
# Load Dataset (Correct Path)
# -----------------------------
df = pd.read_csv("data/synthetic_student_burnout_data.csv")

# Encode target
le = LabelEncoder()
df["Burnout_Risk_Level"] = le.fit_transform(df["Burnout_Risk_Level"])

X = df.drop("Burnout_Risk_Level", axis=1)
y = df["Burnout_Risk_Level"]

# -----------------------------
# Load Pre-Trained Model
# -----------------------------
model = joblib.load("dashboard/burnout_model.pkl")

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="EduPulse Dashboard", layout="wide")

st.title("Early Detection of Student Burnout & Dropout Risk")
st.write("AI-Powered Early Warning System Using Behavioural Analytics")

# -----------------------------
# Sidebar Inputs
# -----------------------------
st.sidebar.header("Enter Student Details")

student_id = st.sidebar.text_input("Student ID")

lms = st.sidebar.slider("LMS Login Frequency (per week)", 0, 12, 5)
delay = st.sidebar.slider("Assignment Delay (days)", 0, 10, 2)
attendance = st.sidebar.slider("Attendance Rate (%)", 50, 100, 80)
consistency = st.sidebar.slider("Study Consistency (0-1)", 0.0, 1.0, 0.5)
sentiment = st.sidebar.slider("Feedback Sentiment (-1 to 1)", -1.0, 1.0, 0.0)
marks_trend = st.sidebar.slider("CAT Marks Trend (-15 to 15)", -15.0, 15.0, 0.0)
late_night = st.sidebar.slider("Late Night Activity Ratio (0-1)", 0.0, 1.0, 0.3)

input_data = np.array([[lms, delay, attendance, consistency,
                        sentiment, marks_trend, late_night]])

# -----------------------------
# Prediction Section
# -----------------------------
if st.button("Predict Risk"):

    prob = model.predict_proba(input_data)
    risk_score = np.max(prob) * 100
    risk_label = le.inverse_transform(model.predict(input_data))[0]

    st.subheader(" Risk Assessment Result")

    # Animated progress bar
    progress_bar = st.progress(0)
    for i in range(int(risk_score)):
        time.sleep(0.01)
        progress_bar.progress(i + 1)

    st.write("Risk Score:", round(risk_score, 2))
    st.write("Risk Category:", risk_label)

    # Intervention Logic
    if risk_label == "High":
        intervention = "Immediate counselling + Faculty alert + Weekly monitoring"
        st.error(" High Risk - Immediate Intervention Required")
    elif risk_label == "Medium":
        intervention = "Send academic reminders + Peer mentoring suggestion"
        st.warning(" Medium Risk - Monitor and Support")
    else:
        intervention = "Stable performance - No immediate intervention needed"
        st.success(" Low Risk - Student is Stable")

    # -----------------------------
    # Top 3 Behavioural Triggers
    # -----------------------------
    st.subheader(" Top 3 Behavioural Triggers")

    importance = model.feature_importances_
    feature_df = pd.DataFrame({
        "Feature": X.columns,
        "Importance": importance
    }).sort_values(by="Importance", ascending=False)

    top3 = feature_df.head(3)

    for index, row in top3.iterrows():
        st.write(f"{row['Feature']} (Importance: {round(row['Importance'],3)})")

    # -----------------------------
    # Downloadable Report
    # -----------------------------
    report = pd.DataFrame({
        "Student_ID": [student_id],
        "Risk_Score": [round(risk_score, 2)],
        "Risk_Category": [risk_label],
        "Intervention_Recommendation": [intervention]
    })

    csv = report.to_csv(index=False).encode("utf-8")

    st.download_button(
        label=" Download Risk Report",
        data=csv,
        file_name=f"{student_id}_risk_report.csv",
        mime="text/csv"
    )

# -----------------------------
# Feature Importance Chart
# -----------------------------
st.subheader(" Feature Importance Overview")

importance = model.feature_importances_
features = X.columns

fig = plt.figure()
plt.barh(features, importance)
plt.xlabel("Importance Score")
plt.title("Behavioural Trigger Importance")
st.pyplot(fig)

# -----------------------------
# Risk Distribution Chart
# -----------------------------
st.subheader(" Dataset Risk Distribution")

risk_counts = df["Burnout_Risk_Level"].value_counts().sort_index()

fig2 = plt.figure()
plt.bar(["Low", "Medium", "High"], risk_counts)
plt.title("Burnout Risk Distribution")
st.pyplot(fig2)