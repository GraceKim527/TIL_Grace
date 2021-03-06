# 목차
- [레이아웃을 구성하는 CSS 박스 모델](#cssbox)
- [이미지와 그라데이션 효과로 배경 꾸미기](#background)
- [CSS 고급 선택자](#selector)
- [트랜지션과 애니메이션](#transition)
- [반응형 웹과 미디어 쿼리](#mediaquery)

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

# CSS 고급 선택자<a id="selector"></a>
## 연결 선택자
### 하위 요소에 스타일을 적용하는 하위 선택자와 자식 선택자
#### 하위 선택자
부모 요소에 포함된 하위 요소를 모두 선택하며 자손 선택자라고도 한다. <br>
자식 요소뿐만 아니라 손자, 요소, 손자의 손자 요소 등 모든 하위 요소까지 적용된다.
````
상위요소 하위요소
````
ex) 하위 선택자를 사용하는 방법 <br>
section 요소 안에 포함된 p 요소를 모두 선택하려면 section과 p 사이에 **공백 한 칸**을 두고 나란히 써준다. 

````html
<section>
  <p> p 선택자요소 </p>
  <div>
    <p>첫번째</p>
  </div>
</section>
````
````css
section p { ...... }
````

#### 자식 선택자
하위 선택자와 다르게 자식 요소에만 스타일을 적용하는 선택자로, 부모 요소와 자식 요소를 구분한다.
````
부모요소 > 자식요소
````

ex) 자식 선택자 사용하는 방법
section 요소의 자식인 p 요소에만 스타일 적용
````html
<section>
  <h1>예약 방법 & 사용 요금</h1>
  <p>아직 온라인 예약 신청이...</p>
</section>
````

````css
section > p { ...... }
````

### 형제 요소에 스타일을 적용하는 인접 형제 선택자와 형제 선택자
#### 인접 형제 선택자
형제 요소 중에서 첫 번째 동생 요소만 선택하는 것
````
요소1 + 요소2
````
ex) 인접 형제 선택자를 사용하는 법
````html
<h1>예약 방법 & 이용 요금</h1>
<p>아직 온라인 예약 ...</p>
<p> 가족실 </p>
````

````css
h1 + p { color: blue; }
````

#### 형제 선택자
형제 요소의 스타일을 정의하는 데 인접 형제 선택자와 달리 모든 형제 요소에 적용된다.
````
요소1 ~ 요소2
````

ex) 형제 선택자를 사용하는 법 
````html
<h1>예약 방법 & 이용 요금</h1>
<p>아직 온라인 예약......</p>
<p>가족실</p>
<p>도미토리</p>
````

````css
h1 ~ p { color: blue; }
````

## 속성 선택자
### 특정 속성이 있는 요소를 선택하는 [속성] 선택자
a 요소 중에서 href 속성이 있는 요소를 선택하는 것이다. 
````css
a[href] { ... }
````

### 특정 속성값이 있는 요소를 선택하는 [속성 = 속성값] 선택자
주어진 속성과 속성값이 일치하는 요소를 찾아 스타일을 지정할 때 사용한다.<br>
ex)
````css
a[target = _blank] {......}
/* <a target = "_blank" >인 요소 */
````

### 여러 값 중에서 특정 속성값이 포함된 속성 요소를 선택하는 [속성 ~= 값] 선택자
여러 속성값 중에서 해당 속성값이 포함된 요소를 선택한다.
````css
[class ~= button] { ...... }
/* class값 중에 button이 있는 요소 */
````
button 글자가 포함된 class에만 다음 css가 적용된다.
````html
<ul>
  <li><a href="#" class="button">메뉴 1</a></li>
  <li><a href="#" class="flat button">메뉴 2</a></li>
</ul>
````

````css
[class ~= "button"] {
  /* 그림자 지정 */
  box-shadow: rgba(0, 0, 0, 0.4) 4px 4px;
  /* 모서리 둥글게 지정 */
  border-radius: 5px; 
}
````

### 특정 속성값이 포함된 속성 요소를 선택하는 [속성 |= 값] 선택자
특정 속성값이 포함된 속성에 스타일을 적용한다. 이때 속성값은 한 단어로 일치해야 한다. <br>
[속성 ~= 값]은 하이픈(-)으로 연결한 단어에 스타일을 적용하지 않는다는 점에서 차이가 있다. <br> 

ex)
````css
a[title |= us] { ...... }
/* 속성값이 'us'이거나 'us-'로 시작하는 a 요소를 찾는 선택자 */
````

### 특정 속성값으로 시작하는 속성 요소를 선택하는 [속성 ^= 값] 선택자
````css
a[title ^= eng] {.....}
````
속성값이 "eng"으로 시작하는 a 요소를 찾는 선택자입니다. 

### 특정한 값으로 끝나는 속성의 요소를 선택하는 [속성 $= 값] 선택자
````css
[href $= xls] {......}
````
주로 파일 확장자일 때 쓰이는 것 같다.

### 일부 속성값이 일치하는 요소를 선택하는 [속성 *= 값] 선택자
````css
[href *= w3] {.....}
````
'w3'가 포함된 요소를 선택한다.

## 가상 클래스와 가상 요소
### 사용자 동작에 반응하는 가상 클래스 
#### 방문하지 않은 링크에 스타일을 적용하는 ':link 가상 클래스 선택자'
- 텍스트 링크는 기본적으로 파란색 글자와 밑줄
- 이때 링크의 밑줄을 없애거나 색상을 바꾸기 위해 사용한다.

#### 방문한 링크에 스타일을 적용하는 ':visited 가상 클래스 선택자'
- 한 번 이상 방문한 텍스트 링크는 기본적으로 파란색이다.
- 사용자가 방문한 텍스트 링크와 색상이 달라지지 않게 하기 위해 사용한다.

#### 특정 요소에 마우스 포인터를 올려놓으면 스타일을 적용하는 ':hover 가상 클래스 선택자'
- 마우스 포인터를 올려놓을 때 스타일을 적용한다.

#### 웹 요소를 활성화했을 때 스타일을 적용하는 ':active 가상 클래스 선택자'
- 웹 요소의 링크나 이미지를 활성화했을 때, 즉 클릭했을 때 스타일을 지정한다.

#### 웹 요소에 초점이 맞추어졌을 때 스타일을 적용하는 ':focus 가상 클래스 선택자' 
- 텍스트 필드 안에 마우스 포인터를 올려놓거나, 웹 문서에서 tab 키를 눌러 입력 커서를 이동했을 때 스타일을 적용한다.

### 요소 상태에 따른 가상 클래스
#### 앵커 대상에 스타일을 적용하는 ':target 가상 클래스 선택자'
- 같은 문서 안에서 다른 위치로 이동할 때 앵커를 사용한다.
- 이때 앵커로 연결된 부분, 앵커의 목적지가 되는 부분의 스타일을 쉽게 적용할 수 있다. 

````html
<style>
  #intro:target{
    background-color: #0069e0;
    color: #fff;
  }
</style>
````

#### 요소의 사용 여부에 따라 스타일을 적용하는 ':enabled와 :disabled 가상 클래스 선택자'
- 해당 요소가 사용할 수 있는 상태라면 enabled 선택자 사용하고, 반대일 때는 disabled 선택자를 사용한다.
- 회원 약관 같은 글에 사용자가 입력할 수 없도록 disabled 속성을 적용해야 한다.

#### 선택한 항목의 스타일을 적용하는 ':checked 가상 클래스 선택자'
- 박스나 체크박스에 checked 속성이 추가되는데, 이때 스타일을 지정하고 싶다면 사용한다.

#### 특정 요소를 제외하고 스타일을 적용하는 ':not 가상 클래스 선택자'
````css
  #signup input:not([type=radio]){
    .....
  }
````

### 구조 가상 클래스
#### 특정 위치의 자식 요소 선택하기
- :only-child :: 부모 안에 자식 요소가 하나뿐일 때 자식 요소 선택
- A:only-type-of :: 부모 안에 A 요소가 하나뿐일 때 선택
- :first-child :: 부모 안에 있는 모든 요소 중에서 첫 번째 자식 요소 선택
- :last-child :: 부모 안에 있는 모든 요소 중에서 마지막 자식 요소 선택
- A:first-of-type :: 부모 안에 있는 A 요소 중에서 첫 번째 요소를 선택
- A:last-of-type :: 부모 안에 있는 A 요소 중에서 마지막 요소를 선택
- nth-child(n) :: 부모 안에 있는 모든 요소 중에서 n번째 자식 요소를 선택
- nth-last-child(n) :: 부모 안에 있는 모든 요소 중에서 끝에서 n번째 자식 요소 선택
- A:nth-of-type(n) :: 부모 안에 있는 A 요소 중에서 n번째 요소를 선택
- A:nth-last-of-type(n) :: 부모 안에 있는 A 요소 중에서 끝에서 n번째 요소를 선택

#### 수식을 사용해 위치 지정하기
````css
/* div 요소에서 홀수 번째 나타나는 자식인 p 요소에 스타일 적용 */
div p:nth-child(odd), div p:nth-child(2n+1)

/* div 요소에서 짝수 번째 나타나는 자식인 p 요소에 스타일 적용 */
div p:nth-child(even), div p:nth-child(2n)
````

### 가상 요소
#### 첫 번째 줄, 첫 번째 글자에 스타일을 적용하는 '::first-line 요소, ::first-letter 요소'
지정한 요소의 첫 번째 줄이나 첫 번째 글자에 스타일 적용할 수 있다.

#### 내용 앞뒤에 콘텐츠를 추가하는 '::before 요소, ::after 요소'
````css
li.new::after {
  content: "NEW!!";
  font-size: x-small;
  padding: 2px 4px;
  margin: 0 10px;
  border-radius: 2px;
}
````
# 트랜지션과 애니메이션 <a id="transition"></a>
## 변형 알아보기
### transform과 변형 함수
````css
.photo { transform: translate(50px, 100px);}
````
x축으로 50px, y축으로 100px 이동한다.

#### 2차원 변형과 3차원 변형
**2차원 변형**은 웹 요소를 평면에서 변형한다. <br>
x축은 오른쪽으로 갈수록 값이 커지고, y축은 아래로 내려갈수록 값이 커진다. <br>
**3차원 변형**은 x축과 y축에 원근감을 주는 z축을 추가해서 변형한다. <br>
z축은 앞뒤로 이동하며, 보는 사람 쪽으로 다가올수록 값이 커지고, 뒤로 갈수록 값이 작아진다.

#### 2차원 변형 함수
- translate(tx, ty) : 지정한 크기만큼 x축, y축으로 이동한다.
- translateX(tx) : 지정한 크기만큼 x축으로 이동한다.
- translateY(ty) : 지정한 크기만큼 y축으로 이동한다.
- scale(sx, sy) : 지정한 크기만큼 x축과 y축으로 확대, 축소한다.
- scale(sx) : 지정한 크기만큼 x축으로 확대, 축소한다.
- scale(sy) : 지정한 크기만큼 y축으로 확대, 축소한다.
- rotate(각도) : 지정한 각도만큼 회전한다.
- skew(ax, ay) : 지정한 각도만큼 x축과 y축으로 왜곡한다.
- skewX(ax) : 지정한 각도만큼 x축으로 왜곡한다.
- skewY(ay) : 지정한 각도만큼 y축으로 왜곡한다.

#### 3차원 변형 함수
- translate3d(tx, ty, tz) : 지정한 크기만큼 x축, y축, z축으로 이동한다.
- translateZ(tz) : 지정한 크기만큼 z축으로 이동한다.
- scaled3d(sx, sy, sz) : 지정한 크기만큼 x축, y축, z축으로 확대, 축소한다.
- scaleZ(sz) : 지정한 크기만큼 z축으로 확대, 축소한다.
- rotate(rx, ry, 각도) : 지정한 각도만큼 회전한다.
- rotate3d(rx, ry, rz, 각도) : 지정한 각도만큼 회전한다.
- rotateX(각도) : 지정한 각도만큼 x축으로 회전한다.
- rotateY(각도) : 지정한 각도만큼 y축으로 회전한다.
- rotateZ(각도) : 지정한 각도만큼 z축으로 회전한다.
- perspective(길이) : 입체적으로 보일 수 있도록 깊잇값을 지정한다.

## 트랜지션 알아보기
### 트랜지션이란
**트랜지션**은 웹 요소의 배경색을 바꾸거나 도형의 테두리를 사각형에서 원형으로 바꾸는 것처럼 스타일 속성이 바뀌는 것을 말한다. <br>

### 트랜지션과 속성
#### 트랜지션의 대상을 지정하는 transition-property 속성
````
transition-property: all | none | < 속성 이름 >
````
- all : 요소의 모든 속성이 트랜지션 대상이 된다. (기본값)
- none : 트랜지션을 하는 동안 아무 속성도 바뀌지 않는다.
- 속성 이름 : 트랜지션 효과를 적용할 속성을 지정한다.

#### 트랜지션의 진행 시간 지정하는 transition-duration 속성
````
transition-duration: <시간>
````

#### 트랜지션의 속도 곡선을 지정하는 transition-timing-function 속성
````
transition-timing-function: linear | ease | ease-in | ease-out | ease-in-out | cubic-bezier(n, n, n, n)
````
- ease : 처음에는 천천히 시작하고 빨라지다가 마지막엔 천천히 끝난다. (기본값)
- linear : 시작부터 끝까지 똑같은 속도로 진행한다.
- ease-in : 느리게 시작한다.
- ease-out : 느리게 끝낸다.
- ease-in-out: 느리게 시작하고 느리게 끝낸다.
- cubic-bezier(n, n, n, n): 베지에 함수를 정의해서 사용한다. n값은 0~1 사이만 사용할 수 있다. 

#### 트랜지션의 지연 시간을 설정하는 transition-delay 속성
지정한 시간만큼 기다렸다가 트랜지션 시작(초(s), 밀리초(ms), 기본값 (0))
````
transition-delay: <시간>
````

#### 트랜지션의 속성을 한꺼번에 표기하는 transition 속성
````
transition: <transition-property값> | <transition-duration값> | <transition-timing-function값> | <transition-delay값>
````

## 애니메이션 알아보기
### CSS 애니메이션에서 사용하는 속성
키프레임 :: 애니메이션 중간에 스타일이 바뀌는 시점

#### 애니메이션의 지점과 이름을 설정하는 @keyframes 속성, animation-name 속성 
````
@keyframes <이름> {
  <선택자> { <스타일 >}
}
````

어떤 애니메이션을 사용하는 지 이름으로 구분해야 한다. 
````
animation-name: <키프레임 이름> | none
````
@keyframes 속성에서 사용하는 선택자는 스타일 속성값이 바뀌는 지점을 가리킨다. <br>
시작, 끝을 각각 0%, 100%으로 놓고, 중간에 여러 프레임을 설정해도 된다. 

#### 애니메이션의 실행 시간을 지정하는 animation-duration 속성
````
animation-duration: <시간> 
````

#### 애니메이션의 방향을 지정하는 animation-direction 속성
````
animation-direction: normal | reverse | alternate | alternate-reverse
````
- normal: 애니메이션을 from에서 to로 진행한다. (기본값)
- reverse: 애니메이션을 to에서 from으로, 원래 방향과는 반대로 진행한다.
- alternate: 홀수 번째는 normal로, 짝수 번째는 reverse로 진행한다.
- alternate-reverse: 홀수 번째는 reverse로, 짝수 번째는 normal로 진행한다.

#### 반복 휫수를 지정하는 animation-iteration-count 속성
````
animation-iteration-count: < 숫자 > | infinite
````
- 숫자 : 애니메이션의 반복 휫수를 정한다.
- infinite : 애니메이션을 무한 반복한다. 

#### 애니메이션의 속도 곡선을 지정하는 animation-timing-function 속성
````
animation-timing-function: linear | ease | ease-in | ease-out | ease-in-out | cubic_bezier(n, n, n, n)
````

#### 애니메이션의 속성을 한꺼번에 표기하는 animation속성
````
animation: <animation-name> | <animation-duration> | <animation-timing-function> | <animation-delay> | <animation-iteraion-count> | <animation-direction>
````

# 반응형 웹과 미디어 쿼리 <a id="mediaquery"></a>
## 반응형 웹 알아보기
### 모바일 기기를 위한 뷰포트
**뷰포트** : 여러 화면에서 실제 내용이 표시되는 영역
````html
<meta name="viewport" content="속성1=값", "속성2=값", ......">
````
종류 | 설명 | 사용 가능 값 | 기본값 |
---- | ---- | ------------ | ------ |
width | 뷰포트 너비 | device-width 또는 크기 | 브라우저 기본값 |
height | 뷰포트 높이 | device-height 또는 크기 | 브라우저 기본값 |
user-scalable | 확대, 축소 가능 여부 | yes 또는 no | yes |
initial-scale | 초기 확대, 축소 값 | 1 ~ 10 | 1 |

**가장 많이 사용하는 뷰포트 속성**
````html
<meta name="viewport" content="width=device-width, initial-scale=1">
````

### 뷰포트 단위
- vw(viewport width): 1vw는 뷰포트 너비의 1%와 같다.
- vh(viewport height): 1vh는 뷰포트 높이의 1%와 같다.
- vmin(viewport minimum): 뷰포트의 너비와 높이 중에서 작은 값의 1%와 같다.
- vmax(viewport maximum): 뷰포트의 너비와 높이 중에서 큰 값의 1%와 같다.


## 미디어 쿼리 알아보기
### 미디어 쿼리
-> 사이트에 접속하는 장치에 따라 특정한 CSS 스타일을 사용하는 방법

````
@media [only | not] 미디어 유형 [and 조건] * [and 조건]
````
- only: 미디어 쿼리를 지원하지 않는 웹 브라우저에서는 미디어 쿼리를 무시하고 실행을 하지않는다.
- not: not 다음에 지정하는 미디어 유형을 제외한다.
- and: 조건을 여러 개 연결해서 추가 가능하다.

#### 미디어 유형의 종류
- all: 모든 미디어 유형
- print: 인쇄 장치
- screen: 컴퓨터 스크린, (스마트폰 스크린도 포함)
- tv: 음성과 영상이 동시에 출력되는 TV에서 사용 
- aural: 음성 합성 장치
- braille: 점자 표시 장치
- handheld: 패드(pad)
- projection: 프로젝터
- tty: 디스플레이 기능이 제한된 장치에 맞는 유형, 이런 장치에서는 px 사용 불가
- embossed: 점자 프린터

#### 웹 문서의 가로 너비와 세로 높이 속성
실제 웹 문서 내용이 화면에 나타나는 영역을 뷰포트라고 하는데, 뷰포트의 너비와 높이를 미디어의 쿼리 조건으로 사용가능. <br>
- width, height: 웹 페이지의 가로 너비, 세로 높이
- min-width, min-height: 웹 페이지의 최소 너비, 최소 높이
- max-width, max-height: 웹 페이지의 최대 너비, 최대 높이

#### 단말기의 가로 너비와 세로 높이 속성
대부분의 단말기 해상도와 실제 브라우저의 너비가 다르다. 
- device-width, device-height: 단말기의 가로 너비, 세로 높이를 지정
- min-device-width, min-device-height: 단말기의 최소 너비, 최소 높이를 지정
- max-device-width, max-device-height: 단말기의 최대 너비, 최대 높이를 지정

#### 화면 회전 속성 
스마트폰이나 태블릿에서는 화면을 세로로 보거나 가로로 돌려서 볼 수가 있는데, 이때 미디어 쿼리에서 **orientation** 속성을 사용하면 기기의 방향을 확인 가능하다.<br>
가로 모드는 landscape, 세로 모드는 portrait이다.
- orientation: portrait :: 세로 모드로 지정
- orientation: landscape :: 가로 모드로 지정

#### 미디어 쿼리의 중단점 
**중단점** : 미디어 쿼리를 작성할 때 화면 크기에 따라 서로 다른 css를 적용할 분기점<br>
주로 모바일, 태블릿, 데스크톱 정도로만 구분하면 좋다. <br>
**모바일 퍼스트 기법** : 모바일을 먼저 고려하여 미디어 쿼리를 작성하는 것
- 스마트폰 : 모바일 페이지는 미디어 쿼리를 사용하지 않고 기본 css로 작성한다. 만약 스마트폰의 방향까지 고려한다면 min-width의 세로와 가로를 각각 portrait 320px, landscape 480px로 지정한다.
- 태블릿 : 세로 크기가 768px이상이면 태블릿으로 지정한다. 가로 크기는 데스크톱과 똑같이 1024px 이상으로 지정한다.
- 데스크톱 : 화면 크기가 1024px이상이면 데스크톱으로 설정한다. 
