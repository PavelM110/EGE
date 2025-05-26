for n in range(101, 1000):
    st = '5' * n
    while '555' in st or '11'in st or '2' in st:
        st = st.replace('555', '1', 1)
        st = st.replace('11', '25', 1)
        st = st.replace('2', '5', 1)
    if st == '15':
        print(n)
        break