import streamlit as st
from datetime import date
from dateutil.relativedelta import relativedelta

st.header("Age Calculator")
st.write("Calculate exact age in years, months, and days.")
st.caption("Optionally calculate remaining time to a target age.")
st.divider()

st.subheader("Input")
col1, col2 = st.columns(2)
with col1:
    dob_date = st.date_input(
        "Date of birth",
        format="DD/MM/YYYY",
        value=None,
        min_value=date(1950, 1, 1),
        max_value=date(2049, 12, 31),
    )
with col2:
    end_date = st.date_input(
        "Reference date",
        format="DD/MM/YYYY",
        value="today",
        min_value=date(1950, 1, 1),
        max_value=date(2049, 12, 31),
    )
toggle_age_to_calc = st.toggle("Calculate days left to certain age")
if toggle_age_to_calc:
    age_to_calc = st.number_input(
        "Target age", value=None, placeholder="Age", min_value=0
    )


if dob_date is not None and end_date is not None:
    if end_date <= dob_date:
        st.error("Date of birth must be before reference date.")
    else:
        age = relativedelta(end_date, dob_date)
        if toggle_age_to_calc and age_to_calc:
            dob_plus_date = dob_date + relativedelta(years=age_to_calc)
            end_date_to_age_to_calc = relativedelta(dob_plus_date, end_date)

        st.subheader("Result")
        st.write(
            f"""
            Current age = **{age.years} years {age.months} months {age.days} days**.
        """
        )
        if toggle_age_to_calc and age_to_calc:
            st.write(
                f"""
                End date to age {age_to_calc: .0f} = **{end_date_to_age_to_calc.years} years {end_date_to_age_to_calc.months} months {end_date_to_age_to_calc.days} days**.
            """
            )

        with st.expander("Notes"):
            st.write("- Results depend on the selected reference date.")
            st.write("- Use this as a planning aid for eligibility milestones.")
