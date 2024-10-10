
jmena = ["Michal", "Jana", "Martina"]
teploty = [23.3, 21.1, 10, 14, 2, 3]
print(jmena[1])
print(teploty[0:3])
print(teploty[2:])
print(len(teploty))

"""inzerat = "Na této pracovní pozici budete využívat Python a SQL"

if "SQL" in inzerat:
    print("SQL ano")
else:
    print("SQL ne")"""
"""
email = "martina.stouracova@czech.cz"

if "@" not in email:
    print("blbe")
else:
    print("dobre")
"""

"""
cisla = [1, 2, 3, 1, 2, 132, 123, 43, 55, 12, 2, 3, 4, 5, 12, 1435, 93]

print(min(cisla))
print(max(cisla))
print(sorted(cisla))
print(sum(cisla))"""
''''
pohyby = [1200, -250, -800, 540, 721, -613, -222]
print(pohyby[2])
print(pohyby[2:])
print(len(pohyby))
print(min(pohyby))
print(max(pohyby))
print(sum(pohyby))
s = [1, 2, 3, 4, 5]
print(sum(s)/len(s))
pr = [1, 2, 3, 4.5]
print(max(pr)-min(pr))
pr1 = [1, 2, 3, 4]
stred = int(len(pr1)/2) - 1
print(pr1[stred])

produkt = input("Zadej produkt: ")
produkt = produkt.lower() # VINO na vino

if produkt == "vino":
    print("vitej v kategorii vina")
elif produkt == "pivo":
    print("vitej v kategorii piva")
else:
    print("spatne zvolena hodnota")
jmeno = "Martina Stourac"
print(jmeno.upper())
print(jmeno.lower())

hodnoty = ['12', '1', '7', '-11']
cislo_tri = hodnoty[2]
vysledek = (int(cislo_tri)) + 4
hodnoty[2] = vysledek
print(hodnoty)
'''
'''jen_cisla = "10"
print(jen_cisla.isdecimal())'''