with open('26_4660.txt') as file:
    n = file.readline()
    data = [int(i) for i in file if i]

data = sorted(data, reverse=True)

sales_1 = [data[i] for i in range(3, int(n), 4)]
summ_1 = sum(data) - sum(sales_1)
sales_1 = list(map(lambda x: x / 2, sales_1))
summ_1 += sum(sales_1)

data = data[::-1]

sales_2 = [i for i in data[:(len(data) // 4)]]
summ_2 = sum(data) - sum(sales_2)
sales_2 = list(map(lambda x: x / 2, sales_2))
summ_2 += sum(sales_2)

print(summ_1, summ_2)
