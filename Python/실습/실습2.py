# 문제1
# n = int(input("정수를 입력하세요 > "))

# if n > 0:
#     print(True)
# else:
#     print(False)


# 문제2
# n1 = int(input("첫 번째 정수를 입력하세요 > "))
# n2 = int(input("두 번째 정수를 입력하세요 > "))

# if n1 > n2:
#     print(n1)
# elif n1 < n2:
#     print(n2)
# else:
#     print(False)


# 문제3
# n = int(input("정수를 입력하세요 > "))

# if 1 < n and n < 10:
#     print(True)
# else:
#     print(False)


# 문제4
# n = int(input("정수를 입력하세요 > "))

# if n > 0:
#     if n%2 == 0:
#         print(True)
#     else:
#         print(False)
# else:
#     print(False)


# 문제5
# n = int(input("정수를 입력하세요 > "))
# if n >= 60:
#     if n > 100:
#         print("에러")
#     else:
#         print("합격")
# else:
#     if n < 0:
#         print("에러")
#     else:
#         print("불합격")


# 문제6
# s = input("문자열을 입력하세요 > ")

# for i in s[::-1]:
#     print(i)


# 문제7
# n1 = int(input("첫 번째 정수를 입력하세요 > "))
# n2 = int(input("두 번째 정수를 입력하세요 > "))

# if n1 > n2:
#     for i in range(n2 + 1, n1):
#         print(i)
# elif n2 > n1:
#     for i in range(n1 + 1, n2):
#         print(i)
# else:
#     print(False)


# 문제8
# n1 = int(input("첫 번째 정수를 입력하세요 > "))
# n2 = int(input("두 번째 정수를 입력하세요 > "))

# if n1 > n2:
#     for i in range(n2 + 1, n1)[::-1]:
#         print(i, end=" ")
# elif n2 > n1:
#     for i in range(n1 + 1, n2)[::-1]:
#         print(i, end=" ")
# else:
#     print(False)


# 문제9
# n = int(input("정수를 입력하세요 > "))
# if n > 0:
#     for i in range(1, n, 2):
#         print(i)
# else:
#     print(False)


# 문제10
# n1 = 10
# n2 = 10

# for n in range(2, n1):
#     for m in range(2, n2):
#         print(f"{n} X {m} = {n*m}")