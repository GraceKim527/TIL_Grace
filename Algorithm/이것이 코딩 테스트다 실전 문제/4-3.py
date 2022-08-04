# chapter04. 구현
# 왕실의 나이트
# 
# ----------------------------------------------------------------------------------
location = input() # 현 위치 문자로 받기
row = int(location[1])
# 아스키코드로 변환하여 a는 1, b는 2값으로 변환됨
column = int(ord(location[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 가능한지 확인
count = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    # 이동가능한지 확인 후 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        count += 1

print(count)
# ----------------------------------------------------------------------------------
# dx, dy나 steps와 같은 변수들은 자주 쓰이니 알아두도록 하자.