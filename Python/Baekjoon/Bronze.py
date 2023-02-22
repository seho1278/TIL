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
# X = int(input())
# result = 1
# n = 1
# while True:
#     if result <= X and X < result + n:
#         t = X - result
#         if n % 2 == 0:
#             print("%d/%d" %(t + 1, n - t))
#         else:
#             print("%d/%d" %(n - t, t + 1))
#         break
#     else:
#         result += n
#         n += 1


# 2869번 달팽이는 올라가고 싶다.

# A, B, V = map(int, input().split())

# x = (V-B)/(A-B)

# if x == int(x):
#     print(int(x))
# else:
#     print(int(x)+1)


# 10250번 ACM 호텔

# T = int(input())

# for t in range(T):
#     H, W, N = map(int, input().split())
    
#     result = N % H
#     result2 = N // H + 1
#     if N % H == 0:
#         result2 = N//H
#         result = h

#     print(f'{result*100+result2}')

# 다른사람 코드
# T = int(input())

# for i in range(T):
#     h, w, n = map(int, input().split( )) # h=각 호텔의 층 수, w=각 층의 방 수, n=몇 

#     floor = n % h 
#     room_line = (n // h) + 1
#     if floor == 0:
#         floor = h
#         room_line -= 1
    
#     print(floor * 100 + room_line)


# 2775번 부녀회장이 될테야
# T = int(input())

# for t in range(T):
#     k = int(input())
#     n = int(input())
#     a = [_ for _ in range(1, n+1)]
    
#     for i in range(k):
#         for j in range(1, n):
#             a[j] += a[j-1]
        
#     print(a[-1])


# 10757번 큰 수 A+B

# A, B = map(int, input().split())

# print(A+B)


# 11653번 소인수분해
# N = int(input())

# while True:
#     for i in range(2, N+1):
#         if N % i == 0:
#             print(i)
#             N = int(N/i)
#             break
#     if N == 1:
#         break

# 2738번 행렬 덧셈
# NxM 크기의 두 행렬 A, B가 주어졌을 때 두 행렬을 더하는 프로그램 작성
# 첫째 줄에 행렬의 크기 N과 M이 주어진다.
# 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다

# N, M = map(int, input().split())
# A, B = [], []

# for n in range(N):
#     num = list(map(int, input().split()))
#     A.append(num)

# for n in range(N):
#     num = list(map(int, input().split()))
#     B.append(num)

# for i in range(N):
#     for j in range(M):
#         print(A[i][j] + B[i][j], end=' ')
#     print()


# 최댓값
# matrix = []
# result = 0
# row = 0
# col = 0
# for _ in range(9):
#     num = list(map(int, input().split()))
#     matrix.append(num)

# for i in range(9):
#     for j in range(9):
#         if matrix[i][j] >= result:
#             result = matrix[i][j]
#             row = j + 1
#             col = i + 1

# print(result)
# print(col, row)


# 2587번 대표값2
# N = [int(input()) for _ in range(5)]

# # center = int(len(N)/2)
# N = sorted(N)
# print(int(sum(N)/5), N[2], sep='\n')


# 25305번 커트라인

# N, k = map(int, input().split())

# x = list(map(int, input().split()))
# x = sorted(x, reverse=True)
# print(x[k-1])


# 10989번 수 정렬하기 3
# import sys

# N = int(sys.stdin.readline())

# num = [0] * 10001 # 자연수 N이 10000까지 있기 때문에 +1 

# for _ in range(N):
#     temp = int(sys.stdin.readline())      # list를 dict 형태로 이용 ?
#     num[temp] += 1                        # 1~ 10000까지 입력할때마다 해당수 카운트하는 방식!

# for i in range(10001):
#     if num[i] != 0:   # 입력한 값이 리스트 안에 있을때
#         for j in range(num[i]):  # num[i] 의 개수만큼 출력
#             print(i)


# 1009 분산처리
# import sys

# T = int(sys.stdin.readline())

# for t in range(T):
#     a, b = map(int, sys.stdin.readline().split())
#     a = a % 10

#     if a == 0:
#         print(10)
#     elif a == 1 or a == 5 or a == 6:
#         print(a)
#     elif a == 4 or a == 9:
#         b = b % 2
#         if b == 1:
#             print(a)
#         else:
#             print((a*a)%10)
#     else:
#         b = b % 4
#         if b == 0:
#             print((a**4) % 10)
#         else:
#             print((a**b)% 10)


# 1032번 명령 프롬프트
# N = int(input())
# list_ = []
# for n in range(N):
#     S = list(input())
#     list_.append(S)

# result = []

# for i in range(N):
#     for j in range(i, N):
#         for m in range(len(S)):
#             for k in range(m,m+1):
#                 if list_[i][m] == list_[j][k]:
#                     if j == 0:
#                         result.append(list_[i][m])
#                     else:
#                         if result[m] == list_[i][m]:
#                             result[m] = list_[i][m]
#                 else:
#                     if j == 0:
#                         result.append('?')
#                     else:
#                         result[m] = '?'

# print(*result, sep = '')


# 1037 약수
# 양수 A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니어야 한다. 어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램을 작성하시오
# 입력 : 첫줄에 N의 진짜 약수의 개수 (0 < X <= 50), 둘째 줄에는 N의 진짜 약수(2 <= Y <= 1,000,000)

# N = int(input())
# nums = list(map(int, input().split()))

# if 2 in nums:
#     print(max(nums)*2)
# else:
#     if len(nums) == 1:
#         print(max(nums)**2)
#     else:
#         print(max(nums)*min(nums))


# 1075번 나누기
# 두 정수 N과 F가 주어진다. 정수 N의 가장 뒤 두자리를 적절히 바꿔서 N을 F로 나누어 떨어지게 만들려고 한다. 가능한 것이 여러 가지일 경우, 뒤 두 자리를 가능하면 작게 만들려고 한다.
# ex ) N = 275, F = 5 -> 00 (200이 5로 나누어 떨어지기 때문) / N = 1021, F = 11 -> 01 (1001이 11로 나누어 떨어진다)

# 입력 : 첫 줄에 N(100 <= N <= 2,000,000,000), 둘째 줄에 F(0 < F <= 100)가 주어진다.
# 출력 : 첫째 줄에 마지막 두 자리를 모두 출력, 한자리이면 앞에 0을 추가해서 두자리로 만든다.

# N = input()
# F = int(input())

# for i in range(100):
#     if i < 10:
#         if int(N[:-2] + '0' + str(i)) % F == 0:
#             print('0' + str(i))
#             break
#     else:
#         if int(N[:-2] + str(i)) % F == 0:
#             print(str(i))
#             break
        


# 1271 엄청난 부자2

# N, M = map(int, input().split())
# print(int(N//M), int(N%M), sep='\n')


# 1085번 직사각형에서 탈출
# 한수는 지금(x, y)에 있다. 직사각형은 각 변이 좌표축에 평행하고, 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은(w,h)에 있다. 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램 작성

# x, y, w, h = map(int, input().split())
# list_ = []
# list_.append(w-x)
# list_.append(h-y)
# list_.append(x-0)
# list_.append(y-0)
# print(min(list_))


# 1076번 저항
# 전자 제품에는 저항이 들어간다 저항은 색 3개를 이용해서 그 저항이


# 1173번 운동
# 운동을하는 과정 = 1분단위, 매 분마다 운동과 휴식 중 하나 선택
# 운동 선택한 경우 영식이 맥박 T만큼 증가, 영식이 맥박이 X였다면 1분동안 운동후 맥박이 X+T 증가 X+T <= M 일때만 운동 가능
# 휴식 R만큼 감소 1분동안 휴식한경우 맥박 X-R, 맥박은 m보다 낮아지면 안된다. 따라서 X-R < m -> 맥박 = m
# 영식이 초기 맥박은 m이다 운동을 N분 하려고 할때 N분하는데 필요한 시간의 최솟값 구하기

# N, m, M, T, R = map(int, input().split())

# X = m
# for n in range(1, N+1):    
#     if X > m:
#         X = X + T
#     elif 


# 1145번 적어도 대부분의 배수
# nums = list(map(int, input().split()))
# n = min(nums)

# while True:
#     cnt = 0
#     for i in range(5):
#         if n % nums[i] == 0:
#             cnt += 1
#     if cnt > 2:
#         print(n)
#         break
#     n += 1

# 1159번 농구 경기

N = int(input())

dict_ = {}
for n in range(N):
    player = input()
    x = player[0]
    if x not in dict_:
        dict_[x] = 1
    else:
        dict_[x] += 1

list_ = []
for key, value in dict_.items():
    if value >= 5:
        list_.append(key)
        
list_ = sorted(list_)

if list_:
    print(*list_, sep='')
else:
    print('PREDAJA')