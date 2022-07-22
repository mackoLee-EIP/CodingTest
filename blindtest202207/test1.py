# def solution(grade):
#     answer = 0
#     pre = grade[-1]
#     for g in grade[::-1]:
#         value = max(0, g-pre)
#         answer += value
#         pre = g - value
#
#     return answer

def solution(grade: []):

    grade.reverse()

    temp = grade[0]
    answer = 0
    for i in range(len(grade)):
        if i > 0:
            diff = temp - grade[i]
            if diff < 0:
                answer += abs(diff)
            else:
                temp = grade[i]
    print(answer)

grade = [3, 2, 3, 6, 4, 5]
solution(grade)