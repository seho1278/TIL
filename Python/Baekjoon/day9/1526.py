# 1526번 가장 큰 금민수

N = int(input())
hate = ['0', '1', '2', '3', '5', '6', '8', '9']
nums = []
for n in range(4, N+1):
    for i in str(n):
        if i in hate:
            break
    else:
        nums.append(n)

print(max(nums))