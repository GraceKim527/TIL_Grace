# 이진 탐색
> '이것이 코딩 테스트다 with 파이썬'을 참고하여 작성한 글입니다.

## 범위를 반씩 좁혀가는 탐색
### 순차 탐색
- 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법

````python
# 순차 탐색 소스코드 구현
def sequential_search(n, target, array):
    # 각 원소를 하나씩 확인하며
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            return i + 1 # 현재 위치 반환(인덱스는 0부터이기때문에 +1)

print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
input_data = input().split()
n = int(input_data[0]) # 원소의 개수
target = input_data[1] # 찾고자 하는 문자열

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()

# 순차 탐색 수행 결과 출력
print(sequential_search(n, target, array))
````
console
````
생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.
5 Dongbin
앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.
Hanul Jonggu Dongbin Taeil Sangwook
3
````

#### 시간 복잡도
데이터의 개수가 N일 때 최대 N번의 연산이 필요하므로 순차 탐색의 최악의 경우 시간 복잡도는 `O(N)`이다.

### 이진 탐색 : 반으로 쪼개면서 탐색하기
- **배열 내부의 데이터가 정렬되어있어야만** 사용할 수 있는 알고리즘이다.
- **시작점, 끝점, 중간점** 을 주로 변수로 사용하고, **찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교**한다.

````python
# 이진 탐색 소스코드 구현(재귀 함수)
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)

# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
````