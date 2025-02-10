from string import ascii_lowercase, digits

alph = digits + ascii_lowercase

for x in alph[:35][::-1]:
    num1 = int(f'6{x}qr{x}', 35)
    num2 = int(f'{x}59sh', 35)
    num3 = int(f'ph{x}69yw', 35)
    num = num1 + num2 + num3
    moda = int(max('012345678', key=lambda x: (str(num).count(x), int(x))))
    if num % moda ** 2 == 0:
        print(num // moda ** 2)
        break