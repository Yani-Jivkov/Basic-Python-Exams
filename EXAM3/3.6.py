first_number = input()
second_number = input()
counter = first_number

for i in range(int(first_number), int(second_number) + 1):
    counter = int(counter) + 1
    if int(counter[0]) % 2 != 0 and int(counter[1]) % 2 != 0 and int(counter[2]) % 2 != 0 and int(counter[3]) % 2 != 0:
        print(f'{counter}', end='')