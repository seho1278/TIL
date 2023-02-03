# 2480 주사위 세개
result = list(map(int, input().split()))

prize_list = []

for i in result:
    if result.count(i) == 3:
        prize_list.append(10000+(i*1000))
        
    elif result.count(i) == 2:
        prize_list.append(1000+(i*100))
        
    else: 
        prize_list.append(max(result)*100)

print(max(prize_list))


# 2480 - 1(조건문만 이용)
n1, n2, n3 = map(int, input().split()) 
p = 0

if n1 == n2 and n2 == n3:
    p = 10000 + n1 * 1000
elif n1 == n2 or n2 == n3 or n1 == n3:
    if n1 == n2:
        p = 1000 + n1 * 100
    elif n2 == n3:
        p = 1000 + n2 * 100
    else:
        p = 1000 + n3 * 100

elif n1 != n2 and n1 != n3 and n2 != n3:
    if n1 > n2 and n1 > n3:
        p = n1 * 100
    elif n2 > n1 and n2 > n3:
        p = n2 * 100
    else:
        p = n3 * 100