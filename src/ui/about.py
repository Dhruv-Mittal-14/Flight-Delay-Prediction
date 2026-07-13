import streamlit as st


def show_about():

    st.title("ℹ️ About Flight Delay Prediction System")

    st.write(
        """
        A Machine Learning based web application that predicts
        whether a flight is likely to be delayed before departure.
        """
    )

    st.divider()

    # -----------------------------------

    st.header("🎯 Project Objective")

    st.write("""
The objective of this project is to develop a Flight Delay Prediction
System capable of predicting whether a flight will be delayed before
departure using Machine Learning and historical flight information.

The application helps passengers and airlines make better decisions
by providing early delay predictions.
""")

    st.divider()

    # -----------------------------------

    st.header("📂 Dataset Information")

    c1, c2 = st.columns(2)

    with c1:

        st.info("""
Dataset Features

• Flight Number

• Airline

• Origin Airport

• Destination Airport

• Distance

• Departure Time

• Flight Duration

• Delay Status
""")

    with c2:

        st.info("""
Feature Engineering

• Day Name

• Departure Period

• Distance Category

• Flight Duration Category

• Weekend Flag

• Departure Hour

• Departure Minute
""")

    st.divider()

    # -----------------------------------

    st.header("⚙️ Technologies Used")

    tech = [
        "Python",
        "Streamlit",
        "Pandas",
        "NumPy",
        "Scikit-Learn",
        "PostgreSQL (NeonDB)",
        "SQLAlchemy",
        "Plotly",
        "Joblib"
    ]

    for t in tech:

        st.write("✅", t)

    st.divider()

    # -----------------------------------

    st.header("🤖 Machine Learning Pipeline")

    st.markdown("""
1. Data Collection

2. Data Cleaning

3. Feature Engineering

4. Encoding

5. Train-Test Split

6. Random Forest Training

7. Model Evaluation

8. Save Model (.pkl)

9. Streamlit Deployment
""")

    st.divider()

    # -----------------------------------

    st.header("📊 Project Features")

    st.success("""
✔ Search Flight by Flight Number

✔ Flight Details from PostgreSQL

✔ Delay Prediction

✔ Prediction Confidence

✔ Analytics Dashboard

✔ Model Performance Dashboard

✔ Interactive Charts

✔ Responsive Web Application
""")

    st.divider()

    # -----------------------------------

    st.header("🛠 Project Architecture")

    st.code("""
User

↓

Streamlit UI

↓

SQLAlchemy

↓

Neon PostgreSQL

↓

Machine Learning Pipeline

↓

Prediction Result
""")

    st.divider()

    # -----------------------------------

    st.header("🚀 Future Scope")

    st.write("""
• Real-Time Flight API Integration

• Live Weather Data

• Airline Recommendation

• Flight Route Visualization

• User Authentication

• Mobile Application

• Model Explainability (SHAP)

• Download Prediction Report

• Cloud Deployment
""")

    st.divider()

    # -----------------------------------

    st.header("👨‍💻 Developer")

    st.success("""
Name : Dhruv Mittal

Course : MCA (Data Science)

University : Lovely Professional University

Project : Flight Delay Prediction System
""")