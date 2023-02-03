# 10101번 삼각형 외우기
# 세 각의 크기가 모두 60이면, Equilateral
# 세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
# 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
# 세 각의 합이 180이 아닌 경우에는 Error

# 입력 : 총 3개의 줄에 걸쳐 삼각형의 각의 크기가 주어진다.

N_list = []
for n in range(3):
    N = int(input())
    N_list.append(N)

if sum(N_list) != 180:
    print('Error')

elif sum(N_list) == 180:
    if N_list[0] == N_list[1] and N_list[0] == N_list[2]:
        print('Equilateral')

    elif N_list[0] != N_list[1] and N_list[0] != N_list[2] and N_list[1] != N_list[2]:
        print('Scalene')

    else:
        print('Isosceles')
