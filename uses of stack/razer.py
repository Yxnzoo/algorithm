#  10799

mb_razer = list(input())
answer = 0
stk = []

for i in range(len(mb_razer)):
    if mb_razer[i] == '(':
        stk.append('(')
    else:
        if mb_razer[i - 1] == '(':
            stk.pop()
            answer += len(stk)
        else:
            stk.pop()
            answer += 1

print(answer)