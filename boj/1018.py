# 문제 #
# M * N을 잘라서 8 * 8로 만든다.
# 변을 공유하는 두 사각형은 다른 색으로 칠해져있어야 한다.
# 맨 왼쪽 위가 흰색이거나 검은색인 경우만 존재한다.
# 다시 칠해야하는 정사각형 개수를 구하시오

# 입력 #
# 8 <= N, M <= 50
# 보드의 각 행의 상태 B와 W로 이루어짐


import sys
class Solution:
    input = sys.stdin.readline
    def solution(self):
        N, M = map(int, input().split())
        board = [input() for i in range(N)]
        pattern = ['W', 'B'] * 4

        def fill(row, col):
            refilled = 0
            for _row in range(row, row+8):
                for _col in range(col, col+8):
                    target = board[_row][_col]
                    if target == pattern[_col]:
                        continue
                    target = pattern[_col]
                    refilled += 1
            return refilled
                    



        result = float('inf')
        for row in range(N-7):
            for col in range(M-7):
                result = min(result, fill(row, col))
        
        return result

Solution().solution()

