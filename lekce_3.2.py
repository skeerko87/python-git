"""
Lekce c. 3, druhy projekt - Skolni rozvrh
-------------------------------------------------------------------------------
SKUP_1 = ['Adam','Chelsea','Marcus','Oliver','Alex','Sandra','Ann',
          'Ron', 'Hermiona]
SKUP_2 = ['Marcus','Alex','Glenn','Samuel', 'Hermiona', 'Clara','Chelsea']
SKUP_3 = ['Hermiona', 'Adam','Tyler', 'Alex','Clara']
SKUP_4 = ['Abraham','Marcus', 'Hermiona', 'Alex','Glenn','Clara']
SKUP_5 = ['Alfred', 'Curt','Oliver','Tyler', 'Hermiona', 'Ann']
PREDMETY = ['Premenovani', 'Astronomie', 'Obrana_proti_cerne_magii',
        'Bylinkarstvi', 'Lektvary']
-------------------------------------------------------------------------------
"""
from pprint import pprint as pp

# Prázdný slovník "ROZVRH"
ROZVRH = {}

PREDMETY = ('Premenovani', 'Astronomie', 'Obrana_proti_cerne_magii',
        'Bylinkarstvi', 'Lektvary')

# Vytvorime klice z PREDMETY
ROZVRH[PREDMETY[0]] = None
ROZVRH[PREDMETY[1]] = None
ROZVRH[PREDMETY[2]] = None
ROZVRH[PREDMETY[3]] = None
ROZVRH[PREDMETY[4]] = None

# pp(ROZVRH)

# Definujeme jednotlive studijni skupiny
SKUP_1 = ['Adam','Chelsea','Marcus','Oliver','Alex','Sandra','Ann',
          'Ron', 'Hermiona']
SKUP_2 = ['Marcus','Alex','Glenn','Samuel', 'Hermiona', 'Clara','Chelsea']
SKUP_3 = ['Hermiona', 'Adam','Tyler', 'Alex','Clara']
SKUP_4 = ['Abraham','Marcus', 'Hermiona', 'Alex','Glenn','Clara']
SKUP_5 = ['Alfred', 'Curt','Oliver','Tyler', 'Hermiona', 'Ann']

# Vlozime sety podle predmetu jako hodnoty
ROZVRH.update(Prejmenovani = SKUP_1)
ROZVRH.update(Astronomie = SKUP_2)
ROZVRH.update(Obrana_proti_cerne_magii = SKUP_3)
ROZVRH.update(Bylinkarstvi = SKUP_4)
ROZVRH.update(Lektvary = SKUP_5)

# Vytvorime sety z "prejmenovani" a "astronomie"
prem_s = set(ROZVRH['Prejmenovani'])
astr_s = set(ROZVRH['Astronomie'])

pp(prem_s)
pp(astr_s)

# přidat
prem_s.add('Harry')

# odebrat
prem_s.discard('Samuel')

pp(prem_s)
pp(astr_s)

# zapiseme prunik všech setu
print()
print('Kdo se ucastni vsech predmetu')
pp(
    prem_s &
    astr_s &
    set(ROZVRH['Obrana_proti_cerne_magii']) &
    set(ROZVRH['Bylinkarstvi']) &
    set(ROZVRH['Lektvary'])
    )

