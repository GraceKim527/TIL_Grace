# 코딩테스트용 파이썬 팁 정리
- [문자열에서 특정 문자 제거 strip()](#strip)
- [자료구조 힙 heapq 모듈](#heapq)
- [반복되는 데이터를 처리하는 기능을 포함하는 라이브러리 itertools](#itertools)

## strip() - 문자열에서 특정 문자 제거 <a id="strip"></a>
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

## 자료구조 힙 heapq 모듈 <a id="heapq"></a>
### heap생성
````python
import heapq

heap = []
````

### heap 삽입
````python
heapq.heappush([힙 이름], [추가할 원소])
````

### heap 삭제
````python
heapq.heappop([힙 이름])
````

**최소 힙 자료구조**를 유지하며 우선순위가 높은 원소를 추출

### 리스트를 힙으로 변경
````python
heapq.heapify([리스트 이름])
````

## isdigit() 메서드
str.isdigit() -> 문자열이 '숫자'로만 이루어진 것인지 확인하는 함수
- 문자가 하나라도 있다면 False
- 모든 문자가 다 숫자라면 True

### 다음과 같이 사용 가능
````python
str.isdigit("판단하고자 하는 문자열")
"판단하고자 하는 문자열".isdigit()


````

## itertools <a id="itertools"></a>
파이썬에서 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리

- permutations (순열)
````python
from itertools import permutations
data = ['A', 'B', 'C']
result = list(permutations(data, 3))

print(result)
````

````
ABC, ACB, BAC, BCA, CAB, CBA
````

- combinations (조합)
````python
from itertools import combinations
data = ['A', 'B', 'C']
result = list(combinations(data, 2))

print(result)
````

````
AB, AC, BC
````

- product
    - permutations와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)을 계산. 원소를 중복하여 뽑는다.

````python
from itertools import product

data = ['A', 'B', 'C']
result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기(중복 허용)

print(result)
````

````
AA, AB, AC, BA, BB, BC, CA, CB, CC
````

- combinations_with_replacement
    - combinations와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)를 계산.

````python
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2))

print(result)
````

````
AA, AB, AC, BB, BC, CC
````