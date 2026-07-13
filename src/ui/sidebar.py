import streamlit as st

def show_sidebar():

    with st.sidebar:

        st.title("✈ Flight Delay")

        st.markdown("---")

        page = st.radio(
            "Navigation",
            [
                "🏠 Home",
                "📊 Analytics Dashboard",
                "🤖 Model Performance",
                "ℹ About Project"
            ]
        )

        st.markdown("---")

        st.write("👨‍💻 Developer")
        st.success("Dhruv Mittal")

        st.write("🎓 Course")
        st.info("MCA Data Science")

        st.markdown("---")

        st.write("🤖 Model")
        st.success("Random Forest")

        st.write("🗄 Database")
        st.success("Neon PostgreSQL")

        st.write("📈 Prediction")
        st.success("Binary Classification")

        st.markdown("---")

        st.caption("Version 1.0")

    return page