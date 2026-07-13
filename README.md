# ✈ Flight Delay Prediction System

A Machine Learning-based web application that predicts whether a flight is likely to be delayed before departure using historical flight data, PostgreSQL, and a Random Forest Classifier.

---

## 📌 Project Overview

The Flight Delay Prediction System is designed to help passengers and airlines anticipate flight delays before departure. The application retrieves flight information from a PostgreSQL database and predicts whether the selected flight is likely to be delayed using a trained Machine Learning model.

The project also includes an Analytics Dashboard and Model Performance Dashboard for visualizing flight statistics and evaluating model performance.

---

## 🚀 Features

- 🔍 Search Flight by Flight Number
- ✈ View Flight Details
- 🤖 Predict Flight Delay
- 📊 Prediction Confidence Score
- 📈 Analytics Dashboard
- 📉 Model Performance Dashboard
- 🗄 PostgreSQL (NeonDB) Integration
- 🎨 Interactive Plotly Charts
- 🌐 Responsive Streamlit Web Application

---

## 🧠 Machine Learning

### Model Used

- Random Forest Classifier

### Workflow

Dataset

↓

Data Cleaning

↓

Feature Engineering

↓

Train-Test Split

↓

Random Forest Training

↓

Model Evaluation

↓

Save Pipeline (.pkl)

↓

Streamlit Deployment

---

## 📊 Model Performance

| Metric | Score |
|----------|--------|
| Accuracy | **71.01%** |
| Precision | **18.44%** |
| Recall | **50.97%** |
| F1 Score | **27.08%** |

### Confusion Matrix

| | Predicted On Time | Predicted Delayed |
|------|----------------|----------------|
| Actual On Time | 69,324 | 25,158 |
| Actual Delayed | 5,471 | 5,688 |

---

## 🗄 Database

Database Used:

- PostgreSQL (NeonDB)

Tables

- Flights

---

## 🛠 Tech Stack

### Frontend

- Streamlit

### Backend

- Python

### Database

- PostgreSQL
- SQLAlchemy

### Machine Learning

- Scikit-Learn
- Joblib

### Data Processing

- Pandas
- NumPy

### Visualization

- Plotly

---

## 📂 Project Structure

```text
Flight Delay Prediction/

│── app.py

│── requirements.txt

│── README.md

│

├── assets/

│      style.css

│

├── pages/

│      Analytics Dashboard

│      Model Performance

│      About Project

│

├── src/

│

│      database/

│      preprocessing/

│      models/

│      utils/

│      ui/
```

---

## ⚙ Installation

Clone the repository

```bash
git clone <repository-url>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📷 Screenshots

### Home Page

(Add Screenshot)

### Analytics Dashboard

(Add Screenshot)

### Model Performance

(Add Screenshot)

### About Project

(Add Screenshot)

---

## 🚀 Future Enhancements

- Real-Time Flight API
- Weather Integration
- SHAP Explainability
- Flight Route Visualization
- PDF Report Generation
- User Authentication
- Cloud Deployment

---

## 👨‍💻 Developer

**Dhruv Mittal**

MCA (Data Science)

Lovely Professional University

---

## ⭐ Acknowledgements

- Scikit-Learn
- Streamlit
- Plotly
- PostgreSQL
- SQLAlchemy