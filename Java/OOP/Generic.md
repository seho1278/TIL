# 제네릭(Generic)

## 1. 정의
- 클래스나 메소드에서 사용할 내부 데이터 타입을 컴파일 시에 미리 지정하는 방법
  - 형 변환에 대한 번거로움을 줄여주고, 컴파일 타임에 체크함으로써 안정성을 높임

| 용어                | 예시           |
|-------------------|--------------
| row type          | List         |
| Parameterized type | List<String> |
| Type Variable     | T, E, K, V   |
| Wild card         | ?            |

- 예시

```java
public class HashMap<K, V> extends AbstractMap<K, V>
    implements Map<K, V>, Cloneable, Serializable {

    public V put(K key, V value) {
        return putVal(hash(key), key, value, false, true);
    }

    public V get(Object key) {
        Node<K, V> e;
        return (e = getNode(hash(key), key)) == null ? null : e.value;
    }
} 

public class DeclarationGenericExample {
    public static void main(String[] args) {
        HashMap<String, Integer> hashMap = new HashMap(0);
        // Key - String, Value - Integer 형태를 지켜야 한다.
        hashMap.put("a", 1);
        hashMap.put("java", 456);
        System.out.println(hashMap.get("a"));
    }
}
```

<br>

## 2. 제네릭 메서드
- 매개 변수와 반환 값에 타입 변수를 갖는 메서드
  - 제네릭 클래스의 <T>와 제네릭 메서드의 <T>는 별개
  - static 변수에 제네릭 타입은 안되지만 메서드에는 가능
  - 제네릭 메서드는 호출할 때 마다 타입 매개변수에 타입을 대입(대부분 추론 가능)

<br>

## 3. 제네릭 타입과 다형성
- 참조 변수와 생성자로 대입된 타입은 일치해야함
- 부모 타입으로 지정된 자료구조나 참조 변수에는 자식 클래스가 들어갈 수 있음
- JDK 1.7 부터는 타입(생성자 타입) 추론 가능
- 대입된 타입이 다른 제네릭 타입 간의 형 변환은 불가능(와일드 카드는 가능)

<br>

## 4. 제네릭 타입의 제한
- 제네릭 타입에 'extends' 키워드 사용시 같은 부모 클래스와 부모 클래스를상속받는 자식 클래스들만 사용 가능
  - ex) <T extends Animal> 와 같이 설정할 경우 Animal 클래스와 Animal을 상속받는 자식 클래스만 T에 들어갈 수 있음
  - 특정 인터페이스를 구현한 클래스로 제약이 필요한 경우 implements가 아닌 extends

<br>

## 5. 와일드 카드
- 메소드의 매개변수로 제네릭 클래스의 객체를 받을 때, 타입을 제한하기 위해 사용
  - <? extends T> 상한 제한 : T와 자손
  - <? super T> 하한 제한 : T와 부모
  - <?> : 제한 없음
  - 와일드카드는 "&" 사용 불가 (여러개의 클래스 나열 불가능)
