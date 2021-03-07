
import sys
class Solution:
    input = sys.stdin.readline
    def solution(self):
        x, y, w, h = map(int, input().split())
        return min(x, y, w-x, h-y)

print(Solution().solution())
