# 포맷팅

#### 코드의 가독성을 위해서는 포맷팅이 필수다.

## 1. 포맷팅이 중요한 이유
- 기존 for문
```java
public void horriblyFormattedMethod() {
    System.out.println("First line");
        System.out.println("Second line");
      System.out.println("Third line");
    for (int i = 0; i < 3; i++)
    System.out.println("number " + i);
}
```
- 포맷팅
```java
public void horriblyFormattedMethod() {
    System.out.println("First line");
    System.out.println("Second line");
    System.out.println("Third line");
    for (int i = 0; i < 3; i++) {
        System.out.println("number " + i);
    }
}
```

- 포맷팅을 하게 되면 코드를 수월하게 읽어나갈 수 있고 코드를 잘못 해석해 버그를 발생할 위험을 줄일 수 있다.

<br>

## 2. 클린코드 포맷팅
- 적절한 길이 유지
  - ~ 200 line : 코드 길이를 200줄 정도로 제한
    - 반드시 지킬 규칙은 아니지만 일반적으로 큰 파일보다는 작은 파일이 이해하기 쉽다
    - 코드 길이가 200라인을 넘어간다면 클래스가 여러개의 일을 하고 있을 수 있음 -> SRP 위배
  - < 500 line
- 밀접한 개념은 가까이
  - 행 묶음은 완결된 생각 하나를 표현 -> 개념은 빈 행으로 분리
  - 변수는 사용되는 위치에서 최대한 가까이 선언

<br>

## 3. Java Class Declarations
- 자바 클래스 선언 포맷팅 룰 (오라클 자바 문서 참고)
- Class 내부 코드 순서.
  - static 변수
    - public -> protected -> package -> private 순서
  - instance 변수
    - public -> protected -> package -> private
  - 생성자
  - 메서드
    - public 메서드에서 호출되는 private 메서드는 그 아래에 위치 (가독성 위주로 그룹핑)
- 예시
```java
package java.blah;

import java.blah.blahdy.BlahBlah;

public class Blah extends SomeClass {
    public static int classVar1;
    
    private static Object classVar2;
    
    public Object instanceVar1;
    
    protected int instanceVar2;
    
    private Object[] instanceVar3;
    
    public Blah() {
        // 생성자
    }
    
    public void doSomething() {
        // ...
    }
    
    public void doSomethingElse(Object someParam) {
        // ...
    }
}
```

<br>

## 4. Team Coding Convention
- 팀의 코딩 스타일에 관한 약속 
- 개발 언어의 컨벤션이 우선이지만, 애매한 부분에 있어서는 팀 컨벤션을 따름 (없는경우 함께 만들기)
- 예시
  - MySQL Convention : 컬럼명은 snake_cake로 네이밍
  - Team Convention : enum 타입으로 사용하는 varchar 타입의 경우 컬럼명은 _type로 끝나도록 네이밍
- 참고할 만한 컨벤션
  - Google Java Style Guide
  - Naver Hackday Java Convention (한글문서)

<br>

<br>

<br>

### 참고자료 : 클린코드
### [위로](#) / [뒤로](/README.md)