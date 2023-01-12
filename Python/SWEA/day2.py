# 2047 신문 헤드라인
# The_headline_is_the_text_indicating_the_nature_of_the_article_below_it. 입력
# THE_HEADLINE_IS_THE_TEXT_INDICATING_THE_NATURE_OF_THE_ARTICLE_BELOW_IT. 출력

# import sys
# sys.stdin = open('input.txt', 'r')

# string = input()
# print(string.upper())


# 2025 N줄덧셈
# 10 입력
# 합한 값 출력

# T = int(input())
# result = 0 
# for t in range(1, T+1):
#     result += t

# print(result)


# 1936 1:1 가위바위보
# 입력값 A, B 입력
# 가위는 1 바위는 2 보는 3로 표현
# 누가 이겼는지 판별

# A, B = map(int, input().split())

# if A > B:
#     print('A')
# elif B > A:
#     print('B')


# # 2027 대각선 출력하기
# import sys
# sys.stdin = open('input.txt', 'r')

# for t in range(1, 6):
#     string = input().split()
#     print(*string)

# print('#++++')
# print('+#+++')
# print('++#++')
# print('+++#+')
# print('++++#')


# 2058 자릿수 더하기

# T = int(input())

# n1 = divmod(T, 1000)
# n2 = divmod(n1[1], 100)
# n3 = divmod(n2[1], 10)
# print(n1[0] + n2[0] + n3[0] + n3[1])


# 2019 더블더블

# T = int(input())
# result = 1
# r_list = [1]
# for t in range(1, T+1):
#     result *= 2
#     r_list.append(result)

# print(*r_list)

# T = int(input())
# result = 0
# r_list = [1]
# for t in range(1, T+1):
#     result += 1
#     r_list.append(2**result)
    
# print(*r_list)