
my_list = [1, 5, 8, 34, 67, 3, 39, 125]
answer = []
for i in range(len(my_list)-1):
    if my_list[i] < my_list[i+1]:
        answer.append(my_list[i+1])

print(answer)

a = [1, 8, 3, 7, 16, 55]
b = (a(i) < a(i+1) for i in range(len(a)-1))

print(b)
