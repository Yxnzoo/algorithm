# 1931

def solution(meet_list):
    answer = 0
    endTime = 0
    for i in range(len(meet_list)):
        if endTime <= meet_list[i][0]:
            endTime = meet_list[i][1]
            answer += 1
    return answer


n = int(input())
meet_list = []
for i in range(n):
    sh, eh = map(int, input().split())
    meet_list.append([sh, eh])

meet_list.sort(key=lambda x: (x[1], x[0]))
print(meet_list)
print(solution(meet_list))
