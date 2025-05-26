for i in range(10000, 100000)[::-1]:
    val = str(i)
    for j in '2468': val = val.replace(j, '0')
    for j in '3579': val = val.replace(j, '1')
    if (i - 9999) % 15 == 0 and '00' not in val and '11' not in val:
        print(i - 9999)
        break