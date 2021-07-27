a = int(input())
aa = list(map(int, input().split()))
b = int(input())
bb = list(map(int, input().split()))

for i in bb:
    if i in aa:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')