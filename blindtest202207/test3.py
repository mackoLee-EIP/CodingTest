import sys

sys.setrecursionlimit(50000000)

INF = 10000


def solution(rows, columns, lands):
    answer = [INF, -INF]
    visited = [[False] * columns for _ in range(rows)]
    lands = list(map(lambda x: tuple([x[0] - 1, x[1] - 1]), lands))

    find_sea(0, 0, visited, lands, rows, columns)

    for y in range(rows):
        for x in range(columns):
            if visited[y][x]:
                continue
            if (y, x) in lands:
                continue
            lake_area = find_lake(x, y, visited, lands, rows, columns)
            if lake_area > 0:
                answer[0] = min(answer[0], lake_area)
                answer[1] = max(answer[1], lake_area)
    if answer == [INF, -INF]:
        return [-1, -1]
    return answer


def find_sea(x, y, visited, lands, rows, columns):
    if visited[y][x]:
        return
    visited[y][x] = True
    for d in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        dx = x + d[0]
        dy = y + d[1]
        if not (0 <= dx < columns and 0 <= dy < rows):
            continue
        if (dy, dx) in lands:
            continue
        if visited[dy][dx]:
            continue
        find_sea(dx, dy, visited, lands, rows, columns)


def find_lake(x, y, visited, lands, rows, columns):
    if visited[y][x]:
        return 0
    visited[y][x] = True
    result = 1
    for d in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        dx = x + d[0]
        dy = y + d[1]
        if not (0 <= dx < columns and 0 <= dy < rows):
            continue
        if (dy, dx) in lands:
            continue
        if visited[dy][dx]:
            continue
        result += find_lake(dx, dy, visited, lands, rows, columns)
    return result
