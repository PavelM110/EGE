ans = 0

for n in range(4, 10_000):
    st = '3' + '5' * n
    while '333' in st or '555' in st:
        if '555' in st: st = st.replace('555', '3', 1)
        else: st = st.replace('333', '5', 1)
    ans = max(ans, sum(map(int, st)))

print(ans)