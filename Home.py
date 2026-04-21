import streamlit as st


def main():
    st.title("TO Tools and Calculator Suite")
    st.write("**Created**: 26 Dec 2023")
    st.write("**Last Updated**: 21 Apr 2026")
    st.divider()

    st.subheader("HR Decisions, Faster and Clearer")
    st.write(
        "Use these calculators to support payroll and talent operations decisions "
        "with fewer manual steps and clearer assumptions."
    )

    st.subheader("Tool Index")
    st.write(
        "1. **📅 Days Calculator**: Calendar-day or working-day difference between two dates. Use for leave duration, notice period checks, timeline planning."
    )
    st.write(
        "2. **💰 Last Salary Hold or Pay**: A clear pay/hold recommendation across recent payroll cycles. Use for final payroll handling in resignation cases."
    )
    st.write(
        "3. **🎉 Bonus Calculator**: Service-period-based bonus indication. Use for exit bonus review of long-tenure employees."
    )
    st.write(
        "4. **⚖️ Penalty Calculator**: Contract-remaining-period penalty estimate. Use for early resignation in fixed-term contracts."
    )
    st.write(
        "5. **👴🏻 Age Calculator**: Exact age and optional time-to-target-age calculation. Use for eligibility and milestone checks."
    )
    st.write(
        "6. **💸 Salary Calculator**: Take-home pay simulation with employee and company contribution details. Use for offer simulation, payroll explanation, and budget planning."
    )

    st.markdown("#### Quality Notes")
    st.write(
        """
    - This app is a decision aid, not a legal document.
    - Inputs and assumptions drive the output quality.
    - Always cross-check exceptional or sensitive cases.
    """
    )

    st.markdown("#### Need Help?")
    st.write(
        """
    - Read the notes at the bottom of each calculator page.
    - Share feedback and discrepancy reports with Devan.
    - Request feature updates when policy changes occur.
    """
    )
    st.markdown(
        """
        #### How To Use
        1. Select a tool from the sidebar on the left.
        2. Complete the input section carefully and review helper notes.
        3. Click calculate (if available) and review the result breakdown.
        4. Need help? Read the instructions in each tool, or reach out to [Devan](mailto:devan@example.com).

        """
    )
    st.divider()
    st.error(
        "**Disclaimer**: This app is a decision aid tool and should not be considered a legal document. "
        "The quality of the output depends on the accuracy of the inputs and assumptions. "
        "Always cross-check exceptional or sensitive cases with your internal policy and legal team."
    )


if __name__ == "__main__":
    main()
