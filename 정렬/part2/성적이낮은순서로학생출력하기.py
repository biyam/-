num = int(input())
dict = {}
for i in range(num):
    name, score = map(str, input().split())
    dict[name] = int(score)

dict = sorted(dict.items(), key = lambda x: x[1])

for i in dict:
    print(i[0], end = ' ')