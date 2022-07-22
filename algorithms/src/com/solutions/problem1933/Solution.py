# 스카이라인
# gold 1
# 20:40 시작
# 22:05 끝
import sys
from queue import PriorityQueue

class Solution:
    def __init__(self):
        test_file = 'resources/problem1933/test1'
        sys.stdin = open(test_file)
        global input
        input = sys.stdin.readline

        self.N = int(input())
        self.LHR_list = []
        self.x_axis = set()
        for _ in range(self.N):
            L, H, R = map(int, input().split())
            self.LHR_list.append((L, H, R))
            self.x_axis.add(L)
            self.x_axis.add(R)
        self.x_axis = sorted(self.x_axis)
        self.LHR_list = sorted(self.LHR_list, reverse=True)

    def solve(self):
        self.min_R_pq = PriorityQueue()
        self.max_H_pq = PriorityQueue()
        self.removed_LHR_list = set()
        pre_H = -1
        for x in self.x_axis:
            self.start_of_building(x)
            self.end_of_building(x)
            if pre_H != self.get_H():
                pre_H = self.get_H()
                print(x, self.get_H(), end=' ')

    def start_of_building(self, x):
        while self.LHR_list and x == self.LHR_list[-1][0]:
            L, H, R = self.LHR_list.pop()
            LHR_id = len(self.LHR_list)
            self.min_R_pq.put((R, LHR_id))
            self.max_H_pq.put((-H, LHR_id))

    def get_H(self):
        while not self.max_H_pq.empty() and self.max_H_pq.queue[0][1] in self.removed_LHR_list:
            self.max_H_pq.get()
        if self.max_H_pq.empty():
            return 0
        return -self.max_H_pq.queue[0][0]

    def end_of_building(self, x):
        while not self.min_R_pq.empty() and x == self.min_R_pq.queue[0][0]:
            R, LHR_id = self.min_R_pq.get()
            self.removed_LHR_list.add(LHR_id)

