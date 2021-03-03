
import sys
class Solution:
    input = sys.stdin.readline
    def solution(self):
        [print(sum(map(int, input().split()))) for i in range(int(input()))]

Solution().solution()