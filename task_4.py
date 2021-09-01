a_list = [2, 2, 50, 83, 56, 56, 5, 37, 45, 80, 104, 122, 104]

result = [x for x in a_list if a_list.count(x) == 1]
print(result)

