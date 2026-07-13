import streamlit as st
from src.ui.charts import bar_chart

from src.database.dashboard_queries import (
    get_kpis,
    get_airline_chart,
    get_departure_period,
    get_delay_distribution,
    get_distance_category,
    get_top_airlines,
    get_preview,
    get_airlines
)
st.subheader("🎯 Dashboard Filters")


airlines = get_airlines()

selected_airline = st.selectbox(
    "Select Airline",
    ["All"] + airlines["marketing_airline_network"].tolist()
)

st.divider()

col1, col2 = st.columns(2)

with col1:

    airline_filter = st.selectbox(
        "Airline",
        ["All"] + sorted(
            get_airline_chart()["marketing_airline_network"].tolist()
        )
    )

with col2:

    distance_filter = st.selectbox(
        "Distance",
        ["All"] + sorted(
            get_distance_category()["distance_category"].tolist()
        )
    )

st.divider()


def show_dashboard():

    st.title("📊 Flight Analytics Dashboard")

    st.write(
        "Interactive dashboard for monitoring airline performance and flight delays."
    )

    st.divider()

    # =====================================================
    # KPI CARDS
    # =====================================================

    kpi = get_kpis()

    total = int(kpi.loc[0, "total"])
    delayed = int(kpi.loc[0, "delayed"])
    on_time = int(kpi.loc[0, "on_time"])
    delay_rate = float(kpi.loc[0, "delay_rate"])

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "✈ Total Flights",
        f"{total:,}"
    )

    c2.metric(
        "🔴 Delayed Flights",
        f"{delayed:,}"
    )

    c3.metric(
        "🟢 On-Time Flights",
        f"{on_time:,}"
    )

    c4.metric(
        "📈 Delay Rate",
        f"{delay_rate:.2f}%"
    )

    st.divider()

    # =====================================================
    # CHARTS
    # =====================================================

    left, right = st.columns(2)

    with left:

        st.subheader("✈ Flights by Airline")

        airline = get_airline_chart(selected_airline)

        st.plotly_chart(
            bar_chart(
                airline,
                "marketing_airline_network",
                "flights",
                "Flights by Airline"
            ),
            use_container_width=True
        )

    with right:

        st.subheader("🌅 Flights by Departure Period")

        period = get_departure_period()

        st.plotly_chart(
            bar_chart(
                period,
                "departure_period",
                "flights",
                "Flights by Departure Period"
            ),
            use_container_width=True
        )

    st.divider()

    left, right = st.columns(2)

    with left:

        st.subheader("📈 Delay Distribution")

        delay = get_delay_distribution()

        delay["delay_status"] = delay["delay_status"].replace(
            {
                0: "On Time",
                1: "Delayed"
            }
        )

        st.bar_chart(
            delay,
            x="delay_status",
            y="flights",
            use_container_width=True
        )

    with right:

        st.subheader("🛫 Distance Category")

        distance = get_distance_category()

        st.plotly_chart(
            bar_chart(
                distance,
                "distance_category",
                "flights",
                "Distance Category"
            ),
        use_container_width=True
    )

    st.divider()

    # =====================================================
    # TOP AIRLINES
    # =====================================================

    st.subheader("🏆 Top Airlines")

    top = get_top_airlines()

    top.columns = [
        "Airline",
        "Flights"
    ]

    st.dataframe(
        top,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # =====================================================
    # DATA PREVIEW
    # =====================================================

    with st.expander("🗂 Dataset Preview"):

        preview = get_preview()

        st.dataframe(
            preview,
            use_container_width=True,
            hide_index=True
        )