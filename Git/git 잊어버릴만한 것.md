# 목차

## 커밋 시간 변경하기
### 최근 커밋 날짜를 현재 날짜로 변경
````
$ git commit --amend --no-edit --date "$(date)"
````

### 최근 커밋 날짜를 원하는 날짜로 변경
````
$ git commit --amend --no-edit --date "Fri 18 Feb 2022 01:35:10 KST"
````
> 요일, 일, 월, 년도, 시각, 한국시간기준 순서

## git 강제 푸쉬
````
$ git push -u origin master --force
````
