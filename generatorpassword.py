import random

uppercase_letters = "abcdefghijklmnoprqstuvwyz"

digits = "0123456789"

simbols= "(){}[]#+-*/\\?¿!¡"

upper, nums, syms = True, True, True

all = ""

if upper:
    all += uppercase_letters
if nums:
    all += digits
if syms:
    all += simbols

length = 20
amount = 10

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)

# es un generador de contraseñas simple 
# podrias modificarlo para tener la cantidad de caracteres que tendrian la contraseña y la cantidad de opciones que te podrian dar
