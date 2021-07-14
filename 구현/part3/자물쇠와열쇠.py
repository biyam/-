# 0: 홈, 1: 돌기 --> 홈과 돌기가 맞아야 함. 근데 
# lock = N x N
# key = M x M (N 이하)

def solution(key, lock):
    answer = True
    return answer

KEY = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
LOCK = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(KEY, LOCK))