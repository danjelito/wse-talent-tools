"""Reusable UI helpers for Streamlit pages."""


def format_idr(amount: float | int) -> str:
    """Format number as Indonesian Rupiah with separator."""
    return f"IDR {amount:,.0f}"


def format_percent(value: float) -> str:
    """Format fraction/number as percentage with up to 2 decimals."""
    return f"{value:.2f}%"
