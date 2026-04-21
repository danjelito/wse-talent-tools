import streamlit as st
from dateutil.relativedelta import relativedelta

st.header("Bonus Calculator")
st.write("Estimate bonus eligibility based on completed service period.")
st.caption("This calculator follows the internal tenure threshold rule.")
st.divider()

st.subheader("Input")
col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input(
        "Employment start date",
        format="DD/MM/YYYY",
        value=None,
    )
    st.caption("Use the date when the employee became permanent.")
with col2:
    end_date = st.date_input(
        "Last working date",
        format="DD/MM/YYYY",
        value=None,
    )


if start_date is not None and end_date is not None:
    if end_date <= start_date:
        st.error("Last working date must be after employment start date.")
    else:
        diff = relativedelta(end_date, start_date)
        if diff.years >= 7:
            bonus = "**:green[3x base salary]**."
        elif diff.years >= 5:
            bonus = "**:green[2x base salary]**."
        else:
            bonus = "**:red[0]**."

        st.subheader("Result")
        st.write(
            f"""
            Service period = **{diff.years} years {diff.months} months {diff.days} days**.
        """
        )
        st.write(f"Bonus entitlement = {bonus}")

        with st.expander("Rule used in this page"):
            st.write("- 7 years or more: 3x base salary.")
            st.write("- 5 to <7 years: 2x base salary.")
            st.write("- Below 5 years: no bonus.")
