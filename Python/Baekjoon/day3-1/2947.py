# 2947번 나무 조각
numbers = list(map(int, input().split()))
r_numbers = sorted(numbers)

while True:
    if numbers != r_numbers:
        for n in range(len(numbers)-1):
            if numbers[n] > numbers[n+1]:      
                numbers[n], numbers[n+1] = numbers[n+1], numbers[n]
                print(*numbers)
    
    else:
        break
