nadpis = """
___  ___          _           ___  ____           _ 
|  \/  |         | |          |  \/  (_)         | |
| .  . | __ _ ___| |_ ___ _ __| .  . |_ _ __   __| |
| |\/| |/ _` / __| __/ _ \ '__| |\/| | | '_ \ / _` |
| |  | | (_| \__ \ ||  __/ |  | |  | | | | | | (_| |
\_|  |_/\__,_|___/\__\___|_|  \_|  |_/_|_| |_|\__,_|

"""
print(nadpis)                                                  

jmeno = input("Zadej jmeno hrace: ")
print("\n")
print("Oukej", jmeno)
print("Pravidla jsou nasledovne\nJa si myslim cislo a ty budes hadat Kdyz budes chtit skoncit, napis 'KONEC'\nNa konci hry uvidis svoje skore")
print("\n")
print("Myslim si cislo...")
import random
random_number = random.randint(1,10)
guess = -1
while guess != random_number:
    guess = int(input("Tvuj typ?: "))
    if guess == random_number:
        print("Správne")
    else:
        print("Nesprávně")
sirka = 4
cela_sirka = int(sirka*4)
print("+{0:-^{cela_sirka}}+".format("Tvoje skore", cela_sirka = cela_sirka))
print("|{0:^{sirka}}".format("Spravne",sirka=sirka + 2), "|{0:^{sirka}}|".format(random_number == guess, sirka=sirka + 2))
print("|{0:^{sirka}}".format("Spatne",sirka=sirka), "|{0:^{sirka}}|".format(random_number, sirka=sirka))
print("|{0:^{sirka}}".format("Celkem",sirka=sirka), "|{0:^{sirka}}|".format(guess + 1, sirka=sirka))
print("+{0:=^{cela_sirka}}+".format("=", cela_sirka = cela_sirka))