prodej_knih = [
    ["Praha", 4200, 4900],
    ["Brno", 2500, 2100],
    ["Ostrava", 1500, 1100],
    ["Plzeň", 1000, 700],
    ["Liberec", 700, 500],
    ["Olomouc", 400, 300]
]

# for radek in prodej_knih:
#     if radek [1] > radek [2]:
#         pocet = pocet + 1
#         print(pocet)

seznam = []
print(seznam)
seznam.append("první")
print(seznam)
seznam.append("druhá")
print(seznam)

mesta_pokles = []
for radek in prodej_knih:
    if radek [1] > radek [2]:  
        mesta_pokles.append(radek[0])
print(mesta_pokles)

prodej_knih = [
    ["Praha", 4200, 4900],
    ["Brno", 2500, 2100],
    ["Ostrava", 1500, 1100],
    ["Plzeň", 1000, 700],
    ["Liberec", 700, 500],
    ["Olomouc", 300, 300]
]
mesta_pokles = []
mesta_rust = []
mesta_beze_zmeny = []
for radek in prodej_knih:
    if radek[1] > radek[2]:
        mesta_pokles.append(radek[0])
    elif radek[1] == radek[2]:
        mesta_beze_zmeny.append(radek[0])
    else:
        mesta_rust.append(radek[0])
print(mesta_pokles)
print(mesta_beze_zmeny)
print(mesta_rust)

def month_of_birth(birth_number):
    month = int(birth_number[2:4]) % 50
    return month


Olga = "9562125899"

mesic_olga = month_of_birth(Olga)
print(mesic_olga)

# Definice funkce
def month_of_birth(birth_number):
    # Potřebujeme zjistit month = v řetězci na pozici 2 a 3
    # Začínáme indexem 2
    # Končíme PŘED indexem 4
    month = int(birth_number[2:4]) % 50
    return month

olga = "9555125899"
mesic_olga = month_of_birth(olga)
print(mesic_olga)
pavel = "9207054439"
mesic_pavel = month_of_birth(pavel)
print(mesic_pavel)

import random
def ruleta(sazka_rada,sazka_penize):
    cislo = random.randint(0, 36)
    zbytek = cislo % 3
    vyhra = 0
    if cislo == 0:
        vyhra = 0
    elif zbytek == 1 and sazka_rada == 1:
        vyhra = sazka_penize * 3
    elif zbytek == 1 and sazka_rada == 2:
        vyhra = sazka_penize * 3
    elif zbytek == 1 and sazka_rada == 3:
        vyhra = sazka_penize * 3
      
    return vyhra
print(ruleta(1,500))

import random
def ruleta(sazka_rada, sazka_penize):
    cislo = 0 #random.randint(0, 36)
    zbytek = cislo % 3
    vyhra = 0
    if zbytek == 1 and sazka_rada == 1:
        vyhra = sazka_penize * 3
    if zbytek == 2 and sazka_rada == 2:
        vyhra = sazka_penize * 3
    if zbytek == 0 and sazka_rada == 3:
        vyhra = sazka_penize * 3
    if cislo == 0:
        vyhra = 0
    return vyhra
print(ruleta(3, 500))