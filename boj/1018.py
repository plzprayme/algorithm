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
        wood = [input() for i in range(N)]
        white = [
            'WBWBWBWB',
            'BWBWBWBW',
            'WBWBWBWB',
            'BWBWBWBW',
            'WBWBWBWB',
            'BWBWBWBW',
            'WBWBWBWB',
            'BWBWBWBW'
        ]

        black = [
            'BWBWBWBW',
            'WBWBWBWB',
            'BWBWBWBW',
            'WBWBWBWB',
            'BWBWBWBW',
            'WBWBWBWB',
            'BWBWBWBW',
            'WBWBWBWB'
        ]

        def window(r, c, _mask):
            updated = 0
            for row in range(r, r+8):
                for col in range(c,c+8):
                    if wood[row][col] != _mask[row-r][col-c]:
                        updated += 1
            print(f'row: {r}, col: {c}, updated: {updated}')
            return updated

        answer = float('inf')
        for row in range(N-7):
            for col in range(M-7):
                answer = min(answer, window(row, col, white))
                answer = min(answer, window(row, col, black))
        
        return answer

print(Solution().solution())

