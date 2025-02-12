from itertools import permutations

alph = '0123456789'

cnt = 0
ans = []

for val1 in permutations(alph, 6):
    val = val1 = ''.join(val1)
    if val[0] != '0':
        val = int(val)
        if val % 4 == 0:
            val = str(val)
            for i in '02468':
                val = val.replace(i, '0')
            if '00' not in val: ans.append(val1)


print(len(ans), ans[:100], sep = '\n')