# 타일채우기
import sys

class Solution:
    def __init__(self):
        test_file = 'resources/problem14852/test1'
        sys.stdin = open(test_file)
        global input
        input = sys.stdin.readline

        self.N = int(input())

    def solve(self):
        a = 1
        b = 2
        dp_sum = 6
        for i in range(2, self.N+1):
            c = 0
            c += dp_sum
            c += a
            c %= 1000000007
            a, b = b, c
            dp_sum += c*2
            dp_sum %= 1000000007
        print(c)

if __name__ == '__main__':
    Solution().solve()
