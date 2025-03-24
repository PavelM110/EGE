ans = 10000000000000

for n in range(4, 2000):
    st = '3' * n + '5'
    while '23' in st or '5333' in st or '33333' in st:
        st = st.replace('23', '3', 1)
        st = st.replace('5333', '32', 1)
        st = st.replace('33333', '55', 1)
    ans = min(ans, sum(map(int, st)))

print(ans)