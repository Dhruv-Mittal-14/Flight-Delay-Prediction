import streamlit as st
import pandas as pd
import plotly.express as px


def show_model_performance():

    st.title("🤖 Machine Learning Model Performance")

    st.write(
        """
        This page displays the evaluation metrics of the trained
        Random Forest Classifier used for flight delay prediction.
        """
    )

    st.divider()

    # ------------------------------------
    # Metrics
    # ------------------------------------

    accuracy = 71.01
    precision = 18.44
    recall = 50.97
    f1 = 27.08

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Accuracy",
        f"{accuracy:.2f}%"
    )

    c2.metric(
        "Precision",
        f"{precision:.2f}%"
    )

    c3.metric(
        "Recall",
        f"{recall:.2f}%"
    )

    c4.metric(
        "F1 Score",
        f"{f1:.2f}%"
    )

    st.divider()

    # ------------------------------------
    # Metric Comparison
    # ------------------------------------

    st.subheader("📊 Evaluation Metrics")

    metrics = pd.DataFrame({

        "Metric": [

            "Accuracy",
            "Precision",
            "Recall",
            "F1 Score"

        ],

        "Score": [

            accuracy,
            precision,
            recall,
            f1

        ]

    })

    fig = px.bar(

        metrics,

        x="Metric",

        y="Score",

        color="Metric",

        text="Score",

        template="plotly_dark"

    )

    fig.update_layout(

        height=450,

        showlegend=False

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.divider()

    # ------------------------------------
    # Confusion Matrix
    # ------------------------------------

    st.subheader("📉 Confusion Matrix")

    confusion = pd.DataFrame(

        [

            [69324,25158],

            [5471,5688]

        ],

        columns=["Predicted On Time","Predicted Delayed"],

        index=["Actual On Time","Actual Delayed"]

    )

    st.dataframe(

        confusion,

        use_container_width=True

    )

    st.divider()

    # ------------------------------------
    # Classification Report
    # ------------------------------------

    st.subheader("📄 Classification Report")

    report = pd.DataFrame({

        "Class":[

            "On Time",

            "Delayed"

        ],

        "Precision":[

            0.93,

            0.18

        ],

        "Recall":[

            0.73,

            0.51

        ],

        "F1 Score":[

            0.82,

            0.27

        ],

        "Support":[

            94482,

            11159

        ]

    })

    st.dataframe(

        report,

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    # ------------------------------------
    # Model Information
    # ------------------------------------

    st.subheader("🧠 Model Information")

    left,right = st.columns(2)

    with left:

        st.info("""

Model

• Random Forest Classifier

• Binary Classification

• Scikit-learn

• Saved using Joblib

""")

    with right:

        st.info("""

Evaluation Dataset

• Test Samples : 105,641

• Features : 17

• Target : Delay Status

""")

    st.divider()

    # ------------------------------------
    # Interpretation
    # ------------------------------------

    st.subheader("📌 Interpretation")

    st.success("""

✔ The model correctly predicts approximately **71%** of all flights.

✔ Recall is around **51%**, indicating that the model identifies about half of the delayed flights.

✔ Lower precision reflects the class imbalance present in the dataset.

✔ Random Forest was selected because it performed better than the baseline models evaluated during experimentation.

""")