ans = 0

for n in range(4, 1_000):
    st = '1' + '2' * n
    while '12' in st or '322' in st or '222' in st:
        st = st.replace('12', '2', 1)
        st = st.replace('322', '21', 1)
        st = st.replace('222', '3', 1)
    ans  = max(ans, len(st))

print(ans)