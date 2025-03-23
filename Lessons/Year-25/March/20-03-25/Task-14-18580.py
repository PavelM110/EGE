from string import digits, ascii_lowercase

alph = digits + ascii_lowercase

for x in alph[:25][::-1]:
    num1 = int(f'a4{x}7f2', 25)
    num2 = int(f'n{x}g5{x}h', 25)
    num3 = int(f'74{x}m26', 25)
    num = num1 + num2 + num3
    if num % 24 == 0:
        print(num // 24)
        break