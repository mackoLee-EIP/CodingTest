def solution(n, horizontal):
    x, y = 0, 0
    answer = [[0] * n for _ in range(n)]
    answer[0][0] = 1
    num = 2
    # x, y
    for i in range(n - 1):
        x, y, num, horizontal = clean_room(answer, x, y, horizontal, num, n)

    return answer


def clean_room(answer, x, y, horizontal, num, n):
    if horizontal:
        x += 1
    else:
        y += 1

    if horizontal:  # 아래먼저 내려감.
        x, y, num = go_down(answer, x, y, num)
        x, y, num = go_left(answer, x, y, num)
    else:
        x, y, num = go_right(answer, x, y, num)
        x, y, num = go_up(answer, x, y, num)

    return x, y, num, not horizontal


def go_down(answer, x, y, num):
    while 1:
        if answer[y][x - 1] != 0:
            break
        answer[y][x] = num
        num += 1
        y += 1
    return x, y, num


def go_left(answer, x, y, num):
    while x > 0:
        answer[y][x] = num
        num += 1
        x -= 1

    answer[y][x] = num
    num += 1
    return x, y, num


def go_right(answer, x, y, num):
    while answer[y - 1][x] != 0:
        answer[y][x] = num
        num += 1
        x += 1
    return x, y, num


def go_up(answer, x, y, num):
    while y > 0:
        answer[y][x] = num
        num += 1
        y -= 1
    answer[y][x] = num
    num += 1
    return x, y, num