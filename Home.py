import streamlit as st


def main():
    st.title("TO Tools and Calculator")
    st.write("Created : 26 Dec 2023")
    st.write("Updated : 5 Jan 2026")
    st.divider()

    st.write(
        """
        Welcome to the TO Tools and Calculator website. This platform provides various tools to simplify employee-related calculations.
        Select the tool you need from the left sidebar.
        """
    )
    st.write(
        """
        Available Tools:
        1. **📅 Days Calculator**: Determine the number of days between two dates.
        2. **💰 Last Salary Hold or Pay**: Decide whether to hold or pay the salary of a resigning employee.
        3. **🎉 Bonus Calculator**: Calculate the bonus an employee is entitled to receive.
        4. **⚖️ Penalty Calculator**: Calculate the penalty for a contract employee who resigns early.
        5. **👴🏻 Age Calculator**: Calculate age from the date of birth.
        6. **💸 Salary Calculator**: Compute the take-home pay given a base salary.
        """
    )
    st.divider()
    st.write(
        """
        **Notes:**
        1. Always double-check the calculations with your common sense to ensure accuracy.
        2. If you encounter any errors, please notify Devan.
        """
    )


if __name__ == "__main__":
    main()
