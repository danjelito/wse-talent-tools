import streamlit as st
from dateutil.relativedelta import relativedelta

st.header("Bonus Calculator")
st.write("We give bonus for resigning employees who have served us for a long time.")
st.divider()


# date selector
col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input(
        "Select employment start date", format="DD/MM/YYYY", value=None
    )
    st.warning("Choose the date at which the employee became **permanent** employee.")
with col2:
    end_date = st.date_input(
        "Select last working date", format="DD/MM/YYYY", value=None
    )


if start_date is not None and end_date is not None:
    # start date must be <= end date
    if end_date <= start_date:
        st.error("End date must be after start date")
    else:
        diff = relativedelta(end_date, start_date)
        if diff.years >= 7:
            bonus = "**:green[3x base salary]**."
        elif diff.years >= 5:
            bonus = "**:green[2x base salary]**."
        else:
            bonus = "**:red[0]**."

        # write the result
        st.subheader("Result")
        st.write(
            f"""
            Working period = **{diff.years} years {diff.months} months {diff.days} days**.
        """
        )
        st.write(f"Bonus = {bonus}")
