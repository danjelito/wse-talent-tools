import streamlit as st
from src import salary_calculator

st.header("Salary Calculator")
st.write("Use this to find out THP given a base salary.")
st.divider()




st.write("#### Input")
base_salary = st.number_input("Base salary", value=None, placeholder=0)
tax_status = st.selectbox(
    "Tax/marriage status",
    (
        "TK/0",
        "TK/1",
        "TK/2",
        "TK/3",
        "K/0",
        "K/1",
        "K/2",
        "K/3",
    ),
)
insurance = st.number_input(
    "Monthly insurance premium",
    value=None,
    placeholder=0,
)
bpjs_kes = st.checkbox("BPJS Kes")
bpjs_tk = st.checkbox("BPJS TK")

st.write("###")
calculate = st.button("Calculate!", type="primary")


if calculate:

    st.divider()
    st.write("#### Result")

    # check if base salary is error
    if not base_salary:
        st.error("Base salary cannot be empty.")
    elif int(base_salary) < 4_000_000:
        st.error(f"Are you sure the base salary is only {base_salary:,}?")
    else:
        base_salary = int(base_salary)
    
        # if there is no insurance premium use 0
        if not insurance:
            insurance = 0

        # calculate
        result = salary_calculator.calculate_thp(base_salary, tax_status, insurance, bpjs_tk, bpjs_kes)

        # print result
        st.write(f"Base salary = **{base_salary:,}**")
        st.write(f"Tax = **- {result.get('tax'):,}**")
        st.write(f"JHT Employee = **- {result.get('jht_employee'):,}**")
        st.write(f"JP Employee = **- {result.get('jp_employee'):,}**")
        st.write(f"JKN Employee = **- {result.get('jkn_employee'):,}**")
        st.write(f"Take Home Pay = **{result.get('thp'):,}**")

        st.divider()
        st.write("#### Note")
        st.write(
            """
            1. Take-home pay is calculated as: Base Salary + Tax + JHT Employee + JP Employee + JKN Employee.
            2. The Salary Calculator is a simulation tool and cannot be used as a legal reference. In case the actual salary differs from the calculations listed here, refer to official regulation.
            """
        )
        st.divider()
        st.write("#### Reference")
        st.write(
            """
            1. [Government Regulation Number 58 of 2023](https://jdih.kemenkeu.go.id/in/dokumen/peraturan/067e1587-ae13-489a-4319-08dc0905f328).
            1. [2024 Tax Calculation Example by Mekari](https://klikpajak.id/blog/pajak-penghasilan-pasal-21-2/).
            """
        )

