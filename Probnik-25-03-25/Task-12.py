for n in range(4, 10_000):
    st = '1' + '2' * n
    while '12' in st or '32' in st or '22' in st:
        st = st.replace('12', '22', 1)
        st = st.replace('32', '211', 1)
        st = st.replace('22', '3', 1)
    if sum(map(int, st)) % 6 == 0:
        print(n)
        break