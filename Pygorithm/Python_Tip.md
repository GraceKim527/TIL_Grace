# 코딩테스트용 파이썬 팁 정리
- [문자열에서 특정 문자 제거 strip()](#strip)
- [자료구조 힙 heapq 모듈](#heapq)
- [반복되는 데이터를 처리하는 기능을 포함하는 라이브러리 itertools](#itertools)
- [collections 모듈을 이용한 Counter](#counter)
- [zip 내장 함수](#zip)
- [알파벳과 인덱스를 이용해야하는 문제](#alpha)
- [파이썬 대문자 소문자](#uplow)

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

## collections 모듈의 Counter사용법 <a id="counter"></a>
````python
from collections import Counter
Counter(["hi", "hey", "hi", "hi", "hello", "hey"])
Counter({'hi': 3, 'hey': 2, 'hello': 1})
````

### 사전처럼 사용
````python
counter["l"] += 1
counter["h"] -= 1
counter

if "o" in counter:
    print("o in counter")

del counter["o"]

if "o" not in counter:
    print("o not in counter")
````

### 데이터의 개수가 많은 순으로 정렬하는 most_common() 메서드
````python
from collections import Counter

Counter('hello world').most_common()

[('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]
````

이외에도 산술연산도 가능하다.
````
counter1 = Counter(["A", "A", "B"])
counter2 = Counter(["A", "B", "B"])

counter1 + counter2
Counter({'A': 3, 'B': 3})

counter1 - counter2
Counter({'A': 1})
````

## zip 내장 함수 <a id="zip"></a>
### zip 기본 문법
````python
>>> numbers = [1, 2, 3]
>>> letters = ["A", "B", "C"]
>>> for pair in zip(numbers, letters):
...     print(pair)
...
(1, 'A')
(2, 'B')
(3, 'C')
````

### 병렬 처리 
````python
>>> for number, upper, lower in zip("12345", "ABCDE", "abcde"):
...     print(number, upper, lower)
...
1 A a
2 B b
3 C c
4 D d
5 E e
````

### unzip
````python
>>> numbers = (1, 2, 3)
>>> letters = ("A", "B", "C")
>>> pairs = list(zip(numbers, letters))
>>> print(pairs)
[(1, 'A'), (2, 'B'), (3, 'C')]
````

- 함수로 넘기는 인자의 길이가 서로 다를 경우, **가장 짧은 인자**를 기준으로 엮이고 나머지 부분은 버려지므로 이 점 유의하자.

## 알파벳과 인덱스를 이용해야 하는 문제  <a id="alpha"></a>

```python
def solution(s, skip, index):
    answer = ""
    alpha = "abcdefghijklmnopqrstuvwxyz" # 알파벳
    
    for ch in skip: # ch => skip의 문자 하나하나
        if ch in alpha:
            alpha = alpha.replace(ch, "") # 알파벳 안에 skip 문자들 제거
    
    for i in s:
        change = alpha[(alpha.index(i) + index) % len(alpha)] # s의 문자 인덱스 + index를 alpha의 길이로 나눈 나머지를 알파벳으로 변환
        answer += change
    
    return answer
```

- 알파벳의 인덱스와 인덱스가 끝난 후 다시 처음으로 돌아와야 할 때 쓰면 좋을만한 구문. 

## 파이썬 대문자 소문자 <a id="uplow"></a>
### string.upper()
- string : 바꾸고자 하는 문자열의 객체
- 반환형 : 모든 문자열이 대문자로 바뀐 문자열

````python
s = 'abcDef'.upper()
print('s : ' + s) # s : ABCDEF
````

### string.lower() 
- string : 바꾸고자 하는 문자열 객체
- 반환형 : 모든 문자열이 소문자로 바뀐 문자열

````python
s = "This is Programming"
print('s : '+s) # s : this is programming
````

### string.isupper()
- 함수 : string 객체 내부에 있는 모든 문자가 대문자인지 검사하는 함수
- 반환형 : Bool(True, False)

### string.islower()
- 함수 : string 객체 내부에 있는 모든 문자가 소문자인지 검사하는 함수
- 반환형 : Bool(True, False)