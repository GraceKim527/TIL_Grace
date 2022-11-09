# 야곰 스위프트 초보문법 강좌 강의노트

## 이름짓기, 콘솔로그, 문자열 보간법
### 콘솔로그 
print - 단순 문자열 출력
dump - 인스턴스의 자세한 설명까지 출력

### 문자열 보간법
` \() ` 사용

## 상수와 변수
상수 선언 키워드 - let
변수 선언 키워드 - var

## 기본 데이터 타입
Swift는 데이터 타입 교환이 굉장히 어려운 언어임.
- Bool  
````swift
var someBool: Bool = true
// 0, 1 불가
````
- Int  
````swift
var someInt: Int = -100
````
- UInt  
````swift
var someUnit: UInt = 100
// Int와 사용 불가
````
- Float, Double
// Float, Double 간의 사용 불가

## Any, AnyObject, Nil
any - swift의 모든 타입을 지칭하는 키워드  
Anyobject - 모든 클래스 타입을 지칭하는 프로토콜  
nil - 없음을 의미하는 키워드  

Any
````swift
var someAny: Any = 100
someAny = "어떤 타입도 수용 가능"
someAny = 123.12

//let someDouble: Double = someAny 
// 위와 같은 경우는 안됨.
````

AnyObject
````swift
class SomeClass {}

var someAnyObject: AnyObject = Someclass()
````

nil
- null, Null, NULL 등 과 비슷함.

## 컬렉션 타입 Array, Dictionary, Set
- Array
순서가 있는 리스트 컬렉션
````swift
var integers: Array<Int> = Array<Int>()
integers.append(1) // 요소 뒤에 추가
integers.append(100)
//integers.append(199.1) // 오류

// 포함되어 있는지 여부
integers.contains(100) // true
integers.contains(99) // false

integers.remove(at: 0) // 0번째 인덱스를 삭제한다
integers.removeLast() // 마지막 멤버 삭제
integers.removeAll() // 전부 삭제

integers.count // 몇개 들어있는지

// Array<Double> 과 [Double]은 동일한 표현
// 빈 Double Array 생성
var doubles: Array<Double> = [Double]()

// 빈 String Array 생성
var strings: [String] = [String]()

// 빈 Character Array 생성
// []으로도 생성 가능
var charcters: [Character] = []

// let으로 선언하면 변경 불가
let immutableArray = [1, 2, 3]

````

- Dictionary
키와 값의 쌍으로 이루어진 컬렉션
````swift
// Key가 String 타입이고 Value가 Any인 빈 딕셔너리
var anyDictionary: Dictionary<String, Any> = [String: Any]()

anyDictionary["someKey"] = "value"
anyDictionary["anotherKey"] = 100

anyDictionary

anyDictionary["someKey"] = "dictionary"

// 둘이 유사
anyDictionary.removeValue(forKey: "anotherKey")
anyDictionary["someKey"] = nil

let emptyDictionary: [String: String] = [:] // 빈 딕셔너리 표현
let initalizedDictionary: [String: String] = ["name": "yagom", "gender": "male"]

// 오류 발생 :: 불확실성 때문에 발생
let someValue: String = initalizedDictionary["name"]
````

- Set 
순서가 없고, 멤버가 유일한 컬렉션
````swift
// 빈 Int Set 생성
var integerSet: Set<Int> = Set<Int>()
integerSet.insert(1)
integerSet.insert(100)
integerSet.insert(99)
integerSet.insert(99)
integerSet.insert(99)

integerSet
integerSet.contains(1) // true
integerSet.contains(2) // false

integerSet.remove(100)
integerSet.removeFirst()

integerSet.count

let setA: Set<Int> = [1, 2, 3, 4, 5]
let setB: Set<Int> = [3, 4, 5, 6, 7]

let union: Set<Int> = setA.union(setB)
let sortedUnion: [Int] = union.sorted()

let intersection: Set<Int> = setA.intersection(setB)
let subtracting: Set<Int> = setA.subtracting(setB)
````

## 함수
- 반환 값이 있는 함수
````
func 함수이름(매개변수1 이름: 매개변수1타입, 매개변수2이름: 매개변수2타입 ...) -> 반환타입 {
    함수 구현 부
    return 반환값
}
````

### 반환 값이 없는 함수
````
func 함수이름(매개변수1 이름: 매개변수1타입, 매개변수2이름: 매개변수2타입 ...) -> void {
    함수 구현 부
    return 
}
````
또는 반환 타입 화살표를 **생략도 가능**

### 매개변수가 있는 함수
````
func 함수이름(매개변수1이름: 매개변수1타입, 매개변수2이름: 매개변수2타입 ...){
    함수 구현 부
    return
}
````

### 매개변수가 없는 함수
````
func 함수이름() -> 반환타입 {
    함수 구현 부
    return 반환 값
}
````

## 함수 심화
### 함수 호출 방법
````swift
sum(a: 3, b: 5) // 8
printMyname(name: "gracekim") // gracekim


// 기본값을 갖는 매개변수는 매개변수 목록 중에 뒤쪽에 배치하는게 좋음.

func greeting(friend: String, me: String = "Yagam"){
    print("Hello \(friend)! I'm \(me)")
}

// 매개변수 기본값을 가지는 매개변수는 생략 가능
greeting(friend: "hana")
greeting(friend: "john", me: "eric")

// 전달인자 레이블
// 함수 사용자 입장에서 표현하고자 할 때 사용
func greeting(to friend: String, from me: String){
    print("Hello \(friend)! I'm \(me)")
}

greeting(to: "hana", from: "gracekim")

// 가변 매개변수

// 전달 받을 값의 개수를 알기 어려울 때 사용,
// 함수당 하나만 가능

func sayHelloToFriends(me: String, friends: String...) -> String {
    return "Hello \(friends)! I'm \(me)!"
}

// 스위프트는 함수형 프로그래밍 패러다임을 포함하는 다중 패러다임 언어
// 스위프트 함수는 일급객체라 변수, 상수 등에 저장이 가능
// 매개변수를 통해 전달 가능

var someFunction: (String, String) -> Void = greeting(to:from:)
someFunction("eric", "gracekim")
````

## if-else문, switch문
### if-else 문
````swift
let someInteger = 100

// if-else

if someInteger < 100 { 
    print("100 미만")
} else if someInteger > 100 {
    print("100 초과")
} else {
    print("100")
}

````
- 스위프트 조건은 항상 Bool 타입이여야 한다.
- 조건쪽에 소괄호는 생략 가능, 중괄호는 생략 불가

### switch 문

````swift

switch someInteger {
case 0:
    print("zero")
case 1..<100:
    print("100")
case 100:
    print("100")
case 101...Int.max:
    print("over 100")
default:
    print("unknown")
}

// 정수 외의 대부분은 기본 타입 사용 가능
switch "gracekim" {
case "jake":
    print("jake")
    fallthrough 
case "mina":
    print("mina")
case "gracekim":
    print("gracekim")
default:
    print("unknown") // default는 꼭 작성하는 것이 좋다.
}
````

- 범위 연산자를 활용하면 더욱 쉽고 유용하다.
- 기본적으로 break가 되어 있다.
- `fallthrough`를 사용하면 기존 break를 쓰지 않는 것과 동일하게 작동한다.

## 반복문 for-in, while, repeat-while
### for-in
````swift
for integer in integers{
    print(integer)
}

// dictionary의 item은 key, value로 구성
for (name, age) in people {
    print("\(name): \(age)")
}
````

### while
````swift
while integers.count > 1{ //조건에는 무조건 bool 값
    integers.removeLast()
}
````

### repeat-while
````swift 
repeat {
    integers.removeLast()
} while integers.count > 0
// 기존 do-while과 비슷하다

````

## 옵셔널(핵심)
- Optional :: 값이 있을 수도 있고, 없을 수도 있다.

### 옵셔널이 왜 필요한가?
- nil의 가능성을 명시적으로 표현하는 것
    - nil 가능성을 문서화하지 않아도 코드만으로 충분히 가능
    - 전달받은 값이 옵셔널이 아니라면 nil체크를 하지 않더라도 안심하고 사용 가능

### 옵셔널의 표현 
````swift
let optionalValue: Optional<Int> = nil
let optionalValue: Int? = nil
````

### 암시적 추출 옵셔널(!)
````swift
var optionalValue: Int! = 100

switch optionalValue {
    case .none:
    print("This Optional variable is nil")
    case .some(let value):
    print("Value is \(value)")
}
````

- 기존 변수 처럼 사용 가능   
ex) `optionalValue = optionalValue +1`

- nil 할당 가능  
ex) `optionalValue = nil`

### 일반적인 옵셔널(?)
````swift
var optionalValue: Int? = 100 // int가 있을 수도 있고, 없을 수도 있는

switch optionalValue {
    case .none:
    print("This Optional variable is nil")
    case .some(let value):
    print("Value is \(value)")
}
````

- nil 할당 가능  
ex) `optionalValue = nil`

- 기존 변수 처럼 사용 **불가** (옵셔널과 일반 값은 다른 타입)  
ex) `optionalValue = optionalValue +1`

## 옵셔널 추출(optional unwrapping)
- 옵셔널의 값을 꺼내오는 방법 중 하나( nil 체크 + 안전한 값 추출 )
- 옵셔널 타입은 보호막이 하나씩 있는다고 생각( 값이 있을 수도 있고, 없을 수도 있다. 보호막에 값이 있는지 물어보는 느낌)
````swift
func printName(_ name: String) {
    print(name)
}
var myName: String! = nil //컴파일 오류 String과 String!은 다름
````

## 구조체
````swift
struct Sample {
    var mutableProperty: Int = 100 // 가변 프로퍼티
    let immutableProperty: Int = 100 // 불변 프로퍼티

    static var typeProperty: Int = 100 //타입 프로퍼티

    // 인스턴스 메서드
    func instanceMethod() {
        print("instance method")
    }

    // 타입 메서드
    static func typeMethod(){
        print("type method")
    }
}
````

- 구조체 사용

````swift
// 가변 인스턴스
var mutable: Sample = Sample()

let immutable: Sample = Sample()


Sample.typeProperty = 300
Sample.typeMethod() // type method


````