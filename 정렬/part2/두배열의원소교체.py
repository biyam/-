n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = sorted(a)
b = sorted(b, reverse = 1)
print(a)
print(b)
# a = [1, 2, 5, 4, 3]
# b = [5, 5, 6, 6, 5]

cnt = 0
for i in range(n):
    if b[i] > a[i]:
        a[i] = b[i]
        cnt += 1
        if cnt == 3:
            break
    else:
        continue
    
print(a)
print(sum(a))