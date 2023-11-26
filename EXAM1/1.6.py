k = int(input())
l = int(input())
m = int(input())
n = int(input())

counter = 0
counter_hit = False

for first in range(k, 9):
    for second in range(9, l - 1, -1):
        for third in range(m, 9):
            for fourth in range(9, n - 1, -1):

                if first % 2 == 0 and second % 2 != 0 and third % 2 == 0 and fourth % 2 != 0:
                    first_num = f'{first}{second}'
                    second_num = f'{third}{fourth}'

                    if counter == 6:
                        counter_hit = True
                        break
                    elif first_num == second_num:
                        print("Cannot change the same player.")
                    else:
                        print(f"{first}{second} - {third}{fourth}")
                        counter += 1

    if counter_hit:
        break