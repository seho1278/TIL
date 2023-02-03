# 9076번 점수 집계

T = int(input())

for t in range(T):
    nums = list(map(int, input().split()))
    nums = sorted(nums)
    nums.pop(0)
    nums.pop()
    
    if max(nums) - min(nums) >= 4:
        print('KIN')
    else:
        print(sum(nums))