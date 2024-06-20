# Python zapoznaje się tylko z definicją funkcji przed jej wywołaniem, bo inaczej zauważyłby błąd.
def fun():
    print("*" - 15.1)

# fun() # Error


# W Pythonie tę samą nazwę funkcji można definiować wiele razy, np:
def f():
    print("1")


def f():
    print("2")


def f():
    print("3")


f()     # zostanie wywołana tylko ostatnia funkcja


# Kasowanie funkcji
del f
# f() # Error


"""
# definiowanie funkcji
def nazwa_funkcji(parametry_formalne):
    ciało funkcji
    # opcjonalnie instrukcja zwracająca wynik wraz z opcjonalnym obiektem:
    return obiekt

# wywołanie funkcji
nazwa_funkcji(parametry_aktualne)
"""


# Funkcje jako obiekty. Aliasy funkcji
pisz = print; czytaj = input
imie = czytaj('Jak masz na imię?')
pisz('Witaj', imie)


# Funkcje z nieznaną liczbą parametrów
def suma(*arg):
    s = 0
    for x in arg:
        s += x
    return s


print(suma(1, 2, 3, 8))


# Funkcje z nieznaną liczbą parametrów nazwanych
def zrzutka(**kwarg):
    s = 0
    for x, y in kwarg.items():
        print(f"{x} wpłacił {y}")
        s += y
    print("Razem mamy:", s)


zrzutka(Heniek=30, Wojtek=18, Edgar=6, Bambur=48)


# Rozpakowywanie parametrów z listy
l = [1, 10, 2]
# range(l)  # Error
print(list(range(*l)))  # rozpakowanie listy


# Rozpakowywanie parametrów ze słownika
def powiel(**kwarg):
    w = ""
    for s, n in kwarg.items():
        w += n * s
    return w


d = {'A':5, 'B':3, 'C':4}; print(powiel(**d))  # AAAAABBBCCCC


# Wiele wartości w rezultacie funkcji
def rozbicie(x): return int(x), x % 1  # zwraca dwie wartości (krotkę): część całkowitą i część dziesiętną liczby x.


# Zmienne lokalne. Przesłanianie zmiennych globalnych
def zwieksz(x):
    x += 1


x = 5
zwieksz(x)
print(x)


# Zmienne globalne
def rejestruj(wpis):
    global dziennik
    dziennik += [wpis]


dziennik = []
rejestruj(3)
rejestruj(4)
rejestruj(5)
print(str(dziennik)[1:-1])  # Wyświetli: 3, 4, 5


# Funkcje zagnieżdżone
"""
Funkcji zagnieżdżonych używamy np. wtedy,
gdy chcemy uniemożliwić wywoływanie pewnych funkcji poza określonym miejscem programu.

Funkcja zagnieżdżona ma dostęp do zmiennych lokalnych funkcji-matki (ale tylko do odczytu),
natomiast funkcja-matka nie ma dostępu do zmiennych lokalnych funkcji zagnieżdżonej.
"""
def stara_data(d):
    def miesiac():
        # d = d[1] + "a"  # to się nie powiedzie
        # d = d.split('-')  # to się nie powiedzie
        print(d[1] + "a")  # to już tak
        # print(d.split('-'))  # to też się nie powiedzie, bo najpierw w 127 jest zamiana d na listę, a potem jest wywoływany miesiac()
        return ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII'][int(d[1])-1]
    d = d.split('-')
    return d[2]+'.'+miesiac()+'.'+d[0]


print(stara_data('2019-11-24'))
# print(miesiac())  # Funkcja zagnieżdżona może być wywoływana jedynie wewnątrz ciała funkcji, w której ją zdefiniowano.


# Domknięcia. Zastosowania funkcji zagnieżdżonych.
# możemy użyć słowa nonlocal, by zezwolić funkcji zagnieżdżonej na modyfikowanie (a nie tylko czytanie) funkcji-matki,
# funkcja-matka może jako swój rezultat zwrócić funkcję zagnieżdżoną, pozwalając na jej wywołanie spoza funkcji-matki.
# W rezultacie możemy tworzyć domknięcia, które można opisać jako funkcje pamiętające swój stan.
# Poniżej wykorzystano ten mechanizm do bardziej eleganckiej implementacji rejestru:
def rejestr():
    dziennik = []

    def rejestruj(*wpis):
        nonlocal dziennik
        dziennik += wpis  # list += is equivalent to list.extend(), see: https://stackoverflow.com/questions/13332987/list-tuple-vs-list-list-tuple
        return str(dziennik)[1:-1]

    return rejestruj

# Tutaj globalnej przestrzeni nazw nie zaśmieca zmienna rejestr,
# nie musimy też jej ręcznie inicjalizować - robi to funkcja rejestr,
# która w swoim rezultacie zwraca funkcję rejestruj służącą do dodawania kolejnych elementów i odczytywania
# aktualnego stanu rejestru.


r = rejestr()
r(3, 4)
print(r(5))


# Silnia jako przykład funkcji rekurencyjnej
def silnia(n):
    if n > 1:
        return n * silnia(n - 1)
    else:
        return 1


print(silnia(5))


# Przekształcanie iteracji w rekursję
# Każda funkcja oparta na iteracji (pętlach), może zostać przedstawiona w postaci rekurencyjnej, np. suma:
def suma(*n):
    if n:
        return n[0] + suma(*list(n)[1:])
    else:
        return 0


print(suma(1, 7, 8))


# Nieefektywność funkcji rekurencyjnych
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1)+fib(n - 2)

# fib(50)  # długi czas czekania na wynik (gdy się już znudzimy, wciskamy kombinację CTRL+C).


# Przekształcanie rekursji w iterację
# Każdą funkcję rekurencyjną da się przekształcić do postaci opartej na pętlach (iteracyjnej).
# W przypadku ciągu Fibonacciego będzie to:
def fib(n):
    """Fib bez rekurencji"""
    if n < 2: return n
    a, b = 0, 1
    for x in range(1, n):
        a, b = b, a + b
    return b


print(fib(5000))

# Wyrażenia lambda
# Python pozwala tworzyć funkcje także w inny sposób niż z wykorzystaniem standardowej definicji,
# a mianowicie z wykorzystaniem wyrażenia lambda. Wyrażenie to ma postać lambda argumenty:
# wyrażenie, a jego rezultatem jest anonimowa funkcja (którą można od razu wykonać, przekazać jako parametr,
# lub zapamiętać w zmiennej – tym samym nadając jej nazwę).

# Najczęściej korzysta się z wyrażeń lambda do:

# tworzenia jednorazowych funkcji przekazywanych jako parametry do innych funkcji,
# np. w poniższym przykładzie do posortowania osób według ich nazwisk:
ludzie = ["Jan Kot", "Adam Sowa", "Piotr Mucha", "Wacław Kret", "Iwo Kruk"]
ludzie.sort(key = lambda x: x.split()[1])
print(ludzie)  # ['Jan Kot', 'Wacław Kret', 'Iwo Kruk', 'Piotr Mucha', 'Adam Sowa']

# tworzenia funkcji reprezentujących wyrażenia matematyczne, np.:
delta = lambda a, b, c: b ** 2 - 4 * a * c
print(delta(2, 4, 2), delta(2, 0, -2))


# Operator warunkowy
# Wyrażenie lambda jest pojedynczym wyrażeniem, nie ciągiem instrukcji, jak ciało funkcji.
# Dlatego niedozwolone są w nim instrukcje warunkowe i pętle. Z pomocą przychodzi tu operator warunkowy, mający postać:

# wartość_gdy_spełniony if warunek else wartość_gdy_niespełniony

# Pozwala on zastąpić instrukcję warunkową wyrażeniem, na przykład:

pt = lambda x: "Pani " + x if x[-1] == 'a' else "Pan " + x
print(pt("Kowalska"))  # 'Pani Kowalska'
print(pt("Kowalski"))  # 'Pan Kowalski'


# Listy funkcji i zagnieżdżone wyrażenia lambda
# Wyrażenie lambda może zwracać inne wyrażenie lambda.
# Przykładowy kod poniżej tworzy listę, której kolejne elementy są funkcjami
# przemnażającymi argument o kolejną liczbę naturalną.
lf = []
mx = lambda i: (lambda x: x * i)
for i in range(10):
    lf += [mx(i)]
print(lf[1](5), lf[2](5), lf[3](5))  # 5, 10, 15

