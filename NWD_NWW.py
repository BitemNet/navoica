# 1. wprowadzanie liczb

print("Podaj dwie liczby naturalne:")
a = int(input("Pierwsza:"))
b = int(input("Druga:"))

# 2. ustalenie, która z liczb jest mniejsza

if a > b:
    w = a
    m = b
else:
    w = b
    m = a

# 3. pętla główna

r = w % m
while r:
    w = m
    m = r
    r = w % m

# 4. wyświetlenie rezultatów

print(f"NWD liczb {a} i {b} wynosi {m}, a ich NWW wynosi {a * b / m}")
