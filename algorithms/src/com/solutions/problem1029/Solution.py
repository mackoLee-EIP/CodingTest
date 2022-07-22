# 그림 교환
# gold 1
# 대략 두시간?
import sys


class Solution:
    def __init__(self):
        test_file = 'resources/problem1029/test1'
        sys.stdin = open(test_file)
        global input
        input = sys.stdin.readline

        self.N = int(input())

        self.artists = []

        for _id in range(self.N):
            _artist = Artist()
            _artist.id = _id
            _artist.sell_price = input()
            self.artists.append(_artist)

        # DP[N][10][2^(N+1)]
        self.DP = [[[-1] * (2 ** (self.N + 1)) for _ in range(10)] for _ in range(self.N)]

        self.solutions()

    def solutions(self):
        _selling_artist = self.artists[0]
        max_people = self.sell_draw(_selling_artist, selling_price=0, bit_bought_people=_selling_artist.to_bit())
        print(max_people)

    def sell_draw(self, selling_artist, selling_price, bit_bought_people):
        _max_people = self.DP[selling_artist.id][selling_price][bit_bought_people]
        if _max_people != -1:
            return _max_people
        _max_people = 0
        for buying_artist in self.artists:
            if buying_artist.id == selling_artist.id:
                continue
            if self.is_bought_person(buying_artist, bit_bought_people):
                continue

            buying_price = selling_artist.sell_to(buying_artist)

            if not self.sellable(selling_price, buying_price):
                continue

            new_bit_bought_people = bit_bought_people + buying_artist.to_bit()
            _max_people = max(_max_people, self.sell_draw(buying_artist, buying_price, new_bit_bought_people))

        getting_draw = 1
        _max_people += getting_draw

        self.DP[selling_artist.id][selling_price][bit_bought_people] = _max_people

        return _max_people

    @staticmethod
    def sellable(selling_price, buying_price):
        return selling_price <= buying_price

    @staticmethod
    def is_bought_person(artist, bit_bought_people):
        return bit_bought_people & artist.to_bit() > 0


class Artist:
    def __init__(self):
        self.sell_price = None
        self.id = None

    def sell_to(self, artist):
        return int(self.sell_price[artist.id])

    def to_bit(self):
        return 2 ** self.id