from fnmatch import fnmatch

for i in range(12347 - 12347 % 141, 10**8, 141):
    if fnmatch(f'{i}', '1234*7'):
        print(i, i // 141)