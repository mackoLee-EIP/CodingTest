# 숫자 정사각형
import sys

INF = 987654321

class Solution:
    def __init__(self):
        test_file = 'resources/problem18290/test5'
        sys.stdin = open(test_file)
        global input
        input = sys.stdin.readline

        self.N, self.M, self.K = map(int, input().split())

        self.board = []
        for i in range(self.N):
            self.board.append(list(map(int, input().split())))
        self.visited = [[False]*(self.M+2) for _ in range(self.N+2)]
        self.answer = -INF

    def solve(self):
        self.dfs(0, 0, self.K, 0)
        print(self.answer)

    def dfs(self, i, j, k, num):
        if k == 0:
            self.answer = max(self.answer, num)
            return
        if i == self.N:
            return
        ni = i+1 if j == self.M-1 else i
        nj = 0 if j == self.M-1 else j+1

        answer = self.dfs(ni, nj, k, num)
        for di, dj in ((-1, 0), (0, -1)):
            if self.get_visited(i+di, j+dj):
                break
        else:
            self.set_visited(i, j, True)
            self.dfs(ni, nj, k-1, num+self.board[i][j])
            self.set_visited(i, j, False)

    def get_visited(self, i, j):
        return self.visited[i+1][j+1]

    def set_visited(self, i, j, v):
        self.visited[i+1][j+1] = v

if __name__ == '__main__':
    Solution().solve()
