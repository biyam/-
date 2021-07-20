n = int(input())
array = []
for i in range(n):
    num = int(input())
    array.append(num)

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]
    # pivot의 왼쪽과 오른쪽
    left = [x for x in tail if x < pivot]
    right = [x for x in tail if x > pivot]

    return left + [pivot] + right

res = quick_sort(array)
for i in res:
    print(i, end = ' ')