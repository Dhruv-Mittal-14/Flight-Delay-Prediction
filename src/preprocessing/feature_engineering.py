import pandas as pd

# Read cleaned dataset
df = pd.read_csv("data/processed/clean_flights.csv")

print(df.head())

df["flight_date"] = pd.to_datetime(df["flight_date"])

# Month
df["month"] = df["flight_date"].dt.month

# Day of Month
df["day"] = df["flight_date"].dt.day

# Day Name
df["day_name"] = df["flight_date"].dt.day_name()

# Day of Week (0=Monday)
df["day_of_week"] = df["flight_date"].dt.dayofweek

# Quarter
df["quarter"] = df["flight_date"].dt.quarter\


df["is_weekend"] = df["day_of_week"].apply(
    lambda x: 1 if x >= 5 else 0
)


df["crs_dep_time"] = pd.to_datetime(
    df["crs_dep_time"].astype(str)
)

df["departure_hour"] = df["crs_dep_time"].dt.hour

df["departure_minute"] = df["crs_dep_time"].dt.minute


def departure_period(hour):

    if 5 <= hour < 12:
        return "Morning"

    elif 12 <= hour < 17:
        return "Afternoon"

    elif 17 <= hour < 21:
        return "Evening"

    else:
        return "Night"


df["departure_period"] = df["departure_hour"].apply(departure_period)


def distance_category(distance):

    if distance < 500:
        return "Short"

    elif distance <= 1500:
        return "Medium"

    else:
        return "Long"


df["distance_category"] = df["distance"].apply(distance_category)


# Flight duration in minutes
df["flight_duration_minutes"] = df["crs_elapsed_time"]

# Flight duration in hours
df["flight_duration_hours"] = (
    df["flight_duration_minutes"] / 60
).round(2)

# Flight duration category
def duration_category(minutes):
    if minutes < 120:
        return "Short Flight"
    elif minutes <= 240:
        return "Medium Flight"
    else:
        return "Long Flight"

df["duration_category"] = df["flight_duration_minutes"].apply(duration_category)

def delay_severity(delay):

    if delay <= 15:
        return "On Time"

    elif delay <= 60:
        return "Moderate Delay"

    else:
        return "Severe Delay"


df["delay_severity"] = df["arr_delay"].apply(delay_severity)







# Create Flight Number

df["flight_sequence"] = (
    df.groupby("marketing_airline_network")
      .cumcount()
)

df["flight_number"] = (
    df["marketing_airline_network"]
    + (1001 + df["flight_sequence"]).astype(str)
)

# Remove helper column
df.drop(columns=["flight_sequence"], inplace=True)

df.to_csv(
    "data/processed/flight_features.csv",
    index=False
)

# print(df.columns.tolist())

# print(df["flight_number"].duplicated().sum())

# print(df.dtypes)

print(df["created_at"].head())