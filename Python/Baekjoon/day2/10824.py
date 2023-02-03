# 10824번 네 수
# 네 자연수 A, B, C, D 주어졌을 때, A, B를 붙인 수와 C, D를 붙인 수의 합을 구하라
# ex A : 20, B : 30 = 2030
# 입력 : 첫줄 네 자연수 A, B, C, D
# 출력 : A, B / C, D 붙인 수의 합 출력

A, B, C, D = input().split()
print(int(A + B) + int(C + D))