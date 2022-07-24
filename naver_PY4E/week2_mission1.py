# Q1. 컴퓨터와 함께하는 가위바위보 게임
import random #random 모듈을 사용하면 무작위 난수를 쓸 수 있다.

def rcp(my):
    if my == com:
        print("비겼습니다!")
    elif my - com == -1 or (my == 2 and com == 0):
        print("컴퓨터 승리!")
    else:
        print("유저 승리!")


sel = ['가위', '바위', '보']
com = random.randint(0,2)

my = int(input("0 :가위, 1: 바위 2: 보 >>> "))
while True:
    if my > 2 or my < 0:
        my = int(input("다시 입력해주세요 (0, 1, 2만 선택) >>> "))
    else:
        break
print("나 : ", sel[my])
print("컴퓨터 : ", sel[com])

rcp(my)