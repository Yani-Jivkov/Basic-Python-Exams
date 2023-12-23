n = int(input())
two_0 = 0
tree_0 = 0
four_0 = 0

for i in range(n):
    number = int(input())

    if number % 2 == 0:
        two_0 += 1

    if number % 3 == 0:
        tree_0 += 1

    if number % 4 == 0:
        four_0 += 1

percent_1 = (two_0 / n) * 100
percent_2 = (tree_0 / n) * 100
percent_3 = (four_0 / n) * 100

print(f'{percent_1:.2f}%')
print(f'{percent_2:.2f}%')
print(f'{percent_3:.2f}%')