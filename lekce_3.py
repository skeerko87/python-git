CISLO = 12688

# Pokud vstup neni číslo, ukončit!
if str(CISLO).isalpha():
    print('Vstupní hodnoty není číslo!')
    exit()
else:
    # 12 x 468
    delka = len(str(CISLO))
    del_bod = delka // 2

    prvni_p = str(CISLO)[:del_bod]
    druha_p = str(CISLO)[del_bod:]

    prvni_p, druha_p = int(prvni_p), int(druha_p)

    # Obě části jsou sudé
    if prvni_p % 2 == 0 and druha_p % 2 == 0:
        print('První část i druhá část jsou SUDÉ')
    elif prvni_p % 2 == 0:
        print('První část je sudá')
    elif druha_p % 2 == 0:
        print('Druha část je lichá')
    else:
        print('Ani jedna cast neni suda')







