#  13300
import math
import sys

k, n = map(int, sys.stdin.readline().split())
# 성별 / 학년
student = [[0]*7 for _ in range(3)]

for _ in range(k):
    s, y = map(int, sys.stdin.readline().split())
    student[s][y] += 1

room = 0
for i in student:
    for j in i:
        room += math.ceil(j/n)

print(room)
