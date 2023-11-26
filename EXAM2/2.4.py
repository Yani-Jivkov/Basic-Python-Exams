N = int(input())
M = int(input())
S = int(input())
char = 0

for i in range(M, N - 1, -1):

    if i % 2 == 0 and i % 3 == 0:
        char = i

    if char == S:
        break
    elif i % 2 == 0 and i % 3 == 0:
        print(char, end=' ')

