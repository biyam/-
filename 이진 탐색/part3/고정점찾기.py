int(input())
lst = list(map(int,input().split()))

ix = "".join(list(str(i) for i in range(len(lst)) if i == lst[i]))

if ix == '':
    print('-1')
else:
    print(ix)
