# 목차
- [커밋 시간 변경하기](#1)
- [git 강제 푸쉬](#2)
## 커밋 시간 변경하기 <a id="1"></a>
### 최근 커밋 날짜를 현재 날짜로 변경
````
$ git commit --amend --no-edit --date "$(date)"
````

### 최근 커밋 날짜를 원하는 날짜로 변경
````
$ git commit --amend --no-edit --date "Fri 18 Feb 2022 01:35:10 KST"
````
> 요일, 일, 월, 년도, 시각, 한국시간기준 순서

## git 강제 푸쉬 <a id="2"></a>
````
$ git push -u origin master --force
````

## git reset: 커밋 취소 <a id="3"></a>
````
$ git log --oneline
````
### 깃의 로그를 확인

````
$ git reset --hard 커밋
````

### Untracked file들 삭제
````
# 삭제 대상(Untracked file) 목록 확인
$ git clean -n
````

````
# Untracked file 파일 삭제
$ git clean -f
````

### 바로 이전 상태를 돌리기
````
$ git reset --hard HEAD^
````