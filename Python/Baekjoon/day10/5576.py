# 5576번 콘테스트

WU = [int(input()) for _ in range(10)]
KU = [int(input()) for _ in range(10)]

WU = sorted(WU, reverse=True)
KU = sorted(KU, reverse=True)
print(sum(WU[:3]), sum(KU[:3]))