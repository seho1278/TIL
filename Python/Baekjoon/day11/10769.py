# 10769번 행복한지 슬픈지
S = input()

emote = []
count = 0
result = 0
for s in S:
    if s == ':' or s == '-' or s == '(' or s == ')':
        emote.append(s)
        if ':' in emote and '-' in emote and ')' in emote:
            count += 1
            result += 1
            emote = []
        elif ':' in emote and '-' in emote and '(' in emote:
            count += 1
            result -= 1
            emote = []
else:
    if result > 0:
        print('happy')
    elif result == 0:
        if count == 0:
            print('none')
        else:
            print('unsure')
    else:
        print('sad')

