#  10840

# list = []
# for i in range(20):
#     list.append(i + 1)
#
# arrList = []
# elist = []
#
# for _ in range(10):
#     arrList.append(input().split())
#
# for i in range(10):
#     n = int(arrList[i][0]) - 1
#     m = int(arrList[i][1]) - 1
#
#     elist = list[n:m + 1]
#     elist.reverse()
#
#     list[n:m + 1] = elist
#
# for j in list:
#     print(j, end=" ")

arr = [i for i in range(21)]
for _ in range(10):
    start, end = map(int, input().split())
    arr[start:end + 1] = arr[end:start - 1:-1]
for i in range(1, 21):
    print(arr[i], end=' ')
