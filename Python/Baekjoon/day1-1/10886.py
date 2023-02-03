# 10886번 0 = not cute / 1 = cute
result = []
for n in range(5):
    result.append(int(input()))

if result.count(1) > result.count(0):
    print('Junhee is cute!')

else:
    print('Junhee is not cute!')