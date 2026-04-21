from dateutil.relativedelta import relativedelta


def calculate_penalty(contract_end_date, last_working_date, base_salary):
    last_working_date_to_contract_end_date = relativedelta(
        contract_end_date, last_working_date
    )
    remaining_months = (
        last_working_date_to_contract_end_date.years * 12
        + last_working_date_to_contract_end_date.months
    )
    penalty = remaining_months * base_salary
    return penalty