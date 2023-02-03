# 2754번 학점계산
N = input()
result = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
if N != 'F':
    if N[1] == '0':
        print(result[N[0]])
    elif N[1] == '+':
        print(result[N[0]] + 0.3)
    else:
        print(result[N[0]] - 0.3)

else:
    print(result[N[0]])