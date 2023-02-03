# 9498번 시험 성적
N = int(input())

if N >= 90:
    print('A')

elif N >= 80 and 90 > N:
    print('B')

elif N >= 70 and 80 > N:
    print('C')

elif N >= 60 and 70 > N:
    print('D')

else:
    print('F')