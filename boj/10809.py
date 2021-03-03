# 문제 #
# 알파벳 소문자로만 이루어진 단어 S가 주어진다.
# 포함되어 있는 경우에는 처음 등장하는 위치, 포함 x시는 -1출력

# 입력 #
# 단어 S / 단어 길이 100넘지 않음 소문자

import sys
class Solution:
    input = sys.stdin.readline
    def solution(self):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        word = input()
        for a in alphabet[:-1]:
            print(word.find(a), end=' ')
        print(word.find(alphabet[-1]), end='')

Solution().solution()