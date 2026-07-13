from sqlalchemy import text
import pandas as pd
from src.database.db_connection import get_engine


def get_flight_details(flight_number):

    query = text("""
        SELECT *
        FROM flights
        WHERE flight_number = :flight_number
    """)

    df = pd.read_sql(
        query,
        get_engine(),
        params={
            "flight_number": flight_number
        }
    )

    return df