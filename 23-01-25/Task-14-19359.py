from string import digits, ascii_lowercase

alph = digits + ascii_lowercase

for x in alph[:22][::-1]:
    num1 = int(f'a23{x}ac0', 22)
    num2 = int(f'gb{x}21670', 22)
    num = num1 + num2
    if num % 21 == 0:
        print(num // 22)