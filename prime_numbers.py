# Przykład nested loops

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'równe', x, '*', int(n/x))
            break
        else:
            print(n, 'jest liczbą pierwszą')
