with open('24_14502.txt') as file:
    data = file.readline()

# data = '11111111222223331313131312321123'


# ans = 10 ** 20
#
# for i in range(len(data) - 27):
#     for j in range(i + 26, len(data)):
#         st = data[i:j]
#         if len(set(st)) == 26:
#             ans = min(ans, len(st))
#             if len(st) == 26: break
#
# print(ans)

s = 0
e = 26
ans = 10**20

while e < len(data):
    e += 1
    st = data[s:e]
    while st.count(st[0]) > 1:
        s += 1
        st = data[s:e]
    if len(set(st)) == 26:
        ans = min(ans, len(st))
        s = e
        e = s + 26

print(ans)





























