st = '>' + '3' * 10 + '5' * 10 + '7' * 10

while '>3' in st or '>5' in st or '>7' in st:
    st = st.replace('>3', '55>', 1)
    st = st.replace('>5', '5>3', 1)
    st = st.replace('>7', '3>5', 1)

print(sum(map(int, st[:-1])))