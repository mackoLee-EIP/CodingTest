# 싸이버개강총회
import sys

class Solution:
    def __init__(self):
        test_file = 'resources/problem19583/test2'
        sys.stdin = open(test_file)
        global input
        input = sys.stdin.readline

        self.S, self.E, self.Q = input().split()

        self.chat_list = []
        try:
            while 1:
                line = input().split()
                if line == []:
                    break
                self.chat_list.append(line)
        except:
            pass
        self.chat_list.append([self.S, '~S'])
        self.chat_list.append([self.E, '!E'])
        self.chat_list.append([self.Q, '~Q'])
        self.chat_list.sort(reverse=True)

    def solve(self):
        before_meeting = set()
        while self.chat_list[-1][1] != '~S':
            before_meeting.add(self.chat_list.pop()[1])

        while self.chat_list[-1][1] != '!E':
            self.chat_list.pop()

        after_meeting = set()
        while self.chat_list[-1][1] != '~Q':
            after_meeting.add(self.chat_list.pop()[1])

        print(len(before_meeting & after_meeting))

if __name__ == '__main__':
    Solution().solve()
