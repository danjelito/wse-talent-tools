import streamlit as st
from dateutil.relativedelta import relativedelta
from src import penalty_and_bonus_calculator
from src.ui_helpers import format_idr

st.header("Penalty Calculator")
st.write("Estimate penalty for contract employees who resign before contract end.")
st.caption("Formula used: penalty = base salary x remaining contract months.")
st.divider()

st.subheader("Input")
col1, col2 = st.columns(2)
with col1:
    contract_end_date = st.date_input(
        "Contract end date", format="DD/MM/YYYY", value=None
    )
with col2:
    last_working_date = st.date_input(
        "Last working date", format="DD/MM/YYYY", value=None
    )

base_salary = st.number_input(
    "Base salary",
    value=None,
    placeholder="Base salary",
    min_value=0,
    step=100_000,
)


if (
    contract_end_date is not None
    and last_working_date is not None
    and base_salary is not None
):
    if contract_end_date <= last_working_date:
        st.error("Contract end date must be after last working date. Otherwise penalty is 0.")
    else:
        last_working_date_to_contract_end_date = relativedelta(
            contract_end_date, last_working_date
        )
        penalty = penalty_and_bonus_calculator.calculate_penalty(
            contract_end_date, last_working_date, base_salary
        )
        remaining_months = (
            last_working_date_to_contract_end_date.years * 12
            + last_working_date_to_contract_end_date.months
        )

        st.subheader("Result")
        st.write(
            f"""
            Remaining contract = **{last_working_date_to_contract_end_date.years} years {last_working_date_to_contract_end_date.months} months {last_working_date_to_contract_end_date.days} days**.
        """
        )
        st.write("Penalty formula = base salary x remaining contract months")
        st.write(
            f"Penalty = {format_idr(base_salary)} x "
            f"{remaining_months} months"
        )
        st.success(f"Estimated penalty: {format_idr(penalty)}")
