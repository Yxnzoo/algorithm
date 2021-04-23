# 10808

import sys
import string

s = sys.stdin.readline().rstrip()
alphabet = string.ascii_lowercase

for i in alphabet:
    cnt = 0
    for j in range(len(s)):
        if s[j] == i:
            cnt += 1
    print(cnt)
