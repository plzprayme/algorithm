

import sys
class Solution:
    input = sys.stdin.readline
    def solution(self):
        input()
        nums = list(map(int, input().split()))
        print(min(nums), max(nums))

Solution().solution()
