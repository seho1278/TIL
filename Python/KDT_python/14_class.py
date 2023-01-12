# class Person:

#     def greeting(self):
#         return 'hi....'


# iu = Person()

# jimin = Person()

# print(type(iu))  # type : person

# print(iu.greeting()) # 메서드 호출

# iu.name = '아이유'   # 속성을 부여할 수 있음
# jimin.name = 'BTS 지민'
# print(iu.name)


class Person:

    # 생성자 메서드
    def __init__(self, name):  # self는 인스턴스 자기자신
        self.name = name
    
    def greeting(self):
        return f'안녕.. 난 {self.name}'

# 인스턴스 생성
p1 = Person('아이유')
print(p1.greeting())

# Person('아이유')
# 파이썬 내부적으로 함수를 싱행

# Person.__init__(xxxx, '아이유')