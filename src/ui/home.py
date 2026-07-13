import streamlit as st

from src.database.get_flight import get_flight_details
from src.utils.predictor import predict_delay


def show_home():

    # ---------------------------------
    # Session State
    # ---------------------------------

    if "flight" not in st.session_state:
        st.session_state.flight = None

    # ---------------------------------
    # Header
    # ---------------------------------

    st.title("✈ Flight Delay Prediction System")

    st.write(
        "Predict whether a flight is likely to be delayed before departure using Machine Learning."
    )

    st.divider()

    # ---------------------------------
    # Search Section
    # ---------------------------------

    st.subheader("🔍 Search Flight")

    col1, col2 = st.columns([5, 1])

    with col1:

        flight_number = st.text_input(
            "Flight Number",
            placeholder="Example : DL1001",
            label_visibility="collapsed"
        )

    with col2:

        search = st.button(
            "Search",
            use_container_width=True
        )

    # ---------------------------------
    # Search Button
    # ---------------------------------

    if search:

        if flight_number.strip() == "":

            st.warning("Please enter a Flight Number.")

            st.session_state.flight = None

        else:

            with st.spinner("Searching Flight..."):

                flight = get_flight_details(
                    flight_number.upper().strip()
                )

            if flight.empty:

                st.error("Flight Not Found.")

                st.session_state.flight = None

            else:

                st.success("✅ Flight Found!")

                st.session_state.flight = flight.iloc[0]

    # ---------------------------------
    # Show Flight Details
    # ---------------------------------

    if st.session_state.flight is not None:

        flight = st.session_state.flight

        st.divider()

        st.subheader("✈ Flight Information")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "Flight",
            flight["flight_number"]
        )

        c2.metric(
            "Airline",
            flight["marketing_airline_network"]
        )

        c3.metric(
            "Origin",
            flight["origin"]
        )

        c4.metric(
            "Destination",
            flight["dest"]
        )

        st.write("")

        c5, c6, c7, c8 = st.columns(4)

        c5.metric(
            "Distance",
            f"{flight['distance']} Miles"
        )

        c6.metric(
            "Duration",
            f"{flight['flight_duration_minutes']} Min"
        )

        c7.metric(
            "Departure",
            str(flight["crs_dep_time"])
        )

        c8.metric(
            "Day",
            flight["day_name"]
        )

        st.divider()

        # ---------------------------------
        # Predict Button
        # ---------------------------------

        if st.button(
            "🚀 Predict Delay",
            use_container_width=True
        ):

            with st.spinner("Predicting..."):

                prediction, probability = predict_delay(flight)

            confidence = (
                probability if prediction == 1
                else (1 - probability)
            )

            st.divider()

            st.subheader("🤖 Prediction Result")

            if prediction == 1:

                st.error("🔴 Flight is likely to be DELAYED")

            else:

                st.success("🟢 Flight is likely to be ON TIME")

            st.metric(
                "Model Confidence",
                f"{confidence * 100:.2f}%"
            )

            st.subheader("🚦 Risk Level")

            if probability < 0.30:

                st.success("🟢 LOW RISK")

                st.progress(probability)

            elif probability < 0.70:

                st.warning("🟡 MEDIUM RISK")

                st.progress(probability)

            else:

                st.error("🔴 HIGH RISK")

                st.progress(probability)

            st.subheader("💡 Recommendation")

            if prediction == 1:

                st.warning("""
• Reach the airport early.

• Keep checking airline notifications.

• Monitor weather conditions.

• Keep your boarding pass ready.

• Reach the airport at least 2 hours before departure.
""")

            else:

                st.success("""
• Flight is expected to depart on time.

• Follow your normal travel schedule.

• Reach the airport 1–2 hours before departure.

• Have a safe journey!
""")