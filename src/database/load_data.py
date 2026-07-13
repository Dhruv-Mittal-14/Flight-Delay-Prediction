import pandas as pd
from sqlalchemy import text
from db_connection import get_engine

engine = get_engine()

print("Reading CSV...")

df = pd.read_csv("data/raw/flights.csv")

print(f"Rows Loaded : {len(df)}")
print(f"Columns     : {len(df.columns)}")

# Convert Date
df["FLIGHTDATE"] = pd.to_datetime(df["FLIGHTDATE"])

# Convert Time
df["CRSDEPTIME"] = pd.to_datetime(
    df["CRSDEPTIME"],
    format="%H:%M"
).dt.time

# Convert Boolean
df["CANCELLED"] = df["CANCELLED"].astype(bool)
df["DIVERTED"] = df["DIVERTED"].astype(bool)

# Rename Columns
df.columns = [
    "flight_date",
    "marketing_airline_network",
    "origin",
    "dest",
    "crs_dep_time",
    "dep_delay",
    "arr_delay",
    "distance",
    "crs_elapsed_time",
    "cancelled",
    "diverted"
]

print(df.head())


df.to_sql(
    "raw_flights",
    engine,
    if_exists="append",
    index=False,
    method="multi",
    chunksize=5000
)