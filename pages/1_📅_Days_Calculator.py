import streamlit as st

from src import days_calculator

st.header("Days Calculator")
st.write("Calculate the number of days between two dates with clear inclusivity rules.")
st.caption("Use calendar days for general timelines or working days for business planning.")
st.divider()

day_types = st.radio(
    "Day type",
    ["Calendar day", "Working day"],
    captions=[
        "Every day in the date range.",
        "Business days excluding weekends and Indonesian public holidays.",
    ],
)

st.subheader("Input")
col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Start date", format="DD/MM/YYYY", value=None)
    start_inclusive = st.toggle("Include start date")
with col2:
    end_date = st.date_input("End date", format="DD/MM/YYYY", value=None)
    end_inclusive = st.toggle("Include end date")

if start_date is not None and end_date is not None:
    st.subheader("Result")

    if end_date <= start_date:
        st.error("End date must be after start date.")

    else:
        if start_inclusive and end_inclusive:
            inclusive = "both"
        elif start_inclusive:
            inclusive = "left"
        elif end_inclusive:
            inclusive = "right"
        else:
            inclusive = "neither"

        if day_types == "Calendar day":
            num_days = days_calculator.calculate_days_between(
                start_date, end_date, "calendar", inclusive
            )

        elif day_types == "Working day":
            num_days = days_calculator.calculate_days_between(
                start_date, end_date, "working", inclusive
            )
            holidays_between = days_calculator.get_holidays_between(
                start_date, end_date, inclusive
            )

        if day_types == "Calendar day":
            message = f"Calendar-day total: **{num_days} days**"
        elif day_types == "Working day":
            message = f"Working-day total: **{num_days} days**"

        st.success(message)
        st.caption(
            f"Inclusivity mode: {inclusive}. Both date boundaries affect the count."
        )

        if day_types == "Working day":
            st.write("Public holidays in the selected range:")
            if len(holidays_between) > 0:
                for k, v in holidays_between.items():
                    st.write(f"- {k}: {v}")
            else:
                st.write("- None")
