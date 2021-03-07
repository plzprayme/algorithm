import sys
class Solution:
    input = sys.stdin.readline
    def solution(self):
        x = [input() for i in range(int(input()))]
        x = list(set(x))
        x.sort()
        x.sort(key=len)
        [print(i) for i in x]

Solution().solution()