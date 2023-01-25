# 1859 백만 장자 프로젝트
# 원재는 연속된 N일 동안의 물건의 매매가를 예측하여 알고 잇따.
# 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입가능
# 판매는 얼마든지 가능
# ex) 3일동안의 매매가가 1, 2, 3이라면 처음 두 날에 원료를 구매하여 마지막 날에 팔면 3의 이익을 얻을 수 있다.

# 입력 : 첫 번째 줄에 테스트 케이스 수 T가 주어진다
# 각 테스트 케이스 별로 첫 줄에는 자연수 N이 주어지고
# 둘째 줄에는 각 날의 매매가를 나타내는 N개의 자연수들이 공백으로 구분되여 순서대로 주어진다.

# 출력 : 각 테스트 케이스마다 '#x를 출력하고, 최대 이익을 출력한다.

# T = int(input())

# for t in range(T):
#     N = int(input())
#     nums = list(map(int, input().split()))
#     cnt = 0
#     result = 0

#     if nums[-1] != max(nums):
#         for i in range(N-1):
#             if nums[i] > nums[i+1]:
#                 result += (nums[i]*cnt)
#                 cnt -= cnt

#             else:
#                 cnt += 1
#                 result -= nums[i]
#         result += (nums[-1]*cnt)
    
#     else:
#         if nums.count(max(nums)) == 1:
#             for j in range(N):
#                 if nums[j] == max(nums):
#                     result += (nums[j]*cnt)
#                 else:
#                     cnt += 1
#                     result -= nums[j]
#         else:
#             for i in range(N-1):
#                 if nums[i] > nums[i+1]:
#                     result += (nums[i]*cnt)
#                     cnt -= cnt

#                 else:
#                     cnt += 1
#                     result -= nums[i]
#             result += (nums[-1]*cnt)
#     print(f'#{t+1} {result}')

# 정답 코드

# T = int(input())

# for t in range(T):
#   n = int(input())
#   l = list(map(int, input().split()))
#   cost = l[-1]
#   benefit = 0
#   for i in reversed(l):
#     if cost <= i:
#       cost = i
#     benefit += cost - i
#   print(f'#{t + 1} {benefit}')


# 1926번 간단한 369게임
# 1부터 순서대로 말하되 3, 6, 9가 들어가 있는 수는 말하지 않는다.
# 3, 6, 9가 들어간 갯수만큼 박수

# 입력: 정수N 주어졌을때 1~N까지 숫자 박수는 "-"로 출력

# N = int(input())

# for n in range(1, N + 1):
#     cnt = 0
#     if '3' in str(n) or '6' in str(n) or '9' in str(n):
#         cnt += str(n).count('3')
#         cnt += str(n).count('6')
#         cnt += str(n).count('9')
#         n = '-'*cnt

#     print(n, end=' ')


# 2007 패턴 마디의 길이
# 패턴에서 반복되는 부분을 마디라고 부른다.
# 문자열을 입력 받아 마디의 길이를 출력하는 프로그램 작성
# 입력 : 첫 줄에 테스트 케이스 개수 T

# T = int(input())

# for t in range(T):
#     S = input()
#     S_dict = {}
#     for i in S:
#         if i not in S_dict:
#             S_dict[i] = 1
#         else:
#             S_dict[i] += 1
#     result = 0
#     m = min(S_dict.values())
#     for j in S_dict.keys():
#         result += S_dict[j] // m

#     print(f'#{t+1} {result}')


# 2005번 파스칼의 삼각형
# 크기가 N인 파스칼의 삼각형 만들기
# 첫 번째 줄은 항상 숫자 1이다.
# 두 번째 줄부터 각 숫자들들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다.

# 입력 : 가장 첫 줄 테스트 케이스 개수 T, 그 아래로 각 테스트 케이스 N이 주어진다.
# 출력 : 파스칼 삼각형 출력
   

# for t in range(int(input())):
#  print(f'#{t+1}')
#  for i in range(int(input())):print(' '.join(str(11**i)))

# 참고        
# T = int(input())
  
# for test_case in range(1,T+1):
      
#     t = int(input())
#     result1 = []
#     for test in range(0,t):
#         result2 = []
#         for k in range(0,test+1):
#             if k == 0 or k == test:
#                 result2.append(1)
#             else:
#                 result2.append(result1[test-1][k-1]+result1[test-1][k])
#         result1.append(result2)
#     print("#{0}".format(test_case))
#     for i in result1:
#         print(*i)

# 정답 코드
# T = int(input())

# for t in range(T):
#     print(f'#{t+1}')
#     N = int(input())
#     result = []
#     for i in range(0, N):
#         result2 = []
#         for j in range(0, i+1):
#             if j == 0 or j == i:
#                 result2.append(1)
#             else:
#                 result2.append(result[i-1][j-1] + result[i-1][j])
#         result.append(result2)
#     for i in result:
#         print(*i)


# 2001번 파리 퇴치
# N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미
# M x M의 크기의 파리채를 한번 내리쳐 최대한 많은 파리를 죽이고자 한다.
# 이 때 파리의 개수를 구하라.

# 입력: 테스트케이스 T, 각 테스트 케이스 첫줄 N, M 다음 N x N 배열

# def M(x):
#     for i in range(x):
#         for j in range(x):



T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    M_list = []
    N_list = []

    for n in range(N):
        numbers = list(map(int, input().split()))
        N_list.append(numbers)

    for k in range(N-M+1):
        for l in range(N-M+1):
            R_list = []
            for i in range(M):
                for j in range(M):
                    R_list.append(N_list[k + i][l + j])
            M_list.append(sum(R_list))

    print(f'#{t+1} {max(M_list)}')