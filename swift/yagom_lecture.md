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

// 타입 프로퍼티 및 메서드
Sample.typeProperty = 300
Sample.typeMethod() // type method

````

- 예시
````swift
struct Student {
    var name: String = "unknown"
    var `class`: String = "Swift" // class는 기존키워드이기 때문에 따로 사용하고 싶으면 `으로 묶어주면된다.
    
    static func selfIntroduce(){ //타입 메서드
        print("학생타입입니다")
    }
    
    func selfIntroduce(){
        print("저는 \(self.class)반 \(name)입니다")
    }
}

Student.selfIntroduce()

var yagom: Student = Student()
yagom.name = "yagom"
yagom.class = "스위프트"
yagom.selfIntroduce() // 저는 스위프트반 yagom입니다.

let jina: Student = Student()

//jina.name = "jina" -> 불변 프로퍼티이므로 불가
jina.selfIntroduce()


````

## 클래스
- 사용 방법
````swift
class Sample {
    var mutableProperty: Int = 100 // 가변 프로퍼티
    let immutableProperty: Int = 100 // 불변 프로퍼티
    static var typeProperty: Int = 100 // 타입 프로퍼티
    
    // 인스턴스 메서드
    func instanceMethod() {
        print("instance method")
    }
    
    // 타입 메서드
    // 재정의 불가 타입 메서드 - static
    static func typeMethod() {
        print("type method - static")
    }
    
    // 재정의 가능 타입 메서드 - class
    class func classMethod() {
        print("type method - class")
    }
}


````

- 클래스의 사용
````swift
// MARK: 클래스 사용
var mutableReference: Sample = Sample()

mutableReference.mutableProperty = 200

let immutableReference: Sample = Sample()
immutableReference.mutableProperty = 200 // 불변형이여도 내부 프로퍼티 값은 변경할 수 있다.

// 타입 프로퍼티 및 메서드
Sample.typeProperty = 300
Sample.typeMethod() // type method
````

**구조체와는 다르게 기변 프로퍼티를 let으로 선언했음에도 프로퍼티를 새로 값을 할당해도 사용이 가능하다**

## 열거형
- 사용

````swift
// MARK: 사용
enum Weekday {
    case mon
    case tue
    case wed
    case thu, fri, sat, sun
}

var day: Weekday = Weekday.mon // day의 타입으로 지정
day = .tue // 이렇게 축약해서 사용 가능

print(day)

switch day {
case .mon, .tue, .wed, .thu:
    print("평일입니다")
case Weekday.fri:
    print("불금 파티 !!")
case .sat, .sun:
    print("신나는 주말!!")
}
````
- 케이스를 전부 구현하면 default를 구현할 필요가 없지만, 하나라도 빠진다면 구현해야한다.

### 원시값
````swift
// C언어의 enum처럼 정수값을 가질 수 있다
// rawValue 사용
// case별로 다른 값을 가져야 한다

enum Fruit: Int {
case apple = 0;
case grape = 1; // 1을 지우더라도 1씩늘어나서 자동으로 값이 들어간다.
    case peach
    
}

print("Fruit.peach.rawValue == \(Fruit.peach.rawValue)")
// Fruit.peach.rawValue == 2

// 정수 타입 뿐 아니라
// Hasshable 프로토콜을 따르는 모든 타입이 원시값의 타입 가능

enum School: String {
    case elementary = "초등"
    case middle = "중등"
    case `high` = "고등"
    case university
}

print("School.middle.rawValue == \(School.middle.rawValue)")

print("School.university.rawValue == \(School.university.rawValue)")
// 이 경우 이름 그대로 나온다.
````

- 원시값을 통한 초기화
    - rawValue를 통해 초기화 가능
    - rawValue가 case에 해당하지 않을 수 있기 때문에
    - rawValue를 통한 초기화 한 인스턴스는 옵셔널 타입

````swift 
let apple: Fruit? = Fruit(rawValue: 0)
// let apple: Fruit = Fruit(rawValue: 0)

if let orange: Fruit = Fruit(rawValue: 5){
    print("rawValue 5에 해당하는 케이스는 \(orange)입니다")
} else {
    print("rawValue 5에 해당하는 케이스가 없습니다")
}
````

- 메서드 추가 가능 
````swift
enum Month {
    case dec, jan, feb
    case mar, apr, may
    case jun, jul, aug
    case sep, oct, nov
    
    func printMessage() {
        switch self {
        case .mar, .apr, .may:
            print("봄")
        case .jun, .jul, .aug:
            print("여름")
        case .sep, .oct, .nov:
            print("가을")
        case .dec, .jan, .feb:
            print("겨울")
        }
    }
}

Month.mar.printMessage()

````

## 값 타입과 참조 타입
### Class
- 단일상속, 전통적인 OOP 관점에서의 클래스
- (인스턴스/타입) 메서드
- (인스턴스/타입) 프로퍼티
- **참조 타입**
- 애플 프레임워크의 대부분 큰 뼈대는 모두 클래스로 구성

### 구조체
- C 언어 등의 구조체보다 다양한 기능
- (인스턴스/타입) 메서드
- (인스턴스/타입) 프로퍼티
- 상속 불가
- **값 타입**
- Swift의 큰 뼈대는 모두 구조체로 구성

### 열거형
- 상속 불가
- **값 타입**
- (인스턴스/타입) 메서드
- (인스턴스/타입) 프로퍼티
- 열거형 자체가 하나의 데이터 타입, 케이스 하나하나 전부 유의미한 값

### 구조체는 언제 사용하는 가?
- 연관된 몇몇의 값들을 모아서 하나의 데이터타입으로 표현하고 싶을 때
- 참조가 아닌 복사를 원할 때
- 자신을 상속할 필요가 없거나, 자신이 다른 타입을 **상속받을 필요가 없을 때**
- 애플 프레임워크에서 프로그래밍 할 때는 주로 클래스를 많이 사용

### Value vs Reference
- Value 
    - 데이터를 전달할 때 값을 복사하여 전달
- Reference 
    - 데이터를 전달할 때 값의 메모리 위치 전달

## 클로저 기본 
- 코드의 블럭
- 일급 시민(first-citizen)
- 변수, 상수 등으로 저장, 전달인자로 전달이 가능

````
(매개변수 목록) -> 반환타입 in
    실행코드
````

````swift

func sumFunction(a: Int, b: Int) -> Int {
    return a + b
}

var sumResult: Int = sumFunction(a: 1, b: 2)

print(sumResult)

var sum: (Int, Int) -> Int = { (a: Int, b: Int) -> Int in
    return a + b
}

sumResult = sum(1, 2)
print(sumResult)

// 함수는 클로저의 일종이므로
// sum 변수에 당연히 함수도 할당가능
sum = sumFunction(a:b:)

sumResult = sum(1, 2)
print(sumResult) // 3

````

## 프로퍼티
### 정의
- 프로퍼티는 구조체, 클래스, 열거형 내부에 구현할 수 있다
- 열거형 내부에는 연산 프로퍼티만 구현할 수 있다
- 연산 프로퍼티는 **var로만** 선언가능

````swift
struct Student {
    // 인스턴스 저장 프로퍼티
    var name: String = ""
    var `class`: String = "Swift"
    var koreanAge: Int = 0
    
    // 인스턴스 연산 프로퍼티
    var westernAge: Int {
        get {
            return koreanAge - 1
        }
        
        set(inputValue) {
            koreanAge = inputValue + 1
        }
    }
    
    // 타입 저장 프로퍼티
    static var typeDescription: String = "학생"
    
    // 인스턴스 메서드
//    func selfIntroduce() {
//        print("저는 \(self.class)반 \(name)입니다")
//    }
    
    //읽기전용 인스턴스 연산 프로퍼티
    var selfIntroduction: String {
        get {
            return "저는 ~~"
        }
    }
}
````

## 프로퍼티 감시자
- 프로퍼티 값이 변경될 때 원하는 동작 수행 가능
### 정의
````swift
struct Money {
    // 프로퍼티 감시자
    var currentRate: Double = 1100 {
        willSet(newRate) {
            print("환율이 \(currentRate)에서 \(newRate)으로 변경 예정")
        }
        didSet(oldRate) {
            print("환율이 \(oldRate)에서 \(currentRate)으로 변경")
        }
    }
    
    var dollar: Double = 0 {
        willSet {
            print("\(dollar)달러에서 \(newValue)달러로 변경 예정")
        }
        didSet {
            print("\(oldValue)달러에서 \(dollar)로 변경")
        }
    }
}

var moneyInMyPocket: Money = Money()

moneyInMyPocket.currentRate = 1150

moneyInMyPocket.dollar = 10


````
willSet 변경 직후, oldSet 변경 되기 전

## 상속
- 클래스, 프로토콜에서 가능
- 열거형, 구조체는 상속 불가
- 다중상속 지원안함

````swift 

class Person {
    var name: String = ""
    
    func selfIntroduce() {
        print("저는 \(name)입니다.")
    }
    
    // final 키워드는 재정의를 방지한다.
    final func sayHello() {
        print("hello")
    }
    
    // 재정의 불가 타입 메서드 - static
    static func typeMethod() {
        print("type method - static")
    }
    
    // 재정의 가능 타입 메서드 - class
    class func classMethod() {
        print("type method - class")
    }
    
//    final class func은 static과 같다.
}

// class 이름 : 상속받을 클래스 이름
class Student: Person {
    var major: String = ""
    
    // 새롭게 사용하길 원한다면 override를 한다.
    override func selfIntroduce() {
        print("저는 \(name)이고, 전공은 \(major)입니다")
    }
    
    override class func classMethod() {
        print("overriden type method - class")
    }
}

````

## 인스턴스의 생성과 소멸
### 프로퍼티의 기본값
- 인스턴스는 초기화와 동시에 모든 프로퍼티에 유효한 값이 할당되어 있어야 함.
- 프로퍼티에 미리 기본값을 할당해두면 인스턴스가 생성됨과 동시에 초기값을 지닌다.

### 이니셜라이저
- 프로퍼티 기본값을 지정하기 어려운 경우에는 이니셜라이저를 통해 인스턴스가 가져야 할 초기값을 전달 가능

````swift
class Person {
    var name: String 
    var age: Int
    var nickName: String
    init(name: String, age: Int, nickName: String) {
        self.name = name
        self.age = age
        self.nickname = nickname
    }
}

````

### 디이니셜라이저
- 클래스의 인스턴스가 메모리에서 해제되는 시점에 호출된다.
- 인스턴스가 해제되는 시점에 해야할 일을 구현할 수 있다.

## 옵셔널 체이닝
- 옵셔널 요소 내부의 프로퍼티로 또다시 옵셔널이 연속적으로 연결되는 경우 유용하게 사용 가능

## 타입캐스팅
- 인스턴스의 타입을 확인하거나 클래스의 인스턴스를 부모 혹은 자식 클래스의 타입으로 사용할 수 있는지를 확인하는 용도로 사용한다.

### is - 타입 확인
````swift
result = yagom is Person // true or false 를 반환
````

### 업 캐스팅
- as를 사용하여 부모클래스의 인스턴스로 사용할 수 있도록 컴파일러에게 타입정보를 전환해준다
- any 혹은 anyobject로도 타입정보를 변환할 수 있다

````swift
var mike: Person = UniversityStudent() as Person
var jina: Any = Person()
````

### 다운 캐스팅
- as? 또는 as!를 사용하여 자식 클래스의 인스턴스로 사용할 수 있도록 컴파일러에게 인스턴스의 타입 정보를 전환해준다.

#### 조건부 다운 캐스팅 - as?
````swift
var optionalCasted: Student?
optionalCasted = mike as? UniversityStudent
optionalCasted = jina as? UniversityStudent // nil
````

#### 강제 다운 캐스팅 - as!
- 이 역할이 가능하다는 걸 강제하는 것
````swift
var forcedCasted = Student

optionalCasted = mike as! UniversityStudent
// optionalCasted = jenny as! UniversityStudent // 런타임 오류
````

## assert와 guard
- 애플리케이션이 동작 도중에 생성하는 다양한 결과값을 동적으로 확인하고 안전하게 처리할 수 있도록 확인하고 빠르게 처리할 수 있다.

### Assertion
- assert(_:_:file:line:) 함수를 사용
- 디버깅 중 조건의 검증을 위하여 사용

````swift
var someInt: Int = 0
assert(someInt == 0, "someInt != 0")
````
- someInt가 0이 아니라면 동작을 중지하고 오른쪽 문자열에 넣었던 메시지가 뜨게 된다.

### Early Exit
- guard를 사용하여 잘못된 값의 전달 시 특정 실행구문을 빠르게 종료한다. 디버깅 모드 뿐 아니라 어떤 조건에서도 동작한다.
- guard의 else 블럭 내부에는 특정 코드블럭을 종료하는 지시어(return, break 등)가 있어야한다.
- 타입 캐스팅, 옵셔널과도 자주 사용되며, 단순 조건 판단 후 빠르게 종료할 때도 사용한다.

````swift
var count = 1
while true {
    guard count < 3 else {
        break
    }
    print(count)
    count += 1
}
//1 
//2
````

## 프로토콜
- 프로토콜은 특정 역할을 수행하기 위한 메서드, 프로퍼티, 이니셜라이저 등의 요구사항을 정의한다.
- 구조체, 클래스, 열거형은 프로토콜을 채택해서 프로토콜의 요구사항을 실제로 구현할 수 있다.
- 어떤 프로토콜의 요구사항을 모두 따르는 타입은 그 '프로토콜을 준수한다(Confirm)'고 표현한다.
- 프로토콜의 요구사항을 충족시키려면 프로토콜이 제시하는 기능을 모두 구현해야 한다.

### 정의
````swift
protocol 프로토콜 이름 {
    정의부
}
````
- 프로퍼티 요구는 항상 var 키워드를 사용한다.
- get은 읽기만 가능, set도 함께 명시하면 읽기 쓰기 모두 가능한 프로퍼티다.
- 이외에 메서드나 이니셜라이저도 요구 가능하다.
````swift
protocol Talkable {
    var topic: String { get set }
    var language: String { get }
    
    func talk()
    
    init(topic: String, language: String)
}

````

### 프로토콜 채택 및 준수
person이 Talkable을 채택한 것
````swift
struct Person: Talkable {
//    var topic: String
//    let language: String
    
    var language: String { get { return "한국어 " }}
    
    var subject: String = ""
    var topic: String {
        set {
            self.subject = newValue
        }
        get {
            return self.subject
        }
    }
    
    func talk() {
        
    }
    
    init(topic:String, language: String){
        self.topic = topic
        self.language = language
    }
}

````

### 프로토콜 상속
- 프로토콜은 클래스와 다르게 **다중상속이 가능** 

### 클래스 상속과 프로토콜
- 클래스에서 상속과 프로토콜 채택을 동시에 하려면 상속받으려는 클래스를 먼저 명시하고 그 뒤에 채택할 프로토콜 목록을 작성한다.

### 프로토콜 준수 확인
- 인스턴스가 특정 프로토콜을 준수하는지 확인 가능
- is, as 연산자 사용
````swift
var someAny: Any = sup
someAny is Readable // true
someAny is ReadSpeakable // false
````

## 익스텐션
- 구조체, 클래스, 열거형, 프로토콜 타입에 새로운 기능을 추가할 수 있는 기능이다.
- 기능을 추가하려는 타입의 구현된 소스 코드를 알지 못하거나 볼 수 없다 해도, 타입만 알고 있다면 그 타입의 기능을 확장할 수 있다.

### 추가 기능
- 연산 타입 프로퍼티 / 연산 인스턴스 프로퍼티
- 타입 메서드 / 인스턴스 메서드
- 이니셜라이저
- 서브스크립트
- 중첩 타입
- 특정 프로토콜을 준수할 수 있도록 기능 추가

### 정의

````swift
extension 타입 {
    타입에 추가될 새로운 기능 구현
}

extension 타입: 프로토콜1, 프로토콜2, 프로토콜3 ... {
    요구사항
}
````

### 익스텐션 구현
#### 연산 프로퍼티
````swift
extension Int {
    var isEven: Bool {
        return self % 2 == 0
    }
    
    var isOdd: Bool {
        return self % 2 == 1
    }
}

print(1.isEven) // false
print(2.isOdd) // false
````

#### 이니셜라이저 추가
````swift
extension String {
    init(intTypeNumber: Int) {
        self = "\(intTypeNumber)"
    }

    init(doubleTypeNumber: Double) {
        self = "\(doubleTypeNumber)"
    }
}

````

## 오류처리 
- Error 프로토콜과 주로 열거형을 통해서 오류를 표현한다
````swift
enum 오류종류이름: Error {
    case 종류1
    case 종류2
    
}
````

### 함수에서 발생한 오류 던지기
- 오류 발생의 여지가 있는 메서드는 throws를 사용해 오류를 내포하는 함수임을 알림
````swift
class VendingMachine {
    let itemPrice: Int = 100
    var itemCount: Int = 5
    var deposited: Int = 0

    func receiveMoney(_ money: Int) throws {
        guard money > 0 else {
            throw VendingMachineError.invalidInput
        }

        self.deposited += money
        print("\(money)원 받음")
    }
}
````

### do-catch 문으로도 오류발생 대비
````swift
do {
    구문
} catch ____ {
    print()
}
````

### try?와 try!
#### try?
- 별도의 오류처리 결과를통보받지 않고 오류가 발생했으면 결과값을 nil로 돌려받을 수 있다.
- 정상동작 후에는 옵셔널 타입으로 정상 반환값을 돌려받는다

#### try!
- 오류가 발생하지 않을 것이라는 확신을 가질 때, 정상동작 후 바로 결과값을 돌려받는다.
- 오류가 발생하면 런타임 오류가 발생해 애플리케이션 동작이 중지된다.

