# 파이썬 코딩테스트 팀노트

## 2차원 리스트를 90도 회전한 결과를 반환하는 함수
````python
def rotate_a_matrix_by_90_degree(a):
    n = len(a) # 행 길이
    m = len(a[0]) # 열 길이
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result
````