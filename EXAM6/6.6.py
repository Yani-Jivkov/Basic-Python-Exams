from math import floor
a1 = int(input())
a2 = int(input())
n = int(input())

for s1 in range(a1 + 1, a2):
    symbol1 = chr(s1)
    for s2 in range(0, n - 1):
        symbol2 = s2
        n = floor(n / 2)
        for s3 in range(1, n - 1):
            symbol3 = s3
            for s4 in range(a1, a2):
                symbol4 = s4
                print(f'{s1}-{s2}{s3}{s4}')