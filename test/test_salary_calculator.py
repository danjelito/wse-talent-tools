from src import salary_calculator


def test_jp_uses_11086300_cap():
    high_salary = 20_000_000
    jp_company, jp_employee = salary_calculator.calculate_jp(high_salary)

    assert jp_company == round(0.02 * 11_086_300, 0)
    assert jp_employee == round(0.01 * 11_086_300, 0)


def test_jkn_uses_12000000_cap():
    high_salary = 20_000_000
    jkn_company, jkn_employee = salary_calculator.calculate_jkn(high_salary)

    assert jkn_company == round(0.04 * 12_000_000, 0)
    assert jkn_employee == round(0.01 * 12_000_000, 0)


def test_jkk_rate_is_configurable():
    base_salary = 10_000_000

    default_jkk = salary_calculator.calculate_jkk(base_salary)
    high_risk_jkk = salary_calculator.calculate_jkk(base_salary, rate_percentage=1.74)

    assert default_jkk == round(0.0024 * base_salary, 0)
    assert high_risk_jkk == round(0.0174 * base_salary, 0)


def test_calculate_thp_returns_company_and_employee_breakdown():
    result = salary_calculator.calculate_thp(
        base_salary=12_000_000,
        tax_status="TK/0",
        insurance_premium=500_000,
        is_bpjs_tk=True,
        is_bpjs_kes=True,
        jkk_rate_percentage=0.54,
    )

    expected_keys = {
        "jht_company",
        "jht_employee",
        "jkk_company",
        "jkm_company",
        "jp_company",
        "jp_employee",
        "jkn_company",
        "jkn_employee",
        "gross_salary",
        "tax",
        "thp",
    }

    assert expected_keys.issubset(result.keys())
    assert result["jkk_company"] == round(0.0054 * 12_000_000, 0)
