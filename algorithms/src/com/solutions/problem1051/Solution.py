# 숫자 정사각형
import sys

class Solution:
    def __init__(self):
        test_file = 'resources/problem1051/test1'
        sys.stdin = open(test_file)
        global input
        input = sys.stdin.readline

        self.N, self.M = map(int, input().split())

        self.board = []
        for i in range(self.N):
            self.board.append(input())

    def solve(self):
        for l in range(min(self.N, self.M), 1, -1):
            if self.can_square(l):
                print(l*l)
                return
        print(1)

    def can_square(self, l):
        for i in range(self.N - l + 1):
            for j in range(self.M - l + 1):
                if len({self.board[i][j], self.board[i+l-1][j], self.board[i][j+l-1], self.board[i+l-1][j+l-1]}) == 1:
                    return True
        return False


if __name__ == '__main__':
    Solution().solve()
