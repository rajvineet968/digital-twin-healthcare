import joblib
import pandas as pd

# Load models
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

heart_model = joblib.load(os.path.join(BASE_DIR, "models/heart.pkl"))
diabetes_model = joblib.load(os.path.join(BASE_DIR, "models/diabetes.pkl"))
kidney_model = joblib.load(os.path.join(BASE_DIR, "models/kidney.pkl"))

# Load encoders
heart_encoders = joblib.load(os.path.join(BASE_DIR, "models/heart_encoders.pkl"))
kidney_encoders = joblib.load(os.path.join(BASE_DIR, "models/kidney_encoders.pkl"))


# ---------------------------
# Feature mapping
# ---------------------------
HEART_FEATURES = [
    'age','sex','cp','trestbps','chol','fbs','restecg',
    'thalch','exang','oldpeak','slope','ca','thal'
]

DIABETES_FEATURES = [
    'Pregnancies','Glucose','BloodPressure','SkinThickness',
    'Insulin','BMI','DiabetesPedigreeFunction','Age'
]

KIDNEY_FEATURES = [
    col for col in kidney_model.feature_names_in_
]


# ---------------------------
# Encode helper
# ---------------------------
def apply_encoders(data, encoders):
    for col, encoder in encoders.items():
        if col in data:
            try:
                data[col] = encoder.transform([str(data[col])])[0]
            except:
                data[col] = 0
    return data


# ---------------------------
# MAIN FUNCTION
# ---------------------------
def predict_all(input_data: dict):

    # ---- HEART ----
    heart_data = {k: input_data.get(k, 0) for k in HEART_FEATURES}
    heart_data = apply_encoders(heart_data, heart_encoders)

    heart_df = pd.DataFrame([heart_data])
    heart_pred = heart_model.predict(heart_df)[0]

    # ---- DIABETES ----
    diabetes_data = {k: input_data.get(k, 0) for k in DIABETES_FEATURES}
    diabetes_df = pd.DataFrame([diabetes_data])
    diabetes_pred = diabetes_model.predict(diabetes_df)[0]

    # ---- KIDNEY ----
    kidney_data = {k: input_data.get(k, 0) for k in KIDNEY_FEATURES}
    kidney_data = apply_encoders(kidney_data, kidney_encoders)

    kidney_df = pd.DataFrame([kidney_data])
    kidney_pred = kidney_model.predict(kidney_df)[0]

    return {
        "heart_risk": int(heart_pred),
        "diabetes_risk": int(diabetes_pred),
        "kidney_risk": int(kidney_pred)
    }