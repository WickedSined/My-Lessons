import math


def build(number, str_build):
    if number < 4: 
        return str_build[0] * number
    elif number == 4:
        return str(str_build[0]) + str(str_build[1])
    elif number == 5: 
        return str_build[1]
    elif number < 9: 
        return str_build[1] + str(str_build[0]) * (number - 5)
    elif number == 9: 
        return str(str_build[0]) + str_build[2]

def decoding(number, pow):
    if pow == 1: 
        build_str = build(number, ["I", "V", "X"])
    elif pow == 2: 
        build_str = build(number, ["X", "L", "C"])
    elif pow == 3:
        build_str = build(number, ["C", "D", "M"])
    elif pow == 4: 
        build_str = build(number, ["M", "U", "Y"])
        
    return build_str
 
number = input("Enter number: ")

try: 
    number = int(number)
except: 
    print("Data isn't valid")
    exit()

if (number < 0):
   print("Data isn't valid")
   exit() 

pow = (math.floor(math.log10(number) + 1))
str_build = ""

for i in range(pow, 0, -1): 
    
    decimal = number // 10**(i - 1)
    str_build += decoding(decimal, i)

    number -= decimal * 10**(i - 1) 
    
print(str_build)