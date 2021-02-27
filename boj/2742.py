# 찍기 N 반대로

import sys
class Solution:
    input = sys.stdin.readline
    def solution(self):
        [print(i) for i in range(int(input()), 0, -1)]

Solution().solution()