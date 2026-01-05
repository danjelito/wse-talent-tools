import pandas as pd
from pprint import pprint

tax_brackets = pd.read_excel("src/ter.xlsx")


def convert_tax_status_to_ter_group(tax_status):
    """Get TER given tax status."""
    ter_map = {
        "TK/0": "TER A",
        "TK/1": "TER A",
        "K/0": "TER A",
        "TK/2": "TER B",
        "TK/3": "TER B",
        "K/1": "TER B",
        "K/2": "TER B",
        "K/3": "TER C",
    }
    return ter_map.get(tax_status, None)


def find_tax_percentage(tax_brackets, gross_salary, tax_status):
    """Find TER given gross salary and TER group."""

    ter_group = convert_tax_status_to_ter_group(tax_status)
    bracket = tax_brackets[
        (tax_brackets["gross_salary_from"] <= gross_salary)
        & (tax_brackets["gross_salary_to"] >= gross_salary)
        & (tax_brackets["ter_group"] == ter_group)
    ]
    if not bracket.empty:
        return bracket.iloc[0]["ter"]
    return None


def calculate_tax(tax_brackets, gross_salary, tax_status):
    """Find tax given gross salary and TER group."""
    ter = find_tax_percentage(tax_brackets, gross_salary, tax_status)
    return round(gross_salary * ter, 0)


def calculate_jht(base_salary):
    jht_company = round(3.7 / 100 * base_salary, 0)
    jht_employee = round(2.0 / 100 * base_salary, 0)
    return jht_company, jht_employee


def calculate_jkk(base_salary):
    jkk_company = round(0.24 / 100 * base_salary, 0)
    return jkk_company


def calculate_jkm(base_salary):
    jkm_company = round(0.3 / 100 * base_salary, 0)
    return jkm_company


def calculate_jp(base_salary):
    jp_company = round(2.0 / 100 * min(base_salary, 10_547_400), 0)
    jp_employee = round(1.0 / 100 * min(base_salary, 10_547_400), 0)
    return jp_company, jp_employee


def calculate_jkn(base_salary):
    jkn_company = round(4.0 / 100 * min(base_salary, 12_000_000), 0)
    jkn_employee = round(1.0 / 100 * min(base_salary, 12_000_000), 0)
    return jkn_company, jkn_employee


def calculate_thp(base_salary, tax_status, insurance_premium, is_bpjs_tk, is_bpjs_kes):
    if is_bpjs_tk:
        jht_company, jht_employee = calculate_jht(base_salary)
        jkk_company = calculate_jkk(base_salary)
        jkm_company = calculate_jkm(base_salary)
        jp_company, jp_employee = calculate_jp(base_salary)
    else:
        jht_company, jht_employee = 0, 0
        jkk_company = 0
        jkm_company = 0
        jp_company, jp_employee = 0, 0

    if is_bpjs_kes:
        jkn_company, jkn_employee = calculate_jkn(base_salary)
    else:
        jkn_company, jkn_employee = 0, 0

    gross_salary = (
        base_salary + insurance_premium + jkk_company + jkm_company + jkn_company
    )
    tax = calculate_tax(tax_brackets, gross_salary, tax_status)
    thp = base_salary - jht_employee - jp_employee - jkn_employee - tax

    return {
        "jht_company": jht_company,
        "jht_employee": jht_employee,
        "jkk_company": jkk_company,
        "jkm_company": jkm_company,
        "jp_company": jp_company,
        "jp_employee": jp_employee,
        "jkn_company": jkn_company,
        "jkn_employee": jkn_employee,
        "gross_salary": gross_salary,
        "tax": tax,
        "thp": thp,
    }


# # test
# if __name__ == "__main__":

#     payroll_file = pd.read_excel("test/2024-05.xlsx")
#     for row in payroll_file.itertuples():

#         # this is from file
#         name = row.name
#         base_salary = row.base_salary
#         transport_allowance = row.transport_allowance
#         commission = row.commission
#         gross_salary = row.gross_salary
#         insurance_premium = row.insurance_premium
#         is_bpjs_kes = row.bpjs_kes_id > 0
#         is_bpjs_tk = row.bpjs_tk_id > 0
#         jht_company = row.jht_company
#         jht_employee = row.jht_employee
#         jkk_company = row.jkk_company
#         jkm_company = row.jkm_company
#         jkn_company = row.jkn_company
#         jkn_employee = row.jkn_employee
#         jp_company = row.jp_company
#         jp_employee = row.jp_employee
#         tax = row.tax
#         tax_status = row.tax_status
#         thp = row.thp
#         from_file = {
#             "gross_salary": gross_salary,
#             "jht_company": jht_company,
#             "jht_employee": jht_employee,
#             "jkk_company": jkk_company,
#             "jkm_company": jkm_company,
#             "jkn_company": jkn_company,
#             "jkn_employee": jkn_employee,
#             "jp_company": jp_company,
#             "jp_employee": jp_employee,
#             "tax": tax,
#             "thp": thp,
#         }

#         # this is calculation
#         calculation = calculate_thp(
#             base_salary,
#             tax_status,
#             insurance_premium,
#             is_bpjs_tk,
#             is_bpjs_kes,
#         )

#         def compare_dicts(dict1, dict2, threshold=0):
#             differences = {}
#             all_keys = set(dict1.keys()).union(set(dict2.keys()))

#             for key in all_keys:
#                 if key in dict1 and key in dict2:
#                     diff = dict1[key] - dict2[key]
#                     if abs(diff) > threshold:
#                         differences[key] = diff
#                 elif key not in dict1:
#                     differences[key] = f"Key '{key}' is missing in dict1"
#                 else:
#                     differences[key] = f"Key '{key}' is missing in dict2"
#             return differences

#         def print_differences(differences):
#             print("Differences found:")
#             for key, diff in differences.items():
#                 pprint(f"Key '{key}' has a difference of {diff}")

#         print()
#         print(f"Check for {name} started.")
#         differences = compare_dicts(calculation, from_file, threshold=1)
#         if differences:
#             print_differences(differences)
#             break
#         print(f"Check for {name} finished, all OK.")
