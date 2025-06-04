ans = 0

for n in range(4, 10_000):
    st = '8' + '4' * n
    while '11' in st or '444' in st or '8888' in st:
        st = st.replace('11', '4', 1)
        st = st.replace('444', '88', 1)
        st = st.replace('8888', '1', 1)
    ans = max(ans, sum(map(int, st)))

print(ans)