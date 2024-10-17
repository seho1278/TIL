# 스프링 프레임워크 vs 스프링 부트

<br>

## 등장배경

#### 기존 스프링 프레임워크에서 하이버네이트(Hibernate)를 사용하기 위해 작성하는 설정 파일 일부
```html
<bean id="dataSource" class="com.mchange.v2.c3p0.ComboPooledDataSource" destroy-method="close">
    <property name="driverClass" value="${db.driver}" />
    <property name="jdbcUrl" value="${db.url}" />
    <property name="user" value="${db.username}" />
    <property name="password" value="${db.password}" />
</bean>

...
```
- 기존 스프링 프레임워크는 필요한 모듈을 추가하다 보면 설정이 복잡해지는 문제가 발생 -> 이를 해결하기 위해 스프링 부트가 등장
- 스프링 부트를 사용하면 복잡한 설정 없이 개발이 가능

## 스프링부트 특징
### 1. 의존성 관리
- 스프링 프레임워크
  - 개발에 필요한 각 모듈의 의존성을 직접 설정하고 호환되는 버전을 명시해야만 정상 동작이 가능
  - 애플리케이션에서 사용하는 스프링 프레임워크나 라이브러리의 버전을 올리는 상황에서는 연관된 다른 라이브러리의 버전까지 고려해야함 

- 스프링 부트
  - 'spring-boot-starter'라는 여러가지 의존성을 제공하여 각 라이브러리의 기능과 관련해서 자주 사용되고 서로 호환되는 버전의 모듈 조합을 제공
  - 주로 사용되는 spring-boot-starter 라이브러리
    - spring-boot-starter-web : 스프링 MVC를 사용하는 RESTful 애플리케이션을 만들기 위한 의존성 기본적으로 내장 톰캣이 포함돼 있어 jar 형식으로 실행 가능
    - spring-boot-starter-test : JUnit, Jupiter, Mockito 등 테스트용 라이브러리 기능 제공
    - spring-boot-starter-jdbc : HikariCP 커넥션 풀을 활용한 JDBC 기능 제공
    - spring-boot-starter-security : 스프링 시큐리티(인증, 권한, 인가 등) 기능을 제공
    - spring-boot-starter-data-jpa : 하이버네이트를 활용한 JPA 기능을 제공
    - spring-boot-starter-cache : 캐시 기능을 제공

### 2. 자동 설정
- 스프링 기능을 사용하기 위한 자동설정(Auto Configuration)을 지원
  - 자동 설정 : 애플리케이션에 추가된 라이브러리를 실행하는데 필요한 환경을 찾아줌

- 스프링 부트를 사용시 애플리케이션을 개발하는데 필요한 의존성을 추가하면 프레임워크가 이를 자동으로 관리해줌

<br>

#### 스프링 부트 메인 애플리케이션 코드 분석
```java
@SpringBootApplication
public class SpringBootApplication {
    public static void main(String[] args) {
        SpringApplication.run(SpringBootApplication.class, args);
    }
}
```
- @SpringBootApplication은 여러 어노테이션을 합쳐 놓은 인터페이스
  - 구성
```java
@Target({ElementType.Type})
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Inherited
@SpringBootConfiguration
@EnableAutoConfiguration
@ComponentScan(
    excludeFilters = {@Filter(
        type = FilterType.CUSTOM,
        classes = {TypeExcludeFilter.class}
    ), @Filter(
        type = FilterType.CUSTOM,
        classes = {AutoConfigurationExcludeFilter.class}
    )}
)
public @interface SpringBootApplication {
    ...
}
```
- @ComponentScan 어노테이션이 @Component 시리즈 어노테이션이 붙은 클래스를 발견해 빈(bean)을 등록 이후 @EnableAutoConfiguration 어노테이션을 통해 'spring-boot-autoconfigure' 패키지 안에 spring.factories 파일을 추가해 다양한 자동설정이 일부 조건을 거쳐 적용됨.
- org.springframework.boot.autoconfigure.EnableAutoConfiguration 하단에 많은 자동 설정 정의
  -  각 파일에 설정된 @Conditional의 조건을 충족할 경우 빈에 등록되고 애플리케이션에 자동 반영

<br>

### 3. 내장 WAS
- spring-boot-starter-web의 경우 톰캣 내장
- 스프링 부트의 자동 설정 기능은 톰캣에도 적용 -> 특별한 설정 없이도 톰캣 실행 가능
  - 필요에 따라 다른 웹 서버로 대체 가능

<br>

### 4. 모니터링
- 개발 이후 서비스 운영 단계에서 해당 시스템이 사용하는 스레드, 메모리, 세션 등 주요 요소들을 모니터링 해야한다.
- 스프링 부트에서는 액추에이터(Spring Boot Actuator)라는 자체 모니터링 도구 존재

<br>

<br>

<br>

### 참고자료 : 스프링 부트 핵심 가이드
### [위로](#) / [뒤로](/README.md/#)