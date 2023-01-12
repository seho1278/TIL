# 문제1
# string = input() # hello, hEllo hypergrowth, java 입력
# result = 0

# if 'e' in string:
#     for i in string:
#         if i != 'e':
#             result += 1
#         elif i == 'e':
#             print(result)
# else:
#     print(-1)


# 문제2
# string = input().split() # hello, hello hypergrowth, apple apple banana grape 입력
# str_dict = {}

# for i in string:
#     if i not in str_dict:
#         str_dict[i] = 1
#     else:
#         str_dict[i] += 1

# for keys, values in str_dict.items():
#     print(keys, values)


# 문제3 
# s1 = input() # apple, hello, hEllo 입력
# s2 = []
# for i in s1:
#     if i != 'e':
#         s2.append(i)
# print(*s2, sep="")


# 문제4
# str_list = input().split() # apple p, hello o, hEllo a 입력
# result = 0

# for i in str_list[0]:
#     if i == str_list[1]:
#         result += 1

# print(result)


# 문제5
# str_list = input().split() # 010 1234 5678 입력
# print(*str_list, sep='-')


# 문제6
# num = int(input()) # 244, 1, -10 입력

# if num >= 100:
#     r1 = divmod(num, 100)
#     r2 = divmod(r1[1], 10)
#     r3 = divmod(r2[1], 1)
#     print(r1[0] + r2[0] + r3[0])

# elif num < 100 and num >= 10:
#     r2 = divmod(num, 10)
#     r3 = divmod(r2[1], 1)
#     print(r2[0] + r3[0])

# elif num < 10 and num >= 0:
#     r3 = divmod(num, 1)
#     print(r3[0])

# else:
#     print(-1)

# 6 - 1 (다른사람 풀이)

# while 사용
# 반복적으로 n을 10으로 나눈 몫,
# n이 0보다 클 때 계속 반복!
# 결과값은 n을 10으로 나눈 나머지를 더해나갈 것

# n = int(input())
# result = 0

# while n > 0:
#     result += n%10
#     n //= 10
    
#     print(n, result)

# print(result)