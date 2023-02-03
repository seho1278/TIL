# 2720번 세탁소 사장 동혁
# 거스름돈의 액수가 주어지면 리암이 줘야할 쿼터의 개수, 다임의 개수, 니켈의 개수, 페니의 개수를 구하는 프로그램 작성
# 거스름돈은 항상 $5.00 이하, 손님이 받는 동전의 개수를 최소로

# 입력 : 첫 줄에 테스트 케이스 개수 T, 각 테스트 케이스는 거스름돈 C를 나타내는 정수 C의 단위는 센트

def div(x):
    x_list = []
    x1 = divmod(x, 25)
    x_list.append(x1[0])
    x2 = divmod(x1[1], 10)
    x_list.append(x2[0])
    x3 = divmod(x2[1], 5)
    x_list.append(x3[0])
    x4 = divmod(x3[1], 1)
    x_list.append(x4[0])
    return x_list

T = int(input())

for t in range(T):
    C = int(input())
    print(*div(C))