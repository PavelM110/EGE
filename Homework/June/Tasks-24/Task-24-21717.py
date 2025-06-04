with open('24_21717.txt') as file:
    data = file.readline()

data = data.split('RSQ')

ans = 10 ** 10

for i in range(1, len(data) - 129):
    st = 'RSQ' + 'RSQ'.join(data[i:i + 129]) + 'RSQ'
    post_st = data[i + 129]
    if post_st == '':
        st += 'R'
    elif post_st[0] != 'Q':
        st += post_st[0]
    elif set(post_st) == {'Q'}:
        st += post_st + 'R'
    else:
        cnt = 0
        while post_st[cnt] == 'Q':
            cnt += 1
        st += post_st[:cnt + 1]
    ans = min(ans, len(st))

print(ans)
