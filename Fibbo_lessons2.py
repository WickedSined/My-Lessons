# Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.

total = 0
fibo_list = [ 0, 1 ]
limit = 4 * 10 ** 6


while True:
    _tmp = fibo_list[len(fibo_list) - 1] + fibo_list[len(fibo_list) - 2] 
    
    if  _tmp > limit:
            break

    if _tmp % 2 == 0:
        total += _tmp 

    fibo_list.append(_tmp)

print(total)
print("\n","Список чисел Фиббоначи:", fibo_list)