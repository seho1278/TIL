# 1453번 피시방 알바

# 앉으려는 번호(1~100)에 사람이 있으면 거절당한다고 할때 거절당하는 사람의 수를 출력하는 프로그램작성

# 입력 : 첫째 줄에 손님의 수 N이 주어진다. 둘째 줄에는 손님이 들어오는 순서대로 각 손님이 앉고 싶어하는 자리가 입력으로 주어진다.

N = int(input())
guest = map(int, input().split())
g_dict = {}
cnt = 0
for i in guest:
    if i not in g_dict:
        g_dict[i] = 1
    else:
        cnt += 1

print(cnt)
