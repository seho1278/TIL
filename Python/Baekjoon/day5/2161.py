# 2161번 카드1
# N장의 카드를 1번 카드가 제일 위에 N번 카드가 제일 아래인 상태로 놓여있따.
# 1) 제일 위의 카드를 바닥에 버린다.
# 2) 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.

card = list(range(1, int(input()) + 1))
remove = []
while len(card) > 1:
    remove.append(card.pop(0))
    card.append(card.pop(0))

print(*remove, card[0])

