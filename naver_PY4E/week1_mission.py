birth = int(input("생일이 지났습니까? 맞으면 0 아니면 -1: "))
while True:
    if birth != 0 and birth != -1:
        birth = int(input("다시 입력해주세요. 생일이 지났습니까? 맞으면 0, 아니면 -1 : "))
    else:
        break
age = int(input("한국 나이로 몇 살 입니까? : "))

if birth == 0: 
    print("당신은 만", age-1, "세 입니다.")
else:
    print("당신은 만", age-2, "세 입니다.")