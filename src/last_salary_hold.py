from dateutil.relativedelta import relativedelta


def month_diff(a, b):
    """Find the number of month between two dates (rounded down)."""
    return relativedelta(a, b).months


def hold_or_pay(last_wd, payroll_cycle_end_date):
    "Find whether to pay or hold salary for a certain month."
    if month_diff(last_wd, payroll_cycle_end_date) < 1:
        return False
    elif month_diff(last_wd, payroll_cycle_end_date) >= 1:
        return True
