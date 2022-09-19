# 목차

## 레포지토리 위치 변경됨
### 상황
````
remote: This repository moved. Please use the new location:
````
git의 레포지토리 이름을 바꾸고 싶어서 바꾸었다가 그날부터 push는 되었지만, 계속 이와 같은 에러메시지가 떴다.

### 해결
현재 레포지토리 위치를 보는 명령어
````
git remote -v
````
레포지토리 위치를 업데이트 하는 명령어
````
git remote set-url origin 새로운 레포지토리 주소
````