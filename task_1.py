def func_salary(var_1, var_2, var_3):
    salary = (var_1 * var_2) + var_3
    return salary

var_1 = int(input("Введите число обработанных часов:"))
var_2 = int(input("Введите сколько стоит 1 час работы:"))
var_3 = int(input("Введите размер возможной премии:"))
func_result = func_salary(var_1, var_2, var_3)

print(func_result)

