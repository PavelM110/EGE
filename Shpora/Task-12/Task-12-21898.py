for n in range(4, 10_000):
    st = '1' + '9' * n
    while '19' in st or '399' in st or '999' in st:
        st = st.replace('19', '9', 1)
        st = st.replace('399', '91', 1)
        st = st.replace('999', '3', 1)
    if sum(map(int, st)) == 33:
        print(n)
        break