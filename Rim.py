import math

def decoding(N, pow):
    letters = {
        '1000': 'M', 
        '4000': 'MU', 
        '5000': 'V'
    }
    print(N*10**(pow - 1))



number = input("Enter number 1000 - 9999: ")

try: 
    number = int(number)
except: 
    print("Data isn't valid")
    exit()

if (number < 0):
   print("Data isn't valid")
   exit() 


"""
M - 1000 - 3000
MU - 4000
U - V - 5000


XXXX

"""
pow = (math.floor(math.log10(number) + 1))
decimal = number // 10**(pow - 1)


decoding(decimal, pow)

if number>=1000 and number<=3000:
    print("M")
elif number>3000 and number<5000:
    print("MU")
elif number>4999:
    print("UV")

    

 