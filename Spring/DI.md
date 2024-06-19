# 의존성 주입(Dependency Injection)

<br>

#### 사용할 객체를 직접 생성하지 않고 외부 컨테이너가 생성한 객체를 주입받아 사용하는 [제어 역전](/Spring/IoC.md)의 방법 중 하나

## 의존성 주입 방식
- 스프링에서는 @Autowired라는 어노테이션을 통해 의존성 주입이 가능
- 스프링에서 의존성을 주입하는 방법은 세 가지가 있다. 

1. **생성자**를 통한 의존성 주입 **(권장)**
   - 레퍼런스 객체 없이 객체를 초기화할 수 없게 설계가 가능하다.
```java
@RestController
public class DIController {
    
    MyService myService;
    
    @Autowired
    public DIController(MyService myService) {
        this.myService = myService;
    }
    
    @GetMapping("/di/hello")
    public String getHello() {
        return myService.getHello();
    }
}
```
2. **필드 객체 선언**을 통한 의존성 주입
```java
@RestController
public class DIController {
    
    @Autowired
    private MyService myService;
    
    @GetMapping("/di/hello")
    public String getHello() {
        return myService.getHello();
    }
}
```
3. **setter 메서드**를 통한 의존성 주입
```java
@RestController
public class DIController {
    
    MyService myService;
    
    @Autowired
    public void setMyService(MyService myService) {
        this.myService = myService;
    }
    
    @GetMapping("/di/hello")
    public String getHello() {
        return myService.getHello();
    }
}
```

<br>

<br>

<br>

### 참고자료 : 스프링 부트 핵심 가이드
### [위로](#) / [뒤로](/README.md/#)

