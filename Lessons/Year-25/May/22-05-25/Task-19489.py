with open('24_19489.txt') as file:
    data = file.readline()

data = data.replace('WSFWW', 'WSFW SFWW').split()

ans = 0

for st in data:
    st = st.split('WWF')
    if len(st) >= 121:
        for i in range(len(st) - 120):
            s = 'WWF'.join(st[i:i+121])
            ans = max(ans, len(s))
    else:
        ans = max(ans, len('WWF'.join(st)))
print(ans)