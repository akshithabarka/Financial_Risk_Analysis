from fastapi import FastAPI
from pydantic import BaseModel

import pandas as pd
import joblib

# Create app
app = FastAPI()

# Load model
model = joblib.load("../model/loan_model.pkl")


# Input schema
class LoanData(BaseModel):

    Age: int
    Income: float
    LoanAmount: float
    CreditScore: float
    YearsExperience: int
    EmploymentType: str


# Home route
@app.get("/")
def home():

    return {
        "message": "Financial Risk Analysis API"
    }


# Prediction route
@app.post("/predict")
def predict(data: LoanData):

    input_data = pd.DataFrame([data.dict()])

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]

    result = "Approved" if prediction == 1 else "Rejected"

    return {
        "prediction": result,
        "probability": float(probability)
    }