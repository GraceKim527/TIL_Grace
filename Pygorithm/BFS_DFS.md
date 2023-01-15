# DFS/BFS 알고리즘
> '이것이 코딩 테스트다 with 파이썬'을 참고하여 작성한 글입니다.

## 꼭 필요한 자료구조 기초
- 탐색 : 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정을 의미
- 자료구조 : 데이터를 표현하고 관리하고 처리하기 위한 구조를 의미
    - 삽입(Push) : 데이터를 삽입
    - 삭제(Pop) : 데이터를 삭제

실제로 스택과 큐를 사용할 때는 삽입과 삭제 외에도 오버플로와 언더플로를 고민해야 한다.  
- 오버플로(Overflow) : 특정한 자료구조가 수용할 수 있는 데이터의 크기를 이미 가득 찬 상태에서 삽입 연산을 수행할 때 발생. 저장 공간을 벗어나 데이터가 넘쳐흐를 때 발생.
- 언더플로(Underflow) : 특정한 자료구조에 데이터가 전혀 들어 있지 않은 상태에서 삭제 연산을 수행하면 데이터가 전혀 없는 상태 발생.

### 스택
- 선입후출 구조 또는 후입선출 구조라고 한다.
- 입구와 출구가 동일한 형태로 스택을 시각화할 수 있다.

````python
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력 
print(stack[::-1]) # 최상단 원소부터 출력
````
````
[5, 2, 3, 1]
[1, 3, 2, 5]
````

### 큐
- 선입선출 구조라고 한다.
````python 
from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse() 
print(queue)
````
````
deque([3, 7, 1, 4])
deque([4, 1, 7, 3])
````
- deque는 스택과 큐의 장점을 모두 채택한 것인데 데이터를 넣고 빼는 속도가 리스트 자료형에 비해 효율적이고 queue 라이브러리를 이용하는 것이 더 간단하다.  
- deque 객체를 리스트 자료형으로 변경하고자 하면 list() 메서드를 이용하면 된다. list(queue)를 하면 리스트 자료형이 반환된다.

### 재귀 함수
- 자기 자신을 다시 호출하는 함수

#### 재귀 함수의 종료 조건
````python
def recursive_function(i):
    if i == 100:
        return
    print(i, ' 번째 재귀 함수에서', i + 1, '번째 재귀 함수를 호출합니다.')
    recursive_function(i + 1)
    print(i, '번째 재귀 함수를 종료합니다.')

recursive_function(1)
````
재귀 함수는 반복문을 이용하는 것과 비교했을 때 더욱 간결한 형태임을 이해할 수 있다.

## 탐색 알고리즘 DFS/BFS 
### DFS(깊이 우선 탐색)
- 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘

![node](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FxxOUl%2Fbtq4cGQ03y4%2FWmuKtGCjCuVOIN0Ok3Tzj0%2Fimg.png)

`노드`와 `간선`으로 표현되며 이때 노드를 `정점`이라고 한다.  

`그래프 탐색`이란 하나의 노드를 시작으로 다수의 노드를 방문하는 것을 말한다.  
두 노드가 간선으로 연결되어 있다면 '두 노드는 인접하다'라고 표현한다.  

- 인접 행렬 : 2차원 배열로 그래프의 연결 관계를 표현하는 방식
- 인접 리스트 : 리스트로 그래프의 연결 관계를 표현하는 방식    
- 인접 행렬 방식 : 2차원 배열에 각 노드가 연결된 형태를 기록하는 방식이다. 파이썬에서는 2차원 리스트로 구현할 수 있다.    
````python
INF = 999999999 

graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]
````
인접 행렬 방식으로 처리할 때에는 데이터를 초기화한다.  
파이썬은 리스트 자료형이 append()와 메소드를 제공하므로, 배열과 연결 리스트의 기능을 모두 기본으로 제공한다. 파이썬으로 인접 리스트를 이용해 그래프를 표현하고자 할 때에도 단순히 2차원 리스트를 이용하면 된다는 점.  

인접 리스트
````python
# 행(Row)이 3개인 2차원 리스트로 인접 리스트 표현 
graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))

# 노드 1에 연결된 노드 정보 저장(노드, 거리)
graph[1].append((0, 7))

# 노드 2에 연결된 노드 정보 저장(노드, 거리)
graph[2].append((0, 5))

print(graph)
````
````
[[(1, 7), (2, 5)], [(0, 7)], [(0, 5)]]
````
- `인접 행렬 방식`은 메모리 측면에서 보면 모든 관계를 저장하기 때문에 노드 개수가 많을수록 메모리가 불필요하게 낭비된다.
- `인접 리스트`은 연결된 정보만을 저장하기 때문에 메모리를 효율적으로 사용한다.    

> DFS의 구체적인 동작 과정
1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

DFS 예제
````python 
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end='')
    
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
````
````
1 2 7 6 8 3 4 5
````

### BFS(너비 우선 탐색)
- 가까운 노드부터 탐색하는 알고리즘

> BFS의 구체적인 동작 과정
1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

BFS 예제
````python
from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    
    # 현재 노드를 방문 처리
    visited[start] = True

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)

````
````
1 2 3 8 7 4 5 6
````

DFS | BFS |
--- | --- |
스택 | 큐 |
재귀 함수 이용 | 큐 자료구조 이용 |