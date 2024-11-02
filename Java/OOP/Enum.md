# 열거형 (Enum)

## 1. 정의
- 관련된 상수들을 모아서 나열해 둔 타입
  - 자바의 열거형은 값과 타입을 모두 체크 -> 하나라도 다르면 컴파일 에러 발생
  - 타입에 안전(Type safe)한 열거형 제공
  - 열거형에는 기본적으로 0부터 시작되는 정수 값이 ordinal로 부여됨
  - 정수 값 외에 필드도 추가할 수 있음

<br>

## 2. 열거형 비교
- '=='과 compareTo 메서드 사용
  - compareTo 메서드는 ordinal 차이를 반환

<br>

## 3. Enum 클래스
- 모든 Enum의 부모 클래스인 추상 클래스
- 
| Method                                    | Description                    |
|-------------------------------------------|--------------------------------|
| Class<E> getDeclaringClass()              | 열거형 상수의 Class 객체를 반환           |
| String name()                             | 열거형 상수의 이름을 반환                 |
| int ordinal()                             | 열거형 상수의 순서를 반환                 |
| T valueOf(Class<T> enumType, String name) | 지정된 열거형의 name과 일치하는 열거형 상수를 반환 |
| static E values()                         | 열거형 상수들을 배열로 반환                |
| static E valueOf(String name)             | 이름과 일치하는 열거형 상수를 반환            |
