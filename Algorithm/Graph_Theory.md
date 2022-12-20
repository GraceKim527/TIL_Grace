# 그래프 이론
> '이것이 코딩 테스트다 with 파이썬'을 참고하여 작성한 글입니다.

## 서로소 집합 자료구조
- 공통 원소가 없는 두 집합을 의미 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조

````python
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end = ' ')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블: ', end=' ')
for i in range(1, v + 1):
    print(parent[i], end=' ')
````
- 입력 예시
````
6 4
1 4
2 3
2 4
5 6
````

- 출력 예시
````
각 원소가 속한 집합: 1 1 1 1 5 5
부모 테이블: 1 1 2 1 5 5
````

- find 함수가 비효율적으로 동작, 최악의 경우는 시간 복잡도가 O(V)다.

### 좀 더 개선된 서로소 집합 알고리즘 소스코드 
````python
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end = ' ')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블: ', end=' ')
for i in range(1, v + 1):
    print(parent[i], end=' ')
````
- 입력 예시
````
6 4
1 4
2 3
2 4
5 6
````

- 출력 예시
````
각 원소가 속한 집합: 1 1 1 1 5 5
부모 테이블: 1 1 2 1 5 5
````

### 서로소 집합 알고리즘의 시간 복잡도
- 노드의 개수 V개이고, 최대 V - 1개의 union 연산과 M개의 find 연산이 가능할 때 경로 압축 방법을 적용한 시간 복잡도는 O(V + M(1 + log2-M/VM))

### 서로소 집합을 활용한 사이클 판별
- 각 간선을 확인하며 두 노드의 루트 노드를 확인한다.
    - 루트 노드가 서로 다르다면 두 노드에 대하여 union 연산을 수행
    - 루트 노드가 서로 같다면 사이클(Cycle)이 발생한 것
- 그래프에 포함되어 있는 모든 간선에 대하여 위 과정을 반복

````python
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

cycle = False # 사이클 발생 여부

for i in range(e):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # 사이클이 발생하지 않았다면 합집합(union) 수행
    else:
        union_parent(parent, a, b)

if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")
````

- 입력 예시
````
3 3
1 2 
1 3
2 3
````

- 출력 예시
````
사이클이 발생했습니다.
````