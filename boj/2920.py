# 문제 #
# c d e f g a b C 총 8개의 음으로 이루어져있다.
# 1 2 3 4 5 6 7 8 로 바꿔서 표현한다.

# 입력 #
# 첫째 줄에 8개 숫자가 주어진다.
# ascending, descending, mixed 판별

import sys
class Solution:
    input = sys.stdin.readline
    def solution(self):
        note = '1 2 3 4 5 6 7 8'
        performed = input()

        if note == performed:
            return 'ascending'
        elif note[::-1] == performed:
            return 'descending'
        
        return 'mixed'
print(Solution().solution())
        