class Person:
    def __init__(self, name):
        self.name = name


class Person_:
    def talk(self):
        print('안녕')

    def eat(self, food):
        print(f'{food}를 냠냠')


person1 = Person('지민')

print(person1.name)

person2 = Person_()
person2.talk()

person2.eat('피자')

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b, a is b)

# ==, 변수가 참조하는 객체가 동등한 경우 True but 둘 다 동일한 대상을 가리키고 있다고 확인해 준 것은 아니다.

# is 두 변수가 동일한 객체를 가리키는 경우 True


class Person__:
    def __init__(self, name):
        self.name = name

john = Person__('john')

print(john.name)

john.name = 'John Kim'
print(john.name)

# 인스턴스 메소드
# 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메소드
# 클래스 내부에 정의되는 메소드의 기본
# 호출 시, 첫번째 인자로 인스턴스 자기자신(self)이 전달됨


# self
# 인스턴스 자기자신
# 파이썬에서 인스턴스 메소드는 호출 시 첫번째 인자로 인스턴스 자신이 전달되게 설계
# 매게변수 이름으로 self를 첫번째 인자로 정의
# 다른 단어로 써도 작동하지만, 파이썬의 암묵적인 규칙


# 생성자(constructor) 메소드
# 인스턴스 객체가 생성될 때 자동으로 호출되는 메소드
# 인스턴스 변수들의 초기값을 설정
# 인스턴스 생성
# __init__ 메소드 자동 호출

class Person___:
    def __init__(self):
        print('인스턴스가 사라졌습니다.')

person4 = Person___()
del person4


# 매직 메소드
# Double underscore(__)가 있는 메소드는 특수한 동작을 위해 만들어진 메소드로, 스페셜 메소드 혹인 매직 메소드라고 불림


N = int(input())

for i in range(N):
    S = input()
    print(S[0], S[-1], sep='')

