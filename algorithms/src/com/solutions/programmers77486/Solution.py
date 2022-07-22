# programmers
# 다단계 칫솔 판매
from com.utils.programmers import Inputs
from collections import deque


class Solution:
    en_ref = None
    people_made_profit = None
    total_profit = None

    def __init__(self):
        test_file = 'resources/programmers77486/test1'
        inputs = Inputs(test_file)
        enroll = inputs.get_list_str()
        referral = inputs.get_list_str()
        seller = inputs.get_list_str()
        amount = inputs.get_list_int()

        print(enroll, referral, seller, amount)
        self.answer = self.solve(enroll, referral, seller, amount)

    def solve(self, enroll, referral, seller, amount):
        self.set_referral_by_name(enroll, referral)
        self.set_people_made_profit(seller, amount)
        self.set_total_profit(enroll)
        #
        while self.people_remain():
            self.hand_out_profit()

        return self.get_total_profit_list(enroll)

    def get_referral_by_name(self, name):
        return self.en_ref[name]

    def get_total_profit_list(self, enroll):
        return [self.total_profit[name] for name in enroll]

    def set_referral_by_name(self, enroll, referral):
        self.en_ref = {name: r for name, r in zip(enroll, referral)}

    def set_people_made_profit(self, seller, amount):
        self.people_made_profit = deque([{
            "name": s, "profit": a*100
        } for s, a in zip(seller, amount)])

    def set_total_profit(self, enroll):
        self.total_profit = {
            name: 0 for name in enroll
        }

    def people_remain(self):
        return len(self.people_made_profit) > 0

    def hand_out_profit(self):
        _person_made_profit = self.people_made_profit.popleft()

        _name = _person_made_profit['name']
        _profit = _person_made_profit['profit']

        _referral_name = self.get_referral_by_name(_name)

        _percent10 = _profit // 10
        _my_profit = _profit - _percent10
        self.total_profit[_name] += _my_profit

        if _percent10 == 0:
            return

        if _referral_name == '-':
            return

        self.people_made_profit.append({'name': _referral_name,'profit': _percent10})
