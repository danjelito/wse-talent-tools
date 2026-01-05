import streamlit as st

from src import days_calculator

st.header("Days Calculator")
st.write("No more manual counting. I'm tired of that.")
st.divider()

# calendar day or working day selector
day_types = st.radio(
    "**Select day type**",
    ["Calendar day", "Working day"],
    captions=[
        "Usual calendar days",
        "Business days, excluding weekends and holidays",
    ],
)
# date selector
col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Select start date", format="DD/MM/YYYY", value=None)
    start_inclusive = st.toggle("Include start date")
with col2:
    end_date = st.date_input("Select end date", format="DD/MM/YYYY", value=None)
    end_inclusive = st.toggle("Include end date")

if start_date is not None and end_date is not None:
    st.subheader("Result")
    # start date must be <= end date
    if end_date <= start_date:
        st.error("End date must be after start date")

    else:
        # create inclusivity
        if start_inclusive and end_inclusive:
            inclusive = "both"
        elif start_inclusive:
            inclusive = "left"
        elif end_inclusive:
            inclusive = "right"
        else:
            inclusive = "neither"

        # for calendar day
        if day_types == "Calendar day":
            num_days = days_calculator.calculate_days_between(
                start_date, end_date, "calendar", inclusive
            )

        # for working day
        elif day_types == "Working day":
            num_days = days_calculator.calculate_days_between(
                start_date, end_date, "working", inclusive
            )
            holidays_between = days_calculator.get_holidays_between(
                start_date, end_date, inclusive
            )

        # display result
        if day_types == "Calendar day":
            message = f"Calendar days between : **{num_days} days**"
        elif day_types == "Working day":
            message = f"Working days between : **{num_days} days**"
        st.success(message)

        # for working days, display the holiday
        if day_types == "Working day":
            st.write("Holidays between these two dates:")
            if len(holidays_between) > 0:
                for k, v in holidays_between.items():
                    st.write("- ", k, ":", v)
            else:
                st.write("- None")
