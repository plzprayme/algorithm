# 문제 #
# 주어진 숫자를 거꾸로 뒤집은 후 대소비교

# 입력 #
# 서로 다른 세 자리 수 A, B 이며 0이 포함되어 있지 않다.

import sys
class Solution:
    input = sys.stdin.readline
    def solution(self):
        A, B = input().split()
        return max(int(A[::-1]), int(B[::-1]))

print(Solution().solution())