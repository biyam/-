array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 나중에 array[pivot] = array[0]이 될 거임
    left = start + 1 # 나중에 array[left] = array[pivot + 1]이 될 거임
    right = end # 나중에 array[right] = array[-1]이 될 거임
    while(left <= right): # 엇갈리지 않을 때까지
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
        # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
        quick_sort(array, start, right - 1)
        quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1) 
# start가 0이고 end가 len(array) - 1인 이유는 인덱스에 맞추기 위해. (인덱스는 0부터 시작함)
print(array)