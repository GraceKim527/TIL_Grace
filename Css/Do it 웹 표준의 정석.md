# 목차
- [레이아웃을 구성하는 CSS 박스 모델](#cssbox)
- [이미지와 그라데이션 효과로 배경 꾸미기](#background)

# 레이아웃을 구성하는 CSS 박스 모델 <a id="cssbox"></a>
## 1. CSS와 박스 모델
### 블록 레벨 요소와 인라인 레벨 요소
**블록 레벨 요소** : 태그를 사용해 요소를 삽입했을 때 혼자 한 줄을 차지하는 것
- ex) < h1 > < div > < p > 

**인라인 레벨 요소** : 콘텐츠만큼만 영역을 차지하고 나머지 공간에는 다른 요소가 차지 가능
- ex) < span > < img > < strong >

### 박스 모델의 크기를 계산하는 box-sizing 속성
````css
.box1 {
    /* 테두리까지 포함해서 너빗값 지정 */
    box-sizing: border-box; 
    /* 콘텐츠 영역만 너빗값을 지정(기본값) */
    box-sizing: content-box;
}
````

### 박스 모델에 그림자 효과를 주는 box-shadow 속성
````css
.box1 {
    box-shadow : <수평거리> <수직거리> <흐림 정도> <번짐 정도> <색상> inset;
}
````
- (필수)수평거리 : 그림자가 가로로 얼마나 떨어져 있는지(양수값은 오른쪽, 음수값은 왼쪽)
- (필수)수직거리 : 그림자가 세로로 얼마나 떨어져 있는지(양수값은 아래쪽, 음수값은 위쪽)
- 흐림 정도 : 값이 커질수록 부드러운 그림자로 표시, 음수값 불가
- 번짐 정도 : 양수값을 사용하면 모든 방향으로 그림자가 퍼진다. 음수값은 모든 방향으로 그림자 축소
- 색상 : 색상 여러 개도 가능
- inset : 안쪽 그림자로 그린다.

## 2. 테두리 스타일 지정하기
### 꼭짓점마다 따로 둥글게 처리하기
ex) 왼쪽 윗부분 꼭짓점이면 border-top-left-radius
- top-left, top-right, bottom-left, bottom-right 등

## 3. 여백을 조절하는 속성
### 요소 주변의 여백을 설정하는 margin 속성
````css
.box1 {
    margin: <크기> | <백분율> | auto;
}
````
- 크기 : 너빗값이나 높잇값을 px, em 등으로 설정
- 백분율 : 부모 요소를 기준으로 퍼센트로 지정
- auto : display 속성에서 지정한 값에 맞게 적절한 값을 자동으로 지정

### 마진 중첩 이해하기
**마진 중첩** : 세로로 배치할 경우에 각 요소의 마진과 마진이 서로 만나면 마진값이 큰 쪽으로 겹쳐지는 문제
- 여러 요소를 세로로 배치할 때 맨 위 마진과 맨 아래 마진에 비해 중간 마진이 지나치게 커지는 것을 방지하기 위해 생긴다. 

## 4. 웹 문서의 레이아웃 만들기
### 배치 방법 결정하는 display 속성
````css
.container {
    display: block;
}
````
- block : 인라인 레벨 요소를 블록 레벨 요소로 만든다
- inline : 블록 레벨 요소를 인라인 레벨 요소로 만든다.
- inline-block : 인라인 레벨 요소와 블록 레벨 요소 속성을 모두 가지며, 마진과 패딩 지정 가능
- none : 화면에 표시하지 않는다.

### 왼쪽이나 오른쪽으로 배치하는 float 속성
**float** : 웹 요소를 문서 위에 떠 있게 만든다. 
- left: 해당 요소를 문서 왼쪽에 배치한다.
- right: 해당 요소를 문서 오른쪽에 배치한다.
- none: 좌우 어디에도 배치 안한다.(기본값)

float속성이 더 이상 유효하지 않게 하려면 clear을 사용한다.

## 5. 웹 요소의 위치 지정하기
### 웹 요소를 지정하는 left, right, top, bottom 속성
````css
.item {
    left: 50px;
    right: 20px; 
}
````
- left: 기준 위치와 요소 사이에 왼쪽으로 얼마나 떨어져 있는지 지정한다. 
- right: 기준 위치와 요소 사이에 오른쪽으로 얼마나 떨어져 있는지 지정한다. 
- top: 기준 위치와 요소 사이에 위쪽으로 얼마나 떨어져 있는지 지정한다. 
- bottom: 기준 위치와 요소 사이에 아래쪽으로 얼마나 떨어져 있는지 지정한다. 

### 배치 방법을 지정하는 position 속성
````css
.item {
    position: static;
}
````
- static: 문서의 흐름에 맞게 배치한다.(기본값)
- relative: 위치값을 지정할 수 있다는 점을 제외하면 static과 같다.
- absolute: relative값을 사용한 상위 요소를 기준으로 위치를 지정해 배치한다.
- fixed: 브라우저 창 기준으로 위치를 지정해 배치한다.


# 이미지와 그라데이션 효과로 배경 꾸미기 <a id="background"></a>
## 배경색과 배경 범위 지정하기
### 배경색을 지정하는 background-color 속성
16진수나 rgb값, 색상 이름을 사용하여 지정한다.
````css
.color {
    background-color: #008000;
    background-color: rgb(0, 128, 0);
    background-color: green;
}
````

### 배경색의 적용 범위를 조절하는 background-clip 속성
````css
.bc {
    background-clip: border-box;
    background-clip: padding-box;
    background-clip: content-box;
}
````
- border-box: 박스 모델의 가장 외각인 테두리까지 적용한다.(기본값)
- padding-box: 박스 모델에서 테두리를 뺀 패딩 범위까지 적용한다.
- content-box: 박스 모델에서 내용 부분에만 적용한다.

## 배경 이미지 지정하기
### 웹 요소에 배경 이미지를 넣는 background-image 속성
````
background-image: url('이미지 경로')
````
이미지 파일은 .jpg, .gif, .png 형식을 사용한다.

### 배경 이미지의 반복 방법을 지정하는 background-repeat 속성
- repeat: 브라우저 화면 가득 찰 때까지 가로와 세로로 반복한다.(기본값)
- repeat-x: 브라우저 화면 너비에 가득 찰 때까지 반복한다.
- repeat-y: 브라우저 화면 높이에 가득 찰 때까지 반보갛낟.
- no-repeat: 한 번만 표시하고 반복하지 않는다.

### 배경 이미지의 위치를 조절하는 background-position 속성
````
background-position: <수평 위치> <수직 위치>;
수평 위치 : left | center | right | <백분율> | <길이 값>
수직 위치 : top | center | bottom | <백분율> | <길이 값>
````

### 배경 이미지의 적용 범위를 조절하는 background-origin 속성
- content-box: 박스 모델에서 내용 부분만 배경 이미지를 표시한다.(기본값)
- padding-box: 박스 모델에서 패딩까지 배경 이미지를 표시한다.
- border-box: 박스 모델에서 테두리까지 배경 이미지를 표시한다.

### 배경 이미지를 고정하는 background-attachment 속성
- scroll: 화면을 스크롤하면 배경 이미지도 스크롤된다.(기본값)
- fixed: 화면을 스크롤하면 배경 이미지는 고정되고 내용만 스크롤된다.

### 배경 이미지 크기를 조절하는 background-size 속성
- auto: 배경 이미지 크기만큼 표시한다.(기본값)
- contain: 요소 안에 배경 이미지가 다 들어오도록 이미지 확대 및 축소
- cover: 배경 이미지로 요소를 모두 덮도록 이미지 확대 및 축소
- <크기> 및 <백분율>

## 그러데이션 효과로 배경 꾸미기
### 선형 그러데이션
````
linear-gradient(to <방향> | <각도>, <색상 중지점> [<색상 중지점>, ...]);
````
#### 방향
왼쪽에서 오른쪽 : to right <br>
왼쪽 아래에서 오른쪽 위 : to right top || to top right 등으로 사용된다.

#### 각도
맨 윗부분이 0deg, 시계 방향으로 회전하면서 90deg, 180deg가 된다.

#### 색상 중지점
그라데이션에서 바뀌는 색을 색상 중지점이라 한다.

### 원형 그러데이션
````
radial-gradient(<모양> <크기> at <위치>, <색상 중지점>, [<색상 중지점>, ......])
````

#### 모양
원형(circle), 타원형(ellipse)이다.

#### 크기 

#### 위치
at 키워드를 통해 원의 중심을 다르게 나타낼 수 있다.<br>
위치 속성값은 키워드(left, center, right 중 하나 | top, center, bottom )
