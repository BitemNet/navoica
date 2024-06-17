"""
Is range a generator?
Here is answer: https://treyhunner.com/2018/02/python-range-is-not-an-iterator/
"...And unlike iterators, you can ask them whether they contain things without changing their state:...
>>> numbers = range(1_000_000)
>>> squares = (n**2 for n in numbers)

>>> 0 in numbers
True
>>> 0 in numbers
True
>>> 0 in squares
True
>>> 0 in squares
False
"
"""


r = range(1, 4)
for i in r:
    for j in r:
        for k in r:
            # print(i, j, k, r)
            print(i * j * k, end=";")
        print(end=" ")
    print()
