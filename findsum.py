number_sum = int(input("Введите число :"))
number_list = [4,1,1,4,5,6,7,8,9,10]
lenght_list = int(len(number_list))
result_list = []

for i in range(lenght_list):
    for x in range(i+1,lenght_list):
        if number_list[i] + number_list[x] == number_sum:
            result_list.append(number_list[i])
            result_list.append(number_list[x])
        
if len(result_list) == 0:        
    print('В списке отсутствуют числа удовлетворяющие условию')
else:     
    print(result_list)