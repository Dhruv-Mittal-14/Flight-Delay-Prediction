import pandas as pd
from sqlalchemy import text

from src.database.db_connection import get_engine


engine = get_engine()


# -----------------------------
# KPI
# -----------------------------

def get_kpis():

    query = text("""
    SELECT

        COUNT(*) AS total,

        SUM(delay_status) AS delayed,

        COUNT(*) - SUM(delay_status) AS on_time,

        ROUND(
            SUM(delay_status)::numeric
            / COUNT(*) * 100,
            2
        ) AS delay_rate

    FROM flights;
    """)

    return pd.read_sql(query, engine)


# -----------------------------
# Airline
# -----------------------------

def get_airline_chart(selected_airline="All"):

    if selected_airline == "All":

        query = text("""
            SELECT
                marketing_airline_network,
                COUNT(*) AS flights
            FROM flights
            GROUP BY marketing_airline_network
            ORDER BY flights DESC;
        """)

        return pd.read_sql(query, engine)

    query = text("""
        SELECT
            marketing_airline_network,
            COUNT(*) AS flights
        FROM flights
        WHERE marketing_airline_network = :airline
        GROUP BY marketing_airline_network;
    """)

    return pd.read_sql(
        query,
        engine,
        params={"airline": selected_airline}
    )


# -----------------------------
# Departure Period
# -----------------------------

def get_departure_period():

    query = text("""

    SELECT

        departure_period,

        COUNT(*) AS flights

    FROM flights

    GROUP BY departure_period

    ORDER BY flights DESC;

    """)

    return pd.read_sql(query, engine)


# -----------------------------
# Delay Distribution
# -----------------------------

def get_delay_distribution():

    query = text("""

    SELECT

        delay_status,

        COUNT(*) AS flights

    FROM flights

    GROUP BY delay_status;

    """)

    return pd.read_sql(query, engine)


# -----------------------------
# Distance Category
# -----------------------------

def get_distance_category():

    query = text("""

    SELECT

        distance_category,

        COUNT(*) AS flights

    FROM flights

    GROUP BY distance_category;

    """)

    return pd.read_sql(query, engine)


# -----------------------------
# Top Airlines
# -----------------------------

def get_top_airlines():

    query = text("""

    SELECT

        marketing_airline_network,

        COUNT(*) AS flights

    FROM flights

    GROUP BY marketing_airline_network

    ORDER BY flights DESC

    LIMIT 10;

    """)

    return pd.read_sql(query, engine)


# -----------------------------
# Preview
# -----------------------------

def get_preview():

    query = text("""

    SELECT *

    FROM flights

    LIMIT 20;

    """)

    return pd.read_sql(query, engine)



def get_airlines():

    query = text("""
        SELECT DISTINCT marketing_airline_network
        FROM flights
        ORDER BY marketing_airline_network;
    """)

    return pd.read_sql(query, engine)