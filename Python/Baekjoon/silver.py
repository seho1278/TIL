# 4673번 셀프 넘버
# 양의 정수 n에 대해서 d(n)을 n과 n의 각 자리수를 더하는 함수라고 정의할 경우
# ex) d(75) = 75 + 7 + 5 = 87
# 양의정수 n이 주어졌을때, 이 수를 시작해서 n, d(n), d(d(n))... 과 같은 무한 수열을 만들 수 있다.
# ex) n = 33 : 33 + 3 + 3 > 39 + 3 + 9 > 51 + 5 + 1  ...
# n을 d(n)의 생성자라고 한다. ex) 33은 39의 생성자
# 생성자가 한개보다 많은 경우도 있다. ex) 91 + 9 + 1 = 101
# 이 때 생성자가 없는 숫자를 셀프 넘버라고 한다. 100보다 작은 셀프넘버는 총 13개가 있다. 1 3 5 7 9 20 31 42 ... 97
# 10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오

# 입력 x

# 출력 : 10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 증가하는 순서로 출력한다.

# def d(x):
#     x_l = [int(a) for a in str(x)]
#     return x + sum(x_l)

# r_list = []
# for n in range(1, 10001):
#     r_list.append(d(n))

# for m in range(1, 10001):
#     if m not in r_list:
#         print(m)


# 1065번 한수
# 한수 : 어떤 양의 정수 X의 각 자리가 등차수열을 이루는 경우
# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램 작성

# 입력 : 첫째 줄에 1000보다 작거나 같은 자연수 N 입력

# 출력 : 첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수 출력

# def d(x):
#     x_l = [int(a) for a in str(x)]
#     return x_l

# N = int(input())
# result = 0
# for n in range(1, N+1):
#     if n < 10:
#         result += 1
#     elif 10 <= n and n < 100:
#         result += 1
#     elif 100 <= n and n < 1000:
#         if d(n)[2] - d(n)[1] == d(n)[1] - d(n)[0]:
#             result += 1

# print(result)

# 1065 -1 (함수없이)
# N = int(input())
# result = 0
# for n in range(1, N+1):
#     if n < 10:
#         result += 1
#     elif 10 <= n and n < 100:
#         result += 1
#     elif 100 <= n and n < 1000:
#         n_list = [int(a) for a in str(n)]
#         if n_list[2] - n_list[1] == n_list[1] - n_list[0]:
#             result += 1

# print(result)


# 1316번 그룹 단어 체커
# 그룸 단어란 각 문자가 연속해서 나타나는 경우만을 말한다.

# 입력: 첫줄에 단어의 개수N

# 출력: 그룹단어 갯수 출력

# N = int(input())

# result = 0
# for n in range(N):
#     S = input()
#     cnt = 0
#     check = []

#     for i in range(cnt, len(S)):
#         if i != len(S) - 1:
#             if S[i] != S[i+1]:
#                 if S[i] not in check:
#                     check.append(S[i])
#                     cnt += i + 1
#                 else:
#                     break
#         else:
#             if S[i] in check:
#                 break

#             else:
#                 result +=1

# print(result)


# N = int(input())
# result = 0

# for n in range(N):
#     S = input()
#     cnt = 0
#     index = S[0]        
#     s_list = []

#     if len(S) == 1:
#         cnt = 1
#     else:
#         for i in S:     
#             if i != index:
#                 s_list.append(index)
#                 index = i
#         s_list.append(index)

#         for m in s_list:
#             if s_list.count(m) >= 2:
#                 cnt = 0
#                 break
#             else:
#                 cnt = 1
                
#         result += cnt

# print(result)


# 10773번 제로
# import sys
# K = int(sys.stdin.readline())
# num_list = []

# for k in range(K):
#     number = int(input())
#     if number == 0:
#         num_list.pop()
        
#     else:
#         num_list.append(number)

# print(sum(num_list))


# 2161번 카드1
# N = int(input())

# num_list = list(range(1, N+1))

# result = []
# while len(num_list) > 1:
#     # 우선, 제일 위에 있는 카드를 바닥에 버린다.
#     # 큐에서 제일 위 : pop(0)
#     result.append(num_list.pop(0))
#     # 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.    
#     num_list.append(num_list.pop(0))

# print(*result, *num_list)


# 1927번 최소 힙

# 1. 배열에 자연수 x를 넣는다.
# 2. 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
# 프로그램은 처음에 비어있는 배열에서 시작

# 입력: 첫 줄에 연산의 개수N이 주어진다. 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다.
# 만약 x가 자연수라면 배열에 x라는 값을 넣는 연산이고, x가 0이라면 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우

# 출력 : 입력에서 0이 주어진 횟수만큼 답을 출력

# import heapq
# import sys

# N = int(sys.stdin.readline())

# array = []
# for n in range(N):
#     x = int(sys.stdin.readline())
#     if x == 0:
#         if len(array) == 0:
#             print(0)
        
#         else:
#             print(-heapq.heappop(array))
    
#     else:
#         heapq.heappush(array, -x)


# 10828번 스택

# 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로글매 작성

# import sys

# N = int(sys.stdin.readline())

# stack = []
# for n in range(N):
#     X = sys.stdin.readline()
#     if 'push' in X:
#         stack.append(int(X.lstrip('push ')))
    
#     elif 'pop' in X:
#         if len(stack) != 0:
#             print(stack.pop())
#         else:
#             print(-1)

#     elif 'size' in X:
#         print(len(stack))

#     elif 'top' in X:
#         if len(stack) != 0:
#             print(stack[-1])
#         else:
#             print(-1)

#     elif 'empty' in X:
#         if len(stack) == 0:
#             print(1)
#         else:
#             print(0)


# 4949번 균형잡힌 세상
# 문자열에 포함되는 괄호는 소괄호와 대괄호 2종류
# 소괄호는 소괄호와만 짝을 이뤄야 하고 대괄호는 대괄호 끼리
# 모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재
# 1:1 매칭만 가능
# 짝을 이루는 두 괄호가 있을 때 그 사이에 있는 문자열도 균형이 잡혀야 한다.

# 입력 : 하나 또는 여러 줄에 걸쳐서 문자열이 주어진다. 각 문자열은 영문 알파벳, 공백, 소괄호, 대괄호 등으로 이루어져 있으며 마침표.로 끝난다.

# 출력 : 각 줄마다 해당 문자열이 균형을 이루고 있으면 yes, 아니면 no
# while True:
#     S = input()
#     array = []
#     if S == '.':
#       break

    
#     for s in S:
#         if s == '(' or s == '[':
#             array.append(s)
#         elif s == ')':
#             if len(array) != 0 and '(' == array[-1]:
#                 array.pop()
#             else:
#                 print('no')
#                 break

#         elif s == ']':
#             if len(array) != 0 and '[' == array[-1]:
#                 array.pop()
#             else:
#                 print('no')
#                 break
#     else:
#         if len(array) == 0:
#             print('yes')
#         else:
#             print('no')


# 1874 스택 수열 (다른사람 코드)

# 1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써 하나의 수열을 만들 수 있다. 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지
# 계산하는 프로그램 작성

# 입력 : 첫 줄에 n이 주어진다. 둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩(중복x)

# 출력 : 입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력 push는 + pop은 -로 표현 불가능한 경우 No

# N = int(input())
# stack, result, find = [], [], True

# cnt = 1
# for _ in range(N):
#     num = int(input())

#     while cnt <= num:
#         stack.append(cnt)
#         result.append('+')
#         cnt += 1
    
#     if stack[-1] == num:
#         stack.pop()
#         result.append('-')

#     else:
#         find = False

# if not find:
#     print('NO')
# else:
#     for i in result:
#         print(i)


# # 2738번 행렬 덧셈(내일 이차원 배열 배우고 다시)
# N, M = map(int, input().split())
# A_list=[]
# B_list=[]
# result = []
# result2 = []
# for n in range(N):
#     i = list(map(int, input().split()))
#     A_list.append(i)

# for m in range(M):
#     j = list(map(int, input().split()))
#     B_list.append(j)

# for k in range(N):
#     for l in range(M):
#         result.append(A_list[k][l] + B_list[k][l])
#     result2.append(result)

# print(result2)