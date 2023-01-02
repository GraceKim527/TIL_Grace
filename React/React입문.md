# 목차
> '리액트를 다루는 기술' 책을 참고하여 작성하였습니다.

- [4. 이벤트 핸들링](#4)

## 이벤트 핸들링 <a id="4"></a>
### 이벤트 핸들링 시 주의할 사항
- 이벤트 이름은 카멜 표기법(onClick)
- 자바스크립트 코드를 전달하는 것이 아니라, 함수 형태의 값을 전달.
- DOM 요소에만 이벤트를 설정 가능.

### onChange 이벤트
````javascript
import React, { Component } from 'react';

class EventPractice extends Component {
    render() {
        return (
            <div>
                <h1>이벤트 연습</h1>
                <input type="text"
                name="message"
                placeholder='아무거나 입력해보세요'
                onChange={
                    (e) => {
                        console.log(e.target.value);
                    }
                }
                />
            </div>
        );
    }
}

export default EventPractice;
````
위와 같이 하면 console에 앞으로 변할 인풋 값이 계속 기록된다.

- 이벤트에 실행할 자바스크립트 코드를 전달하는 것이 아니라, 함수 형태의 값을 전달한다.
