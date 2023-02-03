# 1436번 영화감독 숌

N = int(input())

nums = []
for i in range(1000*N):
    if '666' in str(i):
        nums.append(i)
print(nums[N-1])


# 리스트 컴프리헨션
N = int(input())
nums = [i for i in range(1000*N) if '666' in str(i)]
print(nums[N-1])