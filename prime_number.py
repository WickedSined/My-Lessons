number = int(input("Введите число для проверки: "))
s = 0

if number <= 1:
    print("Число не является простым")
    s = 1 
for i in range(2,int((number**0.5)+1)):
    if number % i == 0:
        s = 1
        print("Число не является простым")

        break
if s != 1:
    print("Число простое")    
