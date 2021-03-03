# 문제 #
# A+B
# A-B
# A*B
# A/B
# A%B

import sys
class Solution:
    input = sys.stdin.readline
    def solution(self):
        A, B = map(int, input().split())
        print(A+B)
        print(A-B)
        print(A*B)
        print(A//B)
        print(A%B)
Solution().solution()