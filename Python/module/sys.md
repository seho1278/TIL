# sys

### 1. Python의 기본 입출력 함수 input()을 사용하지 않는 경우
* 입력 받은 문자열을 문자 단위로 읽는다.
* 게행 문자를 삭제한다.
* 문자를 문자열로 변환하여 반환한다.

#### 이처럼  input()함수는 입력받은 문자열을 문자 단위로 하나씩 읽어들이기 때문에 느리다. 그렇기 때문에 코딩 테스트에서 수십만 건의 입력을 받아야 하는 상황이 온다면 Timeout이 자주 발생한다.

#### 따라서 Python으로 입력이 많은 문제를 풀어야 할 때는, 사용자의 입력을 받는 버퍼를 만든 뒤, 그 버퍼에서 입력을 다시 읽어들이는 sys.stdin.readline() 함수를 이용한다.

<br>

### Python code
```python
import sys

input = sys.stdin.readline

input()   # input()함수 처럼 보이지만 실제로는 sys.stdin.readline() 함수가 실행

# 이런방식은 게행 문자를 포함하여 문자열 자료형으로 변수에 포함되어 저장되기 때문에
# rstrip() 함수와 같이 작성하여 게행 문자를 바로 제거하는 방식을 사용한다.
```


<br>

<br>

<br>

### [위로](#) / [뒤로](/Python/module/README.md/#)