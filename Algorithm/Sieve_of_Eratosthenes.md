# 에라토스테네스의 체
> 수학에서 에라토스테네스의 체는 소수를 찾는 방법이다.  
[wiki](https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4)

## 알고리즘
1. 2부터 소수를 구하고자 하는 구간의 모든 수를 나열.
2. 2는 소수이므로 미리 2를 써둔다.
3. 자기 자신을 제외한 2의 배수를 모두 지운다.
4. 남아있는 수 중 3은 소수이므로 써둔다.
5. 자기 자신을 제외한 3의 배수를 모두 지운다.
6. 남아있는 수 중 5는 소수이므로 써둔다.
7. 자기 자신을 제외한 5의 배수를 모두 지운다.
8. 남아있는 수 중 7은 소수이므로 써둔다.
9. 자기 자신을 제외한 7의 배수를 모두 지운다.
10. 위 과정을 반복하면 구하는 구간의 모든 소수가 남는다.

## 파이썬 코드 
````python
def prime_list(n):
    # 에라토스테네스의 채 초기화 : n개 요소에 True 설정
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i = sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True: #i가 소수라면
            for j in range(i + 1, n, i): # i이후 i 배수들을 False 판정
                sieve[j] = False
    
    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

````
### 결과
````
prime_list(20)
[2, 3, 5, 7, 11, 13, 17, 19]

max(prime_list(1000000))
999983
````