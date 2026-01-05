import streamlit as st
from dateutil.relativedelta import relativedelta
from src import penalty_and_bonus_calculator

st.header("Penalty Calculator")
st.write("We impose penalty for resigning contract employees.")
st.divider()


# date selector
col1, col2 = st.columns(2)
with col1:
    contract_end_date = st.date_input(
        "Select **contract end date**", format="DD/MM/YYYY", value=None
    )
with col2:
    last_working_date = st.date_input(
        "Select **last working date**", format="DD/MM/YYYY", value=None
    )

base_salary = st.number_input(
    "Insert **base salary**", value=None, placeholder="Base salary"
)


if (
    contract_end_date is not None
    and last_working_date is not None
    and base_salary is not None
):
    # start date must be <= end date
    if contract_end_date <= last_working_date:
        st.error("Contract end date must be after last working date. Else, no penalty.")
    else:
        last_working_date_to_contract_end_date = relativedelta(
            contract_end_date, last_working_date
        )
        penalty = penalty_and_bonus_calculator.calculate_penalty(
            contract_end_date, last_working_date, base_salary
        )

        # write the result
        st.subheader("Result")
        st.write(
            f"""
            Remaining contract = **{last_working_date_to_contract_end_date.years} years {last_working_date_to_contract_end_date.months} months {last_working_date_to_contract_end_date.days} days**.
        """
        )
        st.write(f"Penalty = base salary * remaining contract")
        st.write(
            f"Penalty = {base_salary:,.0f} * {last_working_date_to_contract_end_date.months} = {base_salary * last_working_date_to_contract_end_date.months: ,.0f}"
        )
