# 학점 변환기
def grader(name, score):
    print("학생이름 : ", name)
    print("점수 : ", score)
    if score >= 95:
        print("학점 : A+")
    elif score >= 90:
        print("학점 : A")
    elif score >= 85:
        print("학점 : B+")
    elif score >= 80:
        print("학점 : B")
    elif score >= 75:
        print("학점 : C+")
    elif score >= 70:
        print("학점 : C")
    elif score >= 65:
        print("학점 : D+")
    elif score >= 60:
        print("학점 : D")
    else:
        print("학점 : F")

# 이름과 점수 입력
name = input("이름을 출력해주세요 >>> ")
score = int(input("점수를 입력해주세요 >>> "))
while True:
    if score > 100 or score < 0:
        score = int(input("다시 입력해주세요 >>> "))
    else:
        break
grader(name, score)