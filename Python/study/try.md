# try, except문      (점프 투 파이썬 참고)

## **try, except문**
* 기본구조
```python
try:
    ...
except [발생오류 [as 오류변수]]:  # try에서 오류가 발생하면 except블록이 수행된다.
    ...                          # [] 부분 생략해도 오류가 발생 한다면 except수행
```

<br>

* 발생오류만 포함한 경우
```python
try:
    ...
except 발생오류:  # 정해 놓은 발생오류와 동일한 오류일 경우에만 except 수행
    ...
```

<br>

* 오류변수까지 포함한 경우
```python
try:
    ...
except 발생오류 as 오류변수:  # 오류의 내용까지 알고 싶을 때 사용
    ...
```
ex)
```python
try:
    4 / 0
except ZeroDivisionError as e:
    print(e)   # division by zero가 출력된다.
```

<br>

## **try .. finally**
* finally절은 try문 수행 도중 예외 발생 여부에 상관 없이 항상 수행되며 보통 사용한 리소스를 close해야 할때 많이 사용한다.

ex)
```python
try:
    f = open('foo.txt', 'w')

    (... 생략 ...)

finally:
    f.close()  # 예외 발생 여부 관계없이 파일을 닫을 수 있다.
```

<br>

## **여러개의 오류 처리하기**
ex)
```python
try:
    a = [1,2]            
    print(a[3])        # < IndexError가 먼저 발생
    4/0                # < ZeroDivisionError는 발생하지 않는다
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")  # 4/0에 대한 오류
except IndexError:
    print("인덱싱 할 수 없습니다.")   # a[3]에 대한 오류
```

ex) 오류 둘다 처리한 경우
```python
try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:  # 괄호를 사용하여 함께 묶어 처리한다.
    print(e)
```

* pass를 통해 오류를 회피할 수도 있다.
ex)
```python
try:
    f = open("나없는파일", 'r')
except FileNotFoundError:            # FileNotFoundError 발생할 경우 pass 
    pass
```

<br>

## **else**
ex)
```python
try:
    age=int(input('나이를 입력하세요: '))
except:                                       # 오류 있을 때 수행
    print('입력이 정확하지 않습니다.')
else:                                         # 오류 없을 경우에만 수행
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print('환영합니다.')
```

## **오류 발생시키기**
* raise를 통해 강제로 발생시킬수도 있다.

ex) Bird 클래스를 상속받는 자식 클래스에게 반드시 fly라는 함수를 구현하도록 만들고 싶은 경우
```python
class Bird:
    def fly(self):
        raise NotImplementedError   # 파이썬에 정의되어 있는 오류
                                    # 작성해야 하는 부분이 구현되지 않았을 경우 
                                    # 일부러 오류를 일으키기 위해 사용
class Eagle(Bird):
    pass

eagle = Eagle()
eagle.fly()               # Bird 클래스의 fly 메서드 수행 > NotImplementedError
```
* 실행 결과
```python
Traceback (most recent call last):
  File "...", line 33, in <module>
    eagle.fly()
  File "...", line 26, in fly
    raise NotImplementedError
NotImplementedError
```
* NotImplementedError 해결
```python
class Eagle(Bird):
    def fly(self):             # fly 함수 설정
        print("very fast")

eagle = Eagle()
eagle.fly()                    # very fast가 실행된다.
```

<br>

## **예외 만들기**
* 프로그램 수행 도중 특수한 경우에만 예외처리를 하기 위해 만들어서 사용
ex)
```python
class MyError(Exception):  # 파이썬 내장 클래스인 Exception 사용
    pass                   # 예외 생성

def say_nick(nick):        # 함수 작성
    if nick == '바보':
        raise MyError()
    print(nick)

say_nick("천사")           # 함수 호출
say_nick("바보")
```
* 실행 결과
```python
천사
Traceback (most recent call last):
  File "...", line 11, in <module>
    say_nick("바보")
  File "...", line 7, in say_nick
    raise MyError()
__main__.MyError
```

<br>

* 예외 처리 기법 활용
```python
try:
    say_nick("천사")
    say_nick("바보")
except MyError:      # 오류발생시 수행하도록 설정
    print("허용되지 않는 별명입니다.")
```
* 실행 결과
```python
천사
허용되지 않는 별명입니다.
```
* 오류메시지를 사용 하고 싶으면 `as` 기능을 사용하면 된다.

<br>

<br>

<br>

### [위로](#try-except문) / [뒤로](/Python/README.md)