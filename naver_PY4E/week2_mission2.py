# 월급을 입력하면 연봉을 계산하는 계산기
def year_payment(monthly_payment):
    before = monthly_payment * 12
    print("세전 연봉: ", before, "만원")
    after = 0
    if before <= 1200:
        after = before - (before * 0.06)
    elif before <= 4600:
        after = before - (before * 0.15)
    elif before <= 8800:
        after = before - (before * 0.24)
    elif before <= 15000:
        after = before - (before * 0.35)
    elif before <= 30000:
        after = before - (before * 0.38)
    elif before <= 50000:
        after = before - (before * 0.4)
    else:
        after = before - (before * 0.42)
    print("세후 연봉: ", round(after), "만원")

monthly_payment = int(input())
year_payment(monthly_payment)