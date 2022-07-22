'''
문제 설명
어느 왕국에 하나 이상의 도시들이 있습니다. 왕국의 왕은 새 도시를 짓기로 결정하였습니다. 해당 도시를 짓기 위해서는 도시를 짓는 장소에 금 a kg과 은 b kg이 전달되어야 합니다.

각 도시에는 번호가 매겨져 있는데, i번 도시에는 금 g[i] kg, 은 s[i] kg, 그리고 트럭 한 대가 있습니다. i번 도시의 트럭은 오직 새 도시를 짓는 건설 장소와 i번 도시만을 왕복할 수 있으며, 편도로 이동하는 데 t[i] 시간이 걸리고, 최대 w[i] kg 광물을 운반할 수 있습니다. (광물은 금과 은입니다. 즉, 금과 은을 동시에 운반할 수 있습니다.) 모든 트럭은 같은 도로를 여러 번 왕복할 수 있으며 연료는 무한대라고 가정합니다.

정수 a, b와 정수 배열 g, s, w, t가 매개변수로 주어집니다. 주어진 정보를 바탕으로 각 도시의 트럭을 최적으로 운행했을 때, 새로운 도시를 건설하기 위해 금 a kg과 은 b kg을 전달할 수 있는 가장 빠른 시간을 구해 return 하도록 solution 함수를 완성해주세요.

제한사항
0 ≤ a, b ≤ 109
1 ≤ g의 길이 = s의 길이 = w의 길이 = t의 길이 = 도시 개수 ≤ 105
0 ≤ g[i], s[i] ≤ 109
1 ≤ w[i] ≤ 102
1 ≤ t[i] ≤ 105
a ≤ g의 모든 수의 합
b ≤ s의 모든 수의 합
입출력 예
a	b	g	s	w	t	result
10	10	[100]	[100]	[7]	[10]	50
90	500	[70,70,0]	[0,0,500]	[100,100,2]	[4,8,1]	499
입출력 예 설명
입출력 예 #1

도시가 오직 하나뿐이므로, 0번 도시의 유일한 트럭이 모든 운반을 해결해야 합니다. 이 트럭은 최대 7kg만큼의 광물을 운반할 수 있으며 편도 완주에는 10시간이 걸립니다.
맨 처음에 10시간을 써서 7kg만큼의 금을 운반하고, 10시간을 써서 다시 도시로 돌아오고, 10시간을 써서 7kg만큼의 은을 운반하고, 10시간을 써서 다시 도시로 돌아오고, 마지막으로 10시간을 써서 3kg만큼의 금과 3kg만큼의 은을 운반하면, 총 50시간 만에 필요한 모든 금과 은을 조달할 수 있습니다.
따라서, 50을 return 해야 합니다.

'''

INF = 2**42

def calc_total_gs(gs):
    return sum(gs)


class programmers_금과은운바하기:
    def __init__(self):
        pass

    def solution(self, a, b, g, s, w, t):
        if a == 0 and b == 0:
            return 0
        return self.binary_search(a, b, g, s, w, t)

    def binary_search(self, a, b, g, s, w, t):
        _left = 0
        _right = INF
        while _left+1 < _right:
            _time = (_left + _right)//2
            _gs = self.how_many_gold_silver_in(_time, w, t)
            _total_gs = self.calc_total_gs(_gs)
            _max_g = self.calc_max_g(g, _gs)

            _max_s = self.calc_max_s(s, _gs)
            _total = a + b
            if _total_gs < _total:
                _left = _time
                continue
            if a > _max_g:
                _left = _time
                continue
            if b > _max_s:
                _left = _time
                continue
            _right = _time

        return _right

    def how_many_gold_silver_in(self, time, w, t):
        _result = []
        for ww, tt in zip(w, t):
            _one_way = time//tt
            _round_trip = _one_way//2
            _last_way = _one_way % 2

            _result.append(ww * (_round_trip + _last_way))
        return _result

    def calc_max_g(self, g, gs):
        return sum([min(gg, gsgs) for gg, gsgs in zip(g, gs)])

    def calc_max_s(self, s, gs):
        return sum([min(ss, gsgs) for ss, gsgs in zip(s, gs)])

    def calc_total_gs(self, gs):
        return sum(gs)



if __name__ == '__main__':
    input_values = [[10,	10,	[100],	[100],	[7],	[10]],
                    [90,	500,	[70,70,0],	[0,0,500],	[100,100,2],	[4,8,1]]]
    s = programmers_금과은운바하기()
    for input_value in input_values:
        print(s.solution(*input_value))