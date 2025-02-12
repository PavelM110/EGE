from itertools import permutations

alph = 'хочу в вуз'
cnt = 0

for val in set(permutations(alph)):
    val = ''.join(val)
    sent = val.split()
    if len(sent) == 3 and val != alph:
        if all(i[0] != 'у' for i in sent):
            cnt += 1
    # if val[0] not in ' у':
    #     if ' у' not in val and '  ' not in val and val[-2:] != '  ':
    #         cnt += 1

print(cnt)