from functools import reduce

prod_numb = reduce(lambda accum, i: accum * i, range(100, 1001))
print(prod_numb)
