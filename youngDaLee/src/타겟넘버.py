"""
numbers = [4,1,2,1]
target = 4
�� ��� �ó�����

dfs([-4], [1,2,1], 4, 4)
    -> dfs([-4,-1], [2,1], 4, 4)
        -> dfs([-4,-1,-2], [1], 4, 4)
            -> dfs([-4,-1,-2,-1], [], 4, 4) => 0
            -> dfs([-4,-1,-2,1], [], 4, 4) => 0
        -> dfs([-4,-1,2], [1], 4, 4)
            -> dfs([-4,-1,2,-1], [], 4, 4) => 0
            -> dfs([-4,-1,2,1], [], 4, 4) => 0
    -> dfs([-4,1], [2,1], 4, 4)
        -> dfs([-4,1,-2], [1], 4, 4)
            -> dfs([-4,1,-2,-1], [], 4, 4) => 0
            -> dfs([-4,1,-2,1], [], 4, 4) => 0
        -> dfs([-4,1,2], [1], 4, 4)
            -> dfs([-4,1,2,-1], [], 4, 4) => 0
            -> dfs([-4,1,2,1], [], 4, 4) => 0
dfs([4], [1,2,1], 4, 4)
    -> dfs([4,-1], [2,1], 4, 4)
        -> dfs([4,-1,-2], [1], 4, 4)
            -> dfs([4,-1,-2,-1], [], 4, 4) => 0
            -> dfs([4,-1,-2,1], [], 4, 4) => 0
        -> dfs([4,-1,2], [1], 4, 4)
            -> dfs([4,-1,2,-1], [], 4, 4) => 1
            -> dfs([4,-1,2,1], [], 4, 4) => 0
    -> dfs([4,1], [2,1], 4, 4)
        -> dfs([4,1,-2], [1], 4, 4)
            -> dfs([4,1,-2,-1], [], 4, 4) => 0
            -> dfs([4,1,-2,1], [], 4, 4) => 1
        -> dfs([4,1,2], [1], 4, 4)
            -> dfs([4,1,2,-1], [], 4, 4) => 0
            -> dfs([4,1,2,1], [], 4, 4) => 0

=> res = 2
"""
def dfs(array, numbers, target, size):
    answer = 0
    if len(array) == size:  # ���� ���� ���
        if sum(array) == target:
            return 1
        else:
            return 0
    else:
        num = numbers.pop(0)
        for i in [-1, 1]:  # num�� ����/����� ��� ��������� ����
            array.append(num*i)
            answer += dfs(array, numbers, target, size)
            array.pop()
        numbers.append(num)
        return answer

def solution(numbers, target):
    answer += dfs([numbers[0]], numbers[1:], target, len(numbers))
    answer += dfs([-numbers[0]], numbers[1:], target, len(numbers))
    return answer