**Early Warning System for Student Burnout & Dropout Risk**

**AI-Powered Behavioural Analytics Framework**

**Problem Statement**

Universities often detect academic decline only after performance drops
significantly. By that time, effective intervention becomes difficult.

This project builds an **AI-driven behavioural analytics system** that
predicts early signs of student burnout and dropout risk using
behavioural indicators such as LMS activity, attendance patterns,
assignment delays, and emotional sentiment.

The system provides:

-   Risk Score (0--100)

-   Risk Category (Low / Medium / High)

-   Key Behavioural Triggers

-   Recommended Intervention Strategy

-   Interactive Visualization Dashboard

**Project Objective**

To develop an early warning system that:

-   Detects behavioural disengagement patterns

-   Predicts burnout risk before academic failure

-   Provides explainable AI insights

-   Suggests proactive intervention strategies

**Dataset Information**

**Dataset Type:** Synthetic

**Why Synthetic?**

Real university LMS behavioural datasets are not publicly available due
to:

-   Student privacy regulations

-   Institutional data protection policies

-   Ethical and confidentiality constraints

Therefore, a realistic synthetic dataset was generated to simulate
behavioural patterns.

**Dataset Generation Process**

The dataset simulates realistic academic behaviour using statistical
distributions and behavioural rules.

**Number of Records:**

-   **2000 students**

**Number of Features:**

-   **7 behavioural indicators**

-   1 target variable (Burnout Risk Level)

**Feature Description**

  ---------------------------------------------------------------------------
  **Feature**                    **Description**      **Generation Logic**
  ------------------------------ -------------------- -----------------------
  LMS_Login_Frequency_Per_Week   Weekly LMS login     Normal distribution
                                 count                (Mean=5, SD=2)

  Assignment_Delay_Days          Delay in assignment  Poisson distribution
                                 submission           

  Attendance_Rate_Percentage     Class attendance     Uniform (60--100%)
                                 percentage           

  Study_Consistency_Index        Consistency in study Uniform (0--1)
                                 behaviour            

  Feedback_Sentiment_Score       Emotional tone from  Uniform (-1 to 1)
                                 feedback             

  CAT_Marks_Trend                Academic performance Uniform (-15 to 15)
                                 trend                

  Late_Night_Activity_Ratio      Irregular activity   Uniform (0--1)
                                 indicator            
  ---------------------------------------------------------------------------

**Risk Label Creation Logic**

Burnout Risk Level was assigned using behavioural thresholds:

**High Risk if:**

-   Attendance \< 70%

-   Significant decline in marks trend

-   High assignment delays

-   Negative feedback sentiment

**Medium Risk if:**

-   Moderate behavioural decline indicators

**Low Risk if:**

-   Stable behavioural and academic performance

**Model Selection**

**Model Used:** Random Forest Classifier

**Why Random Forest?**

-   Handles nonlinear behavioural relationships

-   Robust to noisy structured data

-   Provides feature importance for explainability

-   Performs well on classification problems

**Model Evaluation**

-   **Accuracy:** 98.75%

-   Precision, Recall, F1-Score

-   Confusion Matrix

-   Risk Score Probability Calibration

The high accuracy validates the strong relationship between behavioural
indicators and burnout risk.

**Behavioural Insights Derived**

Top Behavioural Triggers Identified:

1.  **CAT Marks Trend**

2.  **Attendance Rate**

3.  **Feedback Sentiment Score**

**Key Insight:**

Academic performance decline and attendance reduction are the strongest
early indicators of burnout risk. Emotional negativity also
significantly contributes to disengagement.

**Dashboard Features**

The interactive Streamlit dashboard includes:

-   Real-time Risk Prediction

-   Risk Score (0--100)

-   Downloadable Risk Report

-   Top 3 Behavioural Triggers

-   Feature Importance Visualization

-   Risk Distribution Overview

-   Automated Intervention Recommendation

**Technology Stack**

-   Python

-   Pandas

-   NumPy

-   Scikit-learn

-   Matplotlib

-   Streamlit

-   Joblib

**How to Run the Project**

**Install Dependencies**

pip install -r requirements.txt

**Run the Dashboard**

cd dashboard

streamlit run app.py

The application will open in your browser at:

http://localhost:8501

**Practical Feasibility**

This system can be integrated into:

-   University LMS platforms

-   Academic monitoring systems

-   Student counselling dashboards

-   Institutional risk analytics frameworks

It enables early intervention and data-driven student support.

**Future Enhancements**

-   Integration with real LMS APIs

-   Deep learning-based sentiment analysis

-   Time-series behavioural tracking

-   Automated faculty alert system

-   Deployment on cloud infrastructure

**Conclusion**

This project demonstrates how behavioural analytics combined with
machine learning can proactively identify student burnout risk and
enable timely institutional intervention.

It transforms reactive academic monitoring into a predictive
intelligence system.
