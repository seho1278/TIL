# def add(a, b):   # 정의
#     return a + b

# print(add)
# print(add(-10, -20))   # 호출
# print(add(10, 20))


# 하나의 숫자 n을 입력 받아서 세제곱을 반환하는
# 함수 cube를 작성

# 함수 호출
# 2의 세제곱
# 100의 세제곱

# n = int(input())

# def cube(a):
#     return a ** 3

# print(cube(n))


# def foo():
#     return 1, 2, 3

# print(type(foo()))

# def boo():
#     a = 1 + 2

# print(type(boo()))
# return
# 명시적인 return문 없는 경우 : None
# 여러값을 return 하는 경우 : tuple


# def add(*numbers):
#     # print(type(numbers)) # tuple
#     result = 0
#     for n in numbers:
#         result += n
#     return result

# print(add(1, 2, 3))


# def movie(**kwargs):
#     # print(type(kwargs)) # dict
#     return kwargs

# print(movie(name='더 글로리', writer='김은숙'))


# print(sum)

# # global scope
# a = 10

# # local scope
# def foo():
#     b = 10 # 1 return None = 종료 >> b는 존재하지 않게 됨

# foo()
# print(foo())


# sum : Built-in scope
# print(sum([1, 2, 3]))
# print(type(sum))

# # sum : Global scope
# sum = 1 + 2

# print(type(sum), sum) 
# print(sum([1, 2, 3])) # TypeError: 'int' object is not callable (호출할수 없다)

a = 5

def foo():
    print(a)  # Local scope에 a가 없으면 global을 찾아서 입력한다.

foo()


def boo():
    global a # global 에 있는 a를 가져옴
    a = 3   # Local scope 에 있는 3을 먼저 찾아쓰기 때문에 5가 아닌 3이 입력됨
    print(a)
    return sum(1, 2, 3) # builtin에 있는걸 로컬에 가져다 쓰는것 # 안에 없으면 밖에서 탐색함
    # 발생할 수 있는 문제 : 함수 안에서 처리해야하는데 밖에서 변수값이 바뀌면 함수에 문제가 발생할 수 있는 경우가 생길 수 있음

