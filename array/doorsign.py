#  1475
import math
import sys

n = sys.stdin.readline().rstrip()
numList = [[0] * 2 for _ in range(10)]

for i in range(10):
    numList[i][0] = i

for i in range(len(n)):
    for j in range(10):
        if numList[j][0] == int(n[i]):
            numList[j][1] += 1
maxi = 0
maxIndex = 0

for i in numList:
    if i[1] > maxi:
        maxi = i[1]
        maxIndex = i[0]

if maxIndex == 6 or maxIndex == 9:
    maxi = numList[6][1] + numList[9][1]
    maxi = math.ceil(maxi / 2)

print(maxi)
