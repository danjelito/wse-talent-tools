import pandas as pd
import streamlit as st
from src import last_salary_hold

st.header("Hold or Pay Last Salary?")
st.write(
    "Salary for resigning employees should be held, with a **minimum withholding of one month's salary**."
)
st.divider()


# last working days selector
last_wd = st.date_input("**Select last working day**", format="DD/MM/YYYY", value=None)


# calculate last payroll cycle of that particular employee
if last_wd and last_wd.day <= 23:
    last_payroll_cycle = last_wd + pd.DateOffset(day=23)
elif last_wd and last_wd.day > 23:
    last_payroll_cycle = last_wd + pd.DateOffset(day=23) + pd.DateOffset(months=1)


if last_wd:
    # the closing of payroll cycle
    last_6_payroll_cycle_ending = [
        last_payroll_cycle - pd.DateOffset(months=i) for i in range(0, 7, 1)
    ]
    # the corresponding opening of payrol cycle
    last_6_payroll_cycle_beginning = [
        d - pd.DateOffset(months=1) - pd.DateOffset(day=24)
        for d in last_6_payroll_cycle_ending
    ]

    st.subheader("Result")
    st.write(f"Last working day : **{last_wd.strftime('%d %b %Y')}**")
    st.write(
        f"Last payroll cycle : ",
        f"**{last_6_payroll_cycle_beginning[0].strftime('%d %b %Y')}** - "
        f"**{last_6_payroll_cycle_ending[0].strftime('%d %b %Y')}**",
    )
    # iterate over last 6 payroll cycles
    for payroll_start, payroll_end in zip(
        last_6_payroll_cycle_beginning, last_6_payroll_cycle_ending
    ):
        # whether to pay salay for this month or not
        pay = last_salary_hold.hold_or_pay(
            last_wd=last_wd, payroll_cycle_end_date=payroll_end
        )
        if pay:
            payment_status = "**:green[Pay]**"
        else:
            payment_status = "**:red[Hold]**"
        st.write(
            f"- {payroll_start.strftime('%d %b %Y')} - ",
            f"{payroll_end.strftime('%d %b %Y')} :",
            payment_status,
        )
