with open('24_21717 (1).txt') as file:
    data = file.readline()

data1 = data
data = data.split('RSQ')

ans = 10 ** 10

for i in range(1, len(data) - 129):
    st = 'RSQ' + 'RSQ'.join(data[i:i+129]) + 'RSQ'
    posl = data[i + 129]
    if posl == '': st += '1'
    elif posl[0] != 'Q': st += '1'
    elif set(posl) == {'Q'}: st += '1' * (len(posl) + 1)
    else:
        n = 0
        while posl[n] == 'Q':
            n += 1
            st += '1'
    ans = min(ans, len(st))

print(ans)