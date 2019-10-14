#!/usr/bin/env python3
""" Lekce #1 - Uvod do programovani, 1/2 Destinatio """

# I. KROK: 
# Definujeme konstanty, se kterymi chceme pracovat
# Debatovat nad optimalnim datovym typem pro nase data
SEZNAM_MEST = ('Praha', 'Viden','Brno', 'Svitavy', 'Zlin', 'Ostrava')
SEZNAM_CEN = (1000, 1100, 2000, 1500, 2300, 3400)
SEZNAM_SLEV = ('Svitavy', 'Ostrava')
ODDELOVAC = '=' * 35

# II. KROK:
# Pozdravime uzivatele a doplnime oddelovace '='
# Zobrazit uzivateli nasi nabidkou - lokalita | cena
print(ODDELOVAC)
print('Vitejte u nasi aplikace Destinatio!')
print(ODDELOVAC)
print(
'''
1 - Praha   | 1000
2 - Viden   | 1100
3 - Brno    | 2000
4 - Svitavy | 1500
5 - Zlin    | 2300
6 - Ostrava | 3400
''')
print(ODDELOVAC)

# III. KROK:
# Vyzadame si od uzivatele jednotlive vstupy
# cislo destinace, jmeno, prijmeni, vek, email, heslo
vyber = int(input('Vyberte cislo lokality: '))

if not 0 < vyber <= len(SEZNAM_MEST):
    print('Toto číslo není v nabídce!')
    exit()
else: # ---> pokud mam vyber = 1 - 6
    destinace = SEZNAM_MEST[vyber - 1]  # --> destiance[0] pokud bude vyber = 1
    cena = SEZNAM_CEN[vyber - 1]

    if destinace in SEZNAM_SLEV:
        cena = cena * 0.75
    else:
        cena = cena

jmeno = input('JMENO: ')
prijmeni = input('PRIJMENI: ')
vek = int(input('VEK: '))
email = input('EMAIL: ')
heslo = input('HESLO: ')
print(ODDELOVAC)

# Podminka pro ověření věku uživatele
if vek < 15:
    print('Jste moc mladý, nemůžete pokračovat!')

elif '@' not in email:
    print('Zadaný mail není platný!')
# délka hesla minimálně 8 znaků
# heslo obsahuje jak cisla tak text
# prvni a posledni symbol nesmi byt cislo
elif (
    len(heslo) < 8 or
    heslo.isalpha() or
    heslo.isnumeric() or
    heslo[0].isnumeric() or
    heslo[-1].isnumeric()
    ):
    print('''
    Spatne heslo!
    1. délka hesla minimálně 8 znaků
    2. heslo obsahuje jak cisla tak text
    3. prvni a posledni symbol nesmi byt cislo
    ''')

else:
    print('Dekuji ' + jmeno)
    print('Vybrali jste si destinaci ' + destinace)
    print('Cena za dopravu do ' + destinace + ' je ' + str(cena))
    print(f'Listek posleme na Vas email ({email})')
