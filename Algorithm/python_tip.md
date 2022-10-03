# 코딩테스트용 파이썬 팁 정리

## strip() - 문자열에서 특정 문자 제거
### strip([chars])
- 인자로 전달된 문자를 String의 왼쪽과 오른쪽에서 제거한다.

### lstrip([chars])
- 인자로 전달된 문자를 String의 왼쪽에서 제거한다.

### rstrip([chars])
- 인자로 전달된 문자를 String의 오른쪽에서 제거한다.

## import sys - input대신 사용하자
- `input()`보다 `sys.stdin.readline()`이 좀 더 빠르고 메모리도 적게 소모한다.

### 활용 방법
````python
import sys
input = sys.stdin.readline
n = int(input())
````

### 응용
- 문자열 n줄을 입력받아 리스트에 저장
````python
import sys
data = [sys.stdin.readline().strip() for i in range(n)]
````