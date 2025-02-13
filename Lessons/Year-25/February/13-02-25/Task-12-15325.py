st = '8' * 45

while '1111' in st or '8888' in st:
    if '1111' in st: st = st.replace('1111', '88', 1)
    else: st = st.replace('8888', '11', 1)

print(st)