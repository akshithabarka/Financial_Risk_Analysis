<<<<<<< HEAD
# Financial Risk Analysis System

## Project Overview

The Financial Risk Analysis System is an end-to-end Machine Learning project that predicts whether a loan application should be approved or rejected based on customer financial details.

This project uses:
- Machine Learning
- FastAPI
- Streamlit
- Scikit-learn

---

# Features

- Loan approval prediction
- Risk probability score
- FastAPI backend API
- Streamlit interactive frontend
- Machine Learning model pipeline
- Real-time predictions

---

# Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- FastAPI
- Streamlit
- Joblib

---

# Project Structure

```text
Financial-Risk-Analysis-System/
│
├── data/
│   └── loan_risk_prediction_dataset.csv
│
├── notebooks/
│   └── model_training.ipynb
│
├── model/
│   └── loan_model.pkl
│
├── backend/
│   └── app.py
│
├── frontend/
│   └── streamlit_app.py
│
├── requirements.txt
│
└── README.md
```

---

# Machine Learning Workflow

```text
Data Collection
      ↓
Data Cleaning
      ↓
EDA
      ↓
Feature Engineering
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Model Saving
      ↓
FastAPI Backend
      ↓
Streamlit Frontend
```

---

# Features Used

- Age
- Income
- LoanAmount
- CreditScore
- YearsExperience
- EmploymentType

---

# Model Used

- Random Forest Classifier

---

# Installation

## Step 1: Clone Repository

```bash
git clone <your-github-repo-link>
```

---

## Step 2: Create Virtual Environment

```bash
python -m venv venv
```

---

## Step 3: Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## Step 4: Install Requirements

```bash
pip install -r requirements.txt
```

---

# Run Backend

Go to backend folder:

```bash
cd backend
```

Run FastAPI server:

```bash
uvicorn app:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

Swagger API Docs:

```text
http://127.0.0.1:8000/docs
```

---

# Run Frontend

Open new terminal.

Go to frontend folder:

```bash
cd frontend
```

Run Streamlit app:

```bash
streamlit run streamlit_app.py
```

---

# API Endpoint

## Predict Loan Approval

```text
POST /predict
```

---

# Sample Input

```json
{
    "Age": 30,
    "Income": 85000,
    "LoanAmount": 20000,
    "CreditScore": 780,
    "YearsExperience": 5,
    "EmploymentType": "Employed"
}
```

---

# Sample Output

```json
{
    "prediction": "Approved",
    "probability": 0.95
}
```

---

# Future Improvements

- Add XGBoost model
- Add Authentication
- Deploy on Cloud
- Add Dashboard Visualizations
- Add Risk Analytics

---

# Resume Description

Developed an end-to-end Financial Risk Analysis System using Machine Learning to predict loan approval status. Built a Random Forest classification model with Scikit-learn, developed REST APIs using FastAPI, and created an interactive frontend using Streamlit for real-time predictions.

---

# Author

Bandi Brahmma Reddy
=======
# Financial_Risk_Analysis
>>>>>>> 7777238ead2c988b9d10ec6beefedf06b548281f
