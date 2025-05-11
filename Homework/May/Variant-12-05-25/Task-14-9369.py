ans = []

for x in '0123456789abcdef':
    for y in '0123456789abcdef':
        num1 = int(f'27a{x}23', 16)
        num2 = int(f'8{y}e5d2', 16)
        num = num1 + num2
        if num % 5 == 0:
            ans.append(int(x, 16) + int(y, 16))

print(max(ans))