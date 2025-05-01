from itertools import permutations

cnt = 0

for i in permutations('01234567', 6):
    if i[0] != '0':
        i = ''.join(i)
        st = i
        for j in '357': st = st.replace(j, '1')
        for j in '246': st = st.replace(j, '0')
        if '11' not in st and '00' not in st:
            if int(i, 8) % 5 == 0:
                cnt += 1

print(cnt)