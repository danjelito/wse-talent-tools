import streamlit as st

from src import salary_calculator
from src.glossary import PAYROLL_GLOSSARY, TAX_STATUS_LABELS
from src.ui_helpers import format_idr

st.header("Salary Calculator")
st.write(
    "Simulate monthly payroll with clear visibility of employee deductions "
    "and company-side contributions."
)
st.caption("Simulation period follows Jan-Nov TER approach.")
st.divider()

st.subheader("Input")
base_salary = st.number_input(
    "Base salary (monthly)",
    value=None,
    placeholder=0,
    min_value=0,
    step=100_000,
)

selected_tax_status = st.selectbox(
    "Tax status",
    options=list(TAX_STATUS_LABELS.keys()),
    format_func=lambda code: f"{code} - {TAX_STATUS_LABELS[code]}",
    help="TK = Single, K = Married. Number indicates dependent count.",
)

insurance = st.number_input(
    "Monthly insurance premium paid by company",
    value=None,
    placeholder=0,
    min_value=0,
    step=50_000,
    help="Used as taxable income component in this simulation.",
)

col1, col2 = st.columns(2)
with col1:
    bpjs_kes = st.checkbox(
        "Include JKN (Health)",
        value=True,
        help="Employee 1% and company 4% using max base IDR 12,000,000.",
    )
with col2:
    bpjs_tk = st.checkbox(
        "Include BPJS-TK (JHT, JP, JKK, JKM)",
        value=True,
        help=(
            "Includes JHT, JP, JKK, and JKM. JP uses max base "
            "IDR 11,086,300."
        ),
    )

st.write("###")
calculate = st.button("Calculate Payroll", type="primary")

if calculate:
    st.divider()
    st.subheader("Result")

    if not base_salary:
        st.error("Base salary is required.")
    elif int(base_salary) < 4_000_000:
        st.warning(
            f"Please reconfirm base salary: {format_idr(base_salary)}. "
            "This is below the usual operational baseline."
        )
    else:
        base_salary = int(base_salary)
        insurance = int(insurance) if insurance else 0

        try:
            result = salary_calculator.calculate_thp(
                base_salary=base_salary,
                tax_status=selected_tax_status,
                insurance_premium=insurance,
                is_bpjs_tk=bpjs_tk,
                is_bpjs_kes=bpjs_kes,
                jkk_rate_percentage=0.24,
            )
        except ValueError as err:
            st.error(str(err))
            st.stop()

        employee_deductions = (
            result["tax"]
            + result["jht_employee"]
            + result["jp_employee"]
            + result["jkn_employee"]
        )
        company_contributions = (
            result["jht_company"]
            + result["jp_company"]
            + result["jkn_company"]
            + result["jkk_company"]
            + result["jkm_company"]
        )

        col1, col2, col3 = st.columns(3)
        col1.metric("Base Salary", format_idr(base_salary))
        col2.metric("Employee Deductions", format_idr(employee_deductions))
        col3.metric("Take-Home Pay (THP)", format_idr(result["thp"]))

        st.write("###")
        left, right = st.columns(2)
        with left:
            st.markdown("#### Earnings and Employee-Side")
            st.write(f"- **Base salary:** {format_idr(base_salary)}")
            st.write(f"- **Insurance premium:** {format_idr(insurance)}")
            st.write(f"- **Tax (TER):** -{format_idr(result['tax'])}")
            st.write(f"- **JHT Employee (2%):** -{format_idr(result['jht_employee'])}")
            st.write(f"- **JP Employee (1%):** -{format_idr(result['jp_employee'])}")
            st.write(f"- **JKN Employee (1%):** -{format_idr(result['jkn_employee'])}")
            st.write(f"- **Total employee deductions:** **{format_idr(employee_deductions)}**")

        with right:
            st.markdown("#### Company-Side Contributions")
            st.write(f"- **JHT Company (3.7%):** {format_idr(result['jht_company'])}")
            st.write(f"- **JP Company (2%):** {format_idr(result['jp_company'])}")
            st.write(f"- **JKN Company (4%):** {format_idr(result['jkn_company'])}")
            st.write(
                f"- **JKK Company (0.24%):** {format_idr(result['jkk_company'])}"
            )
            st.write(f"- **JKM Company (0.30%):** {format_idr(result['jkm_company'])}")
            st.write(
                f"- **Total company contributions:** **{format_idr(company_contributions)}**"
            )

        st.info(
            "**How to read this**: THP reflects employee-side deductions and monthly "
            "tax. Company-side contributions are shown separately as employer cost."
        )

        with st.expander("Contribution Rules and Caps"):
            st.write("- JKN Employee: 1% of salary, max base IDR 12,000,000/month.")
            st.write("- JKN Company: 4% of salary, max base IDR 12,000,000/month.")
            st.write("- JHT Employee: 2% of salary, no cap.")
            st.write("- JHT Company: 3.7% of salary, no cap.")
            st.write("- JP Employee: 1% of salary, max base IDR 11,086,300/month.")
            st.write("- JP Company: 2% of salary, max base IDR 11,086,300/month.")
            st.write("- JKK Company: 0.24% to 1.74% of salary, risk-based.")
            st.write("- JKM Company: 0.30% of salary, no cap.")

        with st.expander("Glossary"):
            for term, explanation in PAYROLL_GLOSSARY.items():
                st.write(f"- {term}: {explanation}")

        with st.expander("Technical Notes and References"):
            st.write(
                "- January-November tax uses TER. December payroll may differ due to "
                "annual reconciliation under Article 17."
            )
            st.write(
                "- Output is a simulation and should be validated with current policy "
                "and legal guidance."
            )
            st.write(
                "- Reference: "
                "[Government Regulation Number 58 of 2023]"
                "(https://jdih.kemenkeu.go.id/in/dokumen/peraturan/067e1587-ae13-489a-4319-08dc0905f328)"
            )
            st.write(
                "- Reference: "
                "[2024 Tax Calculation Example by Mekari]"
                "(https://klikpajak.id/blog/pajak-penghasilan-pasal-21-2/)"
            )
