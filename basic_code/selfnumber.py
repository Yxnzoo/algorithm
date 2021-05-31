#  4763
nat_num = set(range(1, 10001))
gen_num = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    gen_num.add(i)

self_num = sorted(nat_num - gen_num)
for i in self_num:
    print(i)
