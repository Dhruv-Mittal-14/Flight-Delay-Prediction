import sys
from pathlib import Path

# Add src folder to Python path
sys.path.append(str(Path(__file__).resolve().parents[1]))



import pandas as pd
from database.db_connection import get_engine

engine = get_engine()

query = "SELECT * FROM raw_flights;"

df = pd.read_sql(query, engine)

print(df.head())

print("///////////////////////////////////////")
print("\n\n")


print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nSummary Statistics:")
print(df.describe())


#Target Variable

df["delay_status"] = df["arr_delay"].apply(
    lambda x: 1 if x > 15 else 0
)



df.to_csv(
    "data/processed/clean_flights.csv",
    index=False
)

print(df.columns.tolist())