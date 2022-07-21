# Markdown 문법 
## Markdown
> 일반 텍스트 기반의 마크업언어로 README.md 파일이나 온라인 문서, 혹은 일반 텍스트 편집기로 문서 양식을 편집할 때 쉽게 쓰고 읽을 수 있으며 HTML로 변환이 가능하다.

## 문법 구분을 위한 강제 개행
: 문단을 구별하려면 한 개 이상의 빈 줄을 문단 사이에 삽입하거나, **줄의 마지막에 [Space Bar]를 두 번 이상 눌러 띄어쓰기**하면 된다.

## 헤더(Header)
````
# 헤더 (h1)
## 헤더 (h2)
### 헤더 (h3)
#### 헤더 (h4)
##### 헤더 (h5)
````

## 목록(Lists)
Unordered
* Item 1
* Item 2
    * Item 2a
    * Item 2b

Ordered
1. Item 1
1. Item 2
1. Item 3
    1. Item 3a
    1. Item 3b

## 이미지
첫번째 방법  
! [Github logo] (.../.jpg)  
Format : ![이미지 alt명] (url링크)  
  
두번째 방법  
````html
<a href="#"><img src="주소 or .../jpg">
````
Format : img태그 사용 - 이미지경로는 상대경로 or 절대경로 

## 하이퍼링크(Links)
````
[Github](http://github.com "깃허브")
````

## 코드 블록(Code Blocks)
`*4 언어이름

## 인용 상자(Blockquotes)
````
asdfasdf 

> dasdfas 
````

## 강조(Emphasis)
````
*This text will be italic*
_This will also be italic_

**This text will be bold**
__This will also be bold__

*You **can** combine them*
````

## 테이블 TABLES
````
First Header | Second Header 
------------ | -------------
Content Cell 1 | Content Cell 2
Content column 1 | Content column 2
````

## 체크 박스(Task Lists)
````
- [x] 1번 문항 
- [ ] 2번 문항
- [x] 3번 문항
````
- [x] 1번 문항
- [ ] 2번 문항
- [x] 3번 문항

## 인라인 코드(Inline code)
````
문단 중간에 `code`를 넣을 수 있다.
````

## 수평선(hr)
````
---
***
---
````

## 탈출 문자(Backslash Escape)
````
\*iteral asteriks\*
_\_Tom\__
````

## 이모지(EMOJI) - 아이콘
:octocat: