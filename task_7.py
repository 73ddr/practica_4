from math import factorial

def fact(n: int):
    for i  in range(1, n + 1):
        yield factorial(i)

num = input('введите количество n для вычисления факториала')

try:
     value = int(num)
except ValueError as a:
     print(a)
     exit(1)

for el in fact(value):
        print(el)
