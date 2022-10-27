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