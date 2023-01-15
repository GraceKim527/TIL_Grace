# 백트래킹 알고리즘

## 구현
- 해를 구하는 도중 해가 아니어서 막히면 막히기 전으로 다시 돌아가서 해를 찾는 기법
- 예를 들어, 갈랫길에서 한쪽으로 갔다가 이 길이 아닌 것 같으면 왔던 길로 되돌아와 다른 선택지로 간다고 생각하면 됨.
- 가상의 트리에서 해를 구하기 위해 부모 노드에서 자식 노드까지 뻗어나간다. 만약 해당 노드가 조건에 맞지 않는다면 다시 부모노드로 돌아감.
- 해가 아닌 선택지는 없애면서 탐색하기 때문에 시간 복잡도를 줄임.

````python
def n_and_m(depth, n, m):
    if depth == m:
        print(' '.join(map(str, answer)))
    
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            answer.append(i)
            n_and_m(depth+1, n, m)
            visited[i] = False
            answer.pop()

n, m = map(int, input().split())
visited = [False] * (n+1)
answer = []

n_and_m(0, n, m)
````