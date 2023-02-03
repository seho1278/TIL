# 2846번 오르막길

N = int(input())

H = list(map(int, input().split()))

result2 = []
cnt = 0
while True:
    result = []
    
    for i in range(cnt, len(H)):
        if i != len(H)-1:
            if H[i] < H[i+1]:
                result.append(H[i])

            else:
                result.append(H[i])
                r = result[-1] - result[0]
                result2.append(r)
                cnt = i + 1
                break
        else:
            result.append(H[i])
            r = result[-1] - result[0]
            result2.append(r)
            cnt = i + 1
            break
    else:
        break

print(max(result2))
