from fnmatch import fnmatch

for i in range(141, 10**8, 141):
    if fnmatch(str(i), '1234*7'):
        print(i, i // 141)