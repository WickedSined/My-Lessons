import math

# объявляем функцию конструкор римских символов:["I","V","X"]
def decoding(x,digree):
    build_str=""
    if digree==1:
        build_str = constructor(x,["I","V","X"])
        
            # return str_build

    elif digree==2:
        build_str = constructor(x,["X","L","C"])
            # return str_build
            
    elif digree==3:
        build_str = constructor(x,["C","D","M"])
            # return str_build
            
    elif digree==4:
        build_str = constructor(x,["M","**","&&"])
    
    return build_str

def constructor(number,rome):
    
    if number < 4:
        return rome[0]*number
    
    elif number == 4:
        return str(rome[0])+str(rome[1])
        
    elif number == 5:
        return str(rome[1])
            
    elif number < 9:
        # str_build=str(rome[2])+str((rome[1]) * number)
        return str(rome[2])+str((rome[1]) * number)
    
    elif number == 9:
        return str(rome[0])+str((rome[2]))

num=int((input("Введите число от 1 до 4000:")))

# определяем разрядность введенного числа:
digree=math.floor(math.log10(int(num)))+1
print("Разрядность числа: "+str(digree))

# spisok_num=[i for i in num]    #! Надо изучить "Списковые включения В Python"
# print(spisok_num)              #! Надо изучить "Списковые включения В Python" лучше чем While ниже 

# Создаем список из разрядов числа: range(digree,0,-1):
x=0
str_build = ""
for i in range(1,digree+1):
      x=num%10
      str_build += decoding(x, i)
      num=num//10
      print("Число в разряде    "+str(x))
      print("i=    "+str(i))
      print("Степень  "+str(digree))
# while num>0:
#     dec=num%10
#     spisok_digits.insert(0,dec)
#     num=num//10

#  Создаем цикл для отработки каждого элемента списка в функции Конструктор


print("Представление введенного числа списком: "+str(str_build))
# decoding(digree,spisok_digits)
















# result1=num%10
# result2=(num//10)%10
# result3=(num//10**2)%10
# result4=(num//10**3)%10
# ! Формула определения разрядности числа

# print(spisok_digstsree)
# result6=num//10
# print(result6)