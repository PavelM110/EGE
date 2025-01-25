for n in range(2, 100):
    st = '>' + '0' * 21 + '1' * n + '2' * 11
    while '>1' in st or '>2' in st or '>0' in st:
        st = st.replace('>1', '22>', 1)
        st = st.replace('>2', '2>', 1)
        st = st.replace('>0', '1>', 1)
    summ = sum([int(i) for i in st[:-1]])
    if summ % n == 0:
        print(n)