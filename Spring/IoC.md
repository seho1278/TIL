# 제어역전(Inversion of Control)

<br>

#### 객체의 관리를 컨테이너에 맡겨 제어권이 넘어간 것

## 일반적인 개발의 경우
- 사용하려는 객체를 선언하고 해당 객체의 의존성을 생성한 후 객체에서 제공하는 기능을 사용 (객체를 생성하고 사용하는 일련의 작업을 개발자가 직접 제어)

```java
@RestController
public class NoDIController {
    
    // 서비스 객체 직접 생성
    private MyService service = new MyServiceImpl();
    
    @GetMapping("/no-di/hello")
    public String getHello() {
        return service.getHello();
    }
}
```
<일반적인 자바 코드에서 객체 사용법>

<br>

## 제어 역전의 경우
- IoC를 적용한 환경에서는 사용할 객체를 직접 생성하지 않고 객체의 생명주기 관리를 외부(스프링 컨테이너)에 위임
- 제어 역전을 통해 [의존성주입(DI)](/Spring/DI.md), [관점지향 프로그래밍(AOP)](/Spring/AOP.md)등이 가능

<br>

<br>

<br>

### 참고자료 : 스프링 부트 핵심 가이드
### [위로](#) / [뒤로](/README.md/#)
