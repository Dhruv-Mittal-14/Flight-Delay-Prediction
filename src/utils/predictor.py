import joblib
import pandas as pd
from pathlib import Path

# Folder containing predictor.py
CURRENT_DIR = Path(__file__).resolve().parent

# Go to project root
PROJECT_ROOT = CURRENT_DIR.parent.parent

# Model path
MODEL_PATH = PROJECT_ROOT / "src" / "models" / "flight_delay_pipeline.pkl"

print("PROJECT ROOT:", PROJECT_ROOT)
print("MODEL PATH:", MODEL_PATH)
print("MODEL EXISTS:", MODEL_PATH.exists())

pipeline = joblib.load(MODEL_PATH)


def predict_delay(flight):

    input_df = pd.DataFrame([{
        "marketing_airline_network": flight["marketing_airline_network"],
        "origin": flight["origin"],
        "dest": flight["dest"],
        "distance": flight["distance"],
        "crs_elapsed_time": flight["crs_elapsed_time"],
        "cancelled": flight["cancelled"],
        "diverted": flight["diverted"],
        "day": flight["day"],
        "day_name": flight["day_name"],
        "day_of_week": flight["day_of_week"],
        "is_weekend": flight["is_weekend"],
        "departure_hour": flight["departure_hour"],
        "departure_minute": flight["departure_minute"],
        "departure_period": flight["departure_period"],
        "distance_category": flight["distance_category"],
        "flight_duration_minutes": flight["flight_duration_minutes"],
        "duration_category": flight["duration_category"]
    }])

    prediction = pipeline.predict(input_df)[0]
    probability = pipeline.predict_proba(input_df)[0][1]

    return prediction, probability