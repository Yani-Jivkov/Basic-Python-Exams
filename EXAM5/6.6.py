name = ''
high_score = 0
high_score_name = ''

while True:
    name = input()
    score = 0

    if name == 'Stop':
        break

    for i in range(len(name)):
        number = int(input())
        if chr(number) == name[i]:
            score += 10
        else:
            score += 2

        if high_score <= score and k == 2:
            high_score = score
            high_score_name = name

print(f'The winner is {high_score_name} with {high_score} points!')
