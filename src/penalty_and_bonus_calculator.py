from dateutil.relativedelta import relativedelta

def calculate_penalty(contract_end_date, last_working_date, base_salary):
    last_working_date_to_contract_end_date = relativedelta(
        contract_end_date, last_working_date
    )
    penalty = last_working_date_to_contract_end_date.months * base_salary
    return penalty