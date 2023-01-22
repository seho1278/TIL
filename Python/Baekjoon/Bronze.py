# 2439번 별 찍기 - 2
# N = int(input())

# for n in range(1, N + 1):
#     print(('*' * n).rjust(N))


# 10952번 A+B -5
# import sys          # input 대신 sys 모듈을 불러와 사용

# while True:         # 무한반복 설정
#     A, B = map(int, sys.stdin.readline().split())
#     if A == 0 and B == 0:
#         break       # 0, 0 조건을 만족하면 종료#23110T-update
      
#     else:           # 0, 0이 아닌경우 A + B 출력
#         print(A + B)


#10951번 A+B - 4
# while True:         # 무한반복 설정
#     try:
#         A, B = map(int, input().split())  # sys를 사용하면 EOFError를 raise하지 않기 때문에 input() 사용!
#         print(A+B)
#     except EOFError:    # 에러가 발생하면 종료되도록 설정
#         break


# 1110 더하기 사이클
# 0보다 크거나 같고, 99보다 작거나 같은 정수 N
# 먼저 주어진 수 < 10 : 앞에 0을 붙여 두자리 수로 만들고 각자리의 숫자를 더한다.
# 그다음 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어붙이면 새로운 수를 만들 수 있다.
# ex) 26부터 시작 2 + 6 = 8, 새로운 수는 68 6 + 8 = 14 새로운 수는 84이다 8 + 4 = 12 새로운 수는 42이다 4 + 2 = 6이다. 새로운 수는 26이다
# 위의 예는 4번만에 원래 수로 돌아올 수 잇따. 따라서 26의 사이클 길이는 4이다.
# N이 주어졌을 때, N의 사이클 길이를 구하는 프로그램 작성

# N = int(input())
# result = 0
# T = N
# r_list = []


# while True:
#     if T >= 10:
#         result = (T//10) + (T%10)
#         result = int(str(T%10) + str(result%10))
    
#     else:
#         result = 0 + T
#         result = int(str(T%10) + str(result%10))

#     if result != N:
#         r_list.append(result)
#         T = result

#     else:
#         r_list.append(result)
#         break

# print(len(r_list))

# 다른 풀이
# N = str(input()).zfill(2)
# result = 0
# T = N
# count = 0

# while True:
#     count += 1
#     result = T[1] + str(int(T[0]) + int(T[1])).zfill(2)[1]
#     result = str(result).zfill(2)
    
#     if int(result) == int(N):
#         break
#     else:
#         T = result

# print(count)


# 10807번 개수 세기
# N개 정수 주어졌을 때 정수 v가 몇개인가
# 첫 줄에는 정수 개수 N
# 둘째 줄에는 정수 공백
# 셋째 줄에는 찾으려는 정수 v가 주어진다

# N = int(input())
# numbers = list(map(int, input().split()))
# v = int(input())

# print(numbers.count(v))

# h, w = map(int, input().split())
# n = int(input())
# l, d, (x, y) = map(int, input().split())


# 10871번 X보다 작은 수
# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성

# 첫째 줄에 N과 X가 주어진다
# 둘째 줄에 수열 A를 이루는 정수 N개가 주어진다.

# X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력

# X, N = map(int, input().split())
# A = list(map(int, input().split()))
# N_list = []

# for n in A:
#     if n < N:
#         N_list.append(n)
# print(*N_list)


# 10818번 최소, 최대
# 첫째 줄에 정수의 개수 N이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다.

# 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력

# import sys

# N = int(sys.stdin.readline())
# M = list(map(int, sys.stdin.readline().split()))
# print(min(M), max(M), sep=' ')


# 2562번 최댓값
# result = 0
# r_list = []
# for n in range(9):
#     N = int(input())
#     r_list.append(N)

# for m in r_list:
#     result += 1
#     if m == max(r_list):
#         print(m, result, sep="\n")


# 5597 과제 안 내신 분..?
# X대학 M교수님은 프로그래밍 수업을 맡고 있다. 교실엔 학생이 30명이 있는데, 학생 명부엔 각 학생별로 1번부터 30번까지 출석번호가 붙어 있다.
# 교수님이 내준 특별과제를 28명이 제출했는데, 그 중에서 제출 안 한 학생 2명의 출석번호를 구하는 프로그램을 작성하시오.

# 입력 수 총 28줄로 각 제출자(학생)의 출석번호 n가 한줄에 하나씩 주어진다. 번호중복x
# 출력은 두줄이다 1째줄엔 제출하지 않은 학생의 출석번호중 가장 작은것, 2번째에선 그 다음 출선번호 출력


# N_list = []
# N2_list = []

# for n in range(1, 29):
#     N = int(input())
#     N_list.append(N)

# for i in range(1,31):
#     if i not in N_list:
#         N2_list.append(i)

# N2_list = sorted(N2_list)

# print(N2_list[0], N2_list[1], sep='\n')


# 3052번 나머지
# 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 
# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

# 첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩 주어진다. 이 숫자는 1,000보다 작거나 같고, 음이 아닌 정수이다.

# 첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력한다.

# result = 0
# A_list = []
# r_list = []

# for m in range(10):
#     A = int(input())
#     A_list.append(A)

# for n in A_list:
#     result = n % 42
#     if result not in r_list:
#         r_list.append(result)

# print(len(r_list))


# 1546번 평균
# 받은 점수중 최댓값 M 설정, 모든 점수를 점수/M*100으로 수정
# ex) max = 70 , math = 50 -> math = 50/70*100 = 71.43

# 첫째 줄에 과목 개수 N, 둘째 줄에 현재성적이 주어진다. 

# 첫째 줄에 새로운 평균을 출력

# N = int(input())
# M = list(map(int, input().split()))
# X = max(M)
# r_list = []
# result = 0

# for n in M:
#     result = n / X * 100
#     r_list.append(result)
    

# print(sum(r_list)/N)


# 8958번 OX퀴즈
# N = int(input())

# for n in range(N):
#     S = input()
#     r_list = []
#     result = 0
#     for m in S:
#         if m == 'O':
#             result += 1 
#             r_list.append(result)
#         else:
#             result = 0
#             r_list.append(result)

#     print(sum(r_list))


# 4344번 평균은 넘겠지
# 테스트 케이스 C
# 테스트 케이스마다 학생의수 N, N명의 점수

# C = int(input())

# for i in range(C):
#     N = list(map(int, input().split()))
#     average = (sum(N) - N[0]) / N[0]
#     r_list = []
#     for n in N[1::]:
#         if n > average:
#             r_list.append(n)

#     print(f'{"%.3f" % ((len(r_list)*100) / N[0])}%')


# 15596번 정수 N개의 합
# a: 합을 구해야 하는 정수 n개가 저장되어 있는 리스트
# 리턴값: a에 포함되어 있는 정수n개의 합
# def solve(a):
#     ans = sum(a)
#     return ans

# n = list(map(int, input().split()))
# print(solve(n))

# 11654번 아스키 코드
# 알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때
# 입력 : 알파벳 소문자, 대문자, 숫자 0-9중 하나가 첫째 줄에 주어진다.
# 출력 : 입력으로 주어진 글자의 아스키 코드 값을 출력한다.

# code = input()
# print(ord(code))


# 10809번 알파벳 찾기
# 알파벳 소문자로만 이루어진 단어S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력
# 입력 : 첫줄에 단어 S 입력
# 출력 : 각각의 알파벳에 대해서, a 가 처음 등장하는 위치, b가 처음 등장하는 위치 .... 를 공백으로 구분해서 출력
# 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력\

# S = input()
# alphabet = []

# for n in range(97, 123):
#     alphabet.append(chr(n))

# r_list = []

# for m in alphabet:
#     result = 0
#     if m in S:
#         for l in S:
#             if l == m:
#                 r_list.append(result)
#                 break
#             else:
#                 result += 1
#     else:
#         r_list.append(-1)

# print(*r_list)

# # 2675번 문자열 반복
# T = int(input())
# for t in range(T):
#     A, B = input().split()
#     A = int(A)
#     result = [a*A for a in B]
#     print(*result, sep='')


# # 1157 단어 공부
# S = input()
# alpha = {}

# for i in S.upper():
#     if i not in alpha:
#         alpha[i] = 1
#     else:
#         alpha[i] += 1

# a_list = []

# for key, value in alpha.items():
#     a_list.append(key)

# if len(a_list) == 1:
#     print(a_list[0])

# else:
#     for i in range(len(alpha)):
#         min_index = i
#         for j in range(i + 1, len(alpha)):
#             if alpha[a_list[min_index]] > alpha[a_list[j]]:
#                 min_index = j
#                 a_list[i], a_list[min_index] = a_list[min_index], a_list[i]

#     if alpha[a_list[-1]] == alpha[a_list[-2]]:
#         print('?')

#     else:
#         print(a_list[-1])


# # 1152번 단어의 개수
# # 영어 대소문자와 공백으로 이루어진 문자열이 주어질 때 몇개의 단어가 있는가(중복 포함)
# # 입력 : 첫 줄에 영어 대소문자와 공백으로 이루어진 문자열이 주어진다.
# # 출력 : 단어의 갯수

# S = input().split()
# String = {}

# for s in S:
#     if s not in String:
#         String[s] = 1
#     else:
#         String[s] += 1

# v_list = []

# for k in String.keys():
#     v_list.append(String[k])

# print(sum(v_list))


# 2908번 상수
# 상수는 수를 거꾸로 읽는다 이때 주어진 숫자들중 큰값을 출력해라

# 입력 : 두 수 A, B 입력
# 출력 : 뒤집은 후 큰값 출력

# A, B = input().split()

# if int(A[::-1]) > int(B[::-1]):
#     print(A[::-1])
# else:
#     print(B[::-1])


# 1712번 손익분기점
# A = 매년 임대료, 재산세 등 내야하는 금액
# B = 노트북을 생산하는데 드는 재료비와 인건비 등
# C = 노트북 가격
# ex) A = 1000, B = 70  > 1대 1070원, 10대 1700원

# 최초로 총 수입이 총 비용보다 많아지는 지점 출력
# import sys

# A, B, C = map(int, sys.stdin.readline().split())

# if B >= C:
#     print(-1)

# else:
#     N = int((A / (C - B)) + 1)
#     print(N)
    
        
# # 2292번 벌집
# N = int(input())

# n = 1
# result = 1
# if result == N:
#     print(1)
# else:
#     while True:
#         if result < N and N <= result+6*n:
#             print(n+1)
#             break
#         else:
#             result += 6*n
#             n += 1


# 1193번 분수찾기
X = int(input())
result = 1
n = 1
while True:
    if result <= X and X < result + n:
        t = X - result
        if n % 2 == 0:
            print("%d/%d" %(t + 1, n - t))
        else:
            print("%d/%d" %(n - t, t + 1))
        break
    else:
        result += n
        n += 1