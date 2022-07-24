# 버스 요금 계산기
def bus_fare(age, pay):
    if pay == '카드':
        if age < 14:
            return 450
        elif age < 20:
            return 720
        else:
            return 1200
    else:
        if age < 14:
            return 450
        elif age < 20:
            return 1000
        else:
            return 1300

age = int(input("나이를 입력해주세요 >>> "))
pay = input("결제 유형을 선택해주세요(카드, 현금) >>> ")

while True:
    if age < 1:
        age = int(input("나이를 다시 입력해주세요 >>> "))
    else:
        break

while True:
    if pay != '카드' and pay != '현금':
        pay = input("결제 유형을 다시 선택해주세요(카드, 현금) >>>")
    else:
        break

print("나이 : ", age, "세")
print("지불유형 : ", pay)
if age < 8 or age >= 75:
    print("버스요금 : 무료")
else:
    print("버스요금 : ", bus_fare(age, pay), "원")