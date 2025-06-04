st = '9' * 100

while '33333' in st or '999' in st:
    if '33333' in st: st = st.replace('33333', '99', 1)
    else: st = st.replace('999', '3', 1)

print(st)