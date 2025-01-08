from fnmatch import fnmatch

pat = '1*28?64'

res = []

for i in range(127544, 199999928964, 596):
    if fnmatch(str(i), pat):
        res.append(i)

print(len(res), sum(res) / len(res))