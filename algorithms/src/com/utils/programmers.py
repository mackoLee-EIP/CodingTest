import sys


class Inputs:
    def __init__(self, test_file):
        sys.stdin = open(test_file)
        global input
        input = sys.stdin.readline

    @staticmethod
    def get_list_str():
        return list(map(lambda x: x.strip(), input().replace('"', '').split(',')))

    @staticmethod
    def get_list_int():
        return list(map(int, input().split(',')))