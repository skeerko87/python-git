# """
# Lekce c. 3, prvni projekt
# Zadane slovniky:
# ------------------------------------------------------------------------------
# film = {
# 'Jmeno': 'Shawshank Redemption',
# 'Hodnoceni': 87,
# 'Rok': 1994,
# 'Reziser': 'Frank Darabont',
# 'Hraji': ['Tim Robbins', 'Morgan Freeman']
# }
# film2 = {
# 'Jmeno': 'The Godfather',
# 'Hodnoceni': 92,
# 'Rok': 1972,
# 'Reziser': 'Francis Ford Coppola',
# 'Hraji': ['Al Pacino', 'Marlon Brando']
# }
# film3 = {
# 'Jmeno': 'The Dark Knight',
# 'Hodnoceni': 90,
# 'Rok': 2008,
# 'Reziser': 'Christopher Nolan',
# 'Hraji': ['Christian Bale', 'Heath Ledger']
# }
# ------------------------------------------------------------------------------
# """

from pprint import pprint as pp

# Prázdný slovník
film_1 = {}

# Vložíme klíče slovníku
film_1['Jmeno'] = None
film_1['Hodnoceni'] = None
film_1['Rok'] = None
film_1['Reziser'] = None

film_1['Jmeno'] = 'Shawshank Redemption'
film_1.update(Hodnoceni = 87)

rok = input('Rok uvedení: ')
reziser = input('Jméno režiséra: ')

film_1['Rok'] = rok
film_1['Reziser'] = reziser

film_1['Rozpocet'] = 1900000
film_1['Hraji'] = ['Tim Robbins', 'Morgan Freeman']

# pp(film_1)
# Odstranení hodnoty
del film_1['Rozpocet']
film_1.pop('Hraji')

# pp(film_1)

film_db = {}

film_2 = {
'Jmeno': 'The Godfather',
'Hodnoceni': 92,
'Rok': 1972,
'Reziser': 'Francis Ford Coppola',
'Hraji': ['Al Pacino', 'Marlon Brando']
}
film_3 = {
'Jmeno': 'The Dark Knight',
'Hodnoceni': 90,
'Rok': 2008,
'Reziser': 'Christopher Nolan',
'Hraji': ['Christian Bale', 'Heath Ledger']
}

# Vkladat jednotlive slovniku
film_db[film_1['Jmeno']] = film_1
film_db[film_2['Jmeno']] = film_2
film_db[film_3['Jmeno']] = film_3

# pp(film_db)

print()
print("Vitejte v nasi skromne filmove databazi")
print("Mame v nabidce tyto snimky: ")
print('1.', film_db['Shawshank Redemption']['Jmeno'], '-',
    film_db['Shawshank Redemption']['Rok'])
print('2.', film_db['The Godfather']['Jmeno'], '-',
    film_db['The Godfather']['Rok'])
print('3.', film_db['The Dark Knight']['Jmeno'], '-',
    film_db['The Dark Knight']['Rok'])

# Dotazy uživatele
print()
dotaz_1 = input('Jméno filmu: ')
dotaz_2 = input('Výběr kategorie: ')

pp(film_db.get(dotaz_1, 'Neexistující film') .get(dotaz_2, 'Nic'))






