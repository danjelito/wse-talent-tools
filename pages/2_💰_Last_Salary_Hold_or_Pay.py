import pandas as pd
import streamlit as st
from src import last_salary_hold

st.header("Hold or Pay Last Salary?")
st.write(
    "Review whether salary should be held or paid for a resigning employee across payroll cycles."
)
st.caption("Policy note: this page reflects the one-month minimum withholding approach.")
st.divider()

st.subheader("Input")
last_wd = st.date_input("Last working day", format="DD/MM/YYYY", value=None)

if last_wd and last_wd.day <= 23:
    last_payroll_cycle = last_wd + pd.DateOffset(day=23)
elif last_wd and last_wd.day > 23:
    last_payroll_cycle = last_wd + pd.DateOffset(day=23) + pd.DateOffset(months=1)


if last_wd:
    last_6_payroll_cycle_ending = [
        last_payroll_cycle - pd.DateOffset(months=i) for i in range(0, 7, 1)
    ]

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

    st.markdown("#### Pay or Hold by Cycle")
    for payroll_start, payroll_end in zip(
        last_6_payroll_cycle_beginning, last_6_payroll_cycle_ending
    ):
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

    with st.expander("How this decision is interpreted"):
        st.write("- Hold: salary is withheld for that payroll cycle.")
        st.write("- Pay: salary can be processed for that payroll cycle.")
        st.write(
            "- Always validate final action with your internal payroll policy owner."
        )
