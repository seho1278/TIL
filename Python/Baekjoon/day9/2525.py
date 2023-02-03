# 2525번 오븐 시계

A, B = map(int, input().split())
C = int(input())

if B + C >= 60:
    A += ((B+C) // 60)
    B = ((B+C) % 60)
    
else:
    B += C

if A >= 24:
    A -= 24

print(A, B)

# divmod 이용

X = divmod(B+C, 60)

A += X[0]
B = X[1]

if A >= 24:
    A -= 24

print(A, B)