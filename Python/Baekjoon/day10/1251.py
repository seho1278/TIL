# 1251번 단어나누기

S = input()

result = []
for i in range(1, len(S)-1):
    for j in range(i+1, len(S)):
        result2 = []
        
        result2.append(S[:i])
        result2.append(S[i:j])
        result2.append(S[j:len(S)])

        result.append(result[0][::-1]+result[1][::-1]+result[2][::-1])

result = sorted(result)
print(result[0])