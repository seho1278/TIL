# 10817번 세 수

nums = list(map(int, input().split()))
nums = sorted(nums, reverse=True)
nums.pop(0)
print(nums[0])