st = '1' * 100

while '111' in st or '88888' in st:
    if '111' in st: st = st.replace('111', '88', 1)
    else: st = st.replace('88888', '8', 1)

print(st)