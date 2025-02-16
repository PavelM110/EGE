with open('17.txt') as file:
    data = [int(i) for i in file if i]

max_50 = max(i for i in data if abs(i) % 100 == 50)

ans = []

for i in range(len(data) - 2):
    nums = data[i:i+3]
    ul1 = len(nums) == len(set(nums))
    a, b, c  = nums
    ua1 = 10000 <= abs(a) <= 99999
    ub1 = 10000 <= abs(b) <= 99999
    uc1 = 10000 <= abs(c) <= 99999
    u1 = all((ua1, ub1, uc1, ul1))
    u2 = sum(nums) <= max_50
    if u1 and u2: ans.append(sum(nums))

print(len(ans), max(ans))