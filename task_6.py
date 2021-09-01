from itertools import count

for el in count(3):
    if el > 10:
        break
    else:
        print(el)


from itertools import cycle

a = 0
for el in cycle("123"):
    if a > 10:
        break
    print(el)
    a += 1








