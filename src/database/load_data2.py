import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# ==========================
# Load Environment Variables
# ==========================
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

# ==========================
# Load Processed Dataset
# ==========================
df = pd.read_csv(
    "data/processed/flight_features.csv"
)

print(f"Dataset Shape: {df.shape}")

# ==========================
# Data Type Conversions
# ==========================

# Date
df["flight_date"] = pd.to_datetime(df["flight_date"])

# Time
df["crs_dep_time"] = pd.to_datetime(df["crs_dep_time"]).dt.time

# Timestamp
df["created_at"] = pd.to_datetime(df["created_at"])

# Boolean
df["cancelled"] = df["cancelled"].astype(bool)
df["diverted"] = df["diverted"].astype(bool)

# ==========================
# Import to NeonDB
# ==========================

try:

    df.to_sql(
        name="flights",
        con=engine,
        if_exists="append",
        index=False,
        method="multi",
        chunksize=5000
    )

    print("===================================")
    print("✅ Data Imported Successfully!")
    print("===================================")

except Exception as e:

    print("===================================")
    print("❌ Import Failed")
    print("===================================")

    print(e)