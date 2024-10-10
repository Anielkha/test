import math
import statistics



prumer = statistics.mean([2, 3, 4, 5])
print(prumer)
#Napište program, který dostane na vstupu desetinné číslo a na výstup napíše toto číslo zaokrouhlené nejdříve nahoru, potom dolů a potom běžným Pythonovským zaokrouhlováním.

#zaokrouhledni nahoru
vysledek = math.ceil(3.1)
print(vysledek)
#zaokrouhledni dolu
vysledek1 = math.floor(3.9)
print(vysledek1)

vysledek3 = round(3,7)
print(vysledek3)

votes = [
    "curling", 
    "vánoční svařák na trzích", 
    "vánoční svařák na trzích", 
    "curling", 
    "zážitková první pomoc",
    "curling", 
    "zážitková první pomoc",
    "curling",
    "zážitková první pomoc",
    ]
#vysledek4 = statistics.mode(votes)
#print(vysledek4)
print(statistics.mode(votes))

school_report = [
    ["Český jazyk", 1],
    ["Anglický jazyk", 1],
    ["Matematika", 1],
    ["Přírodopis", 2],
    ["Dějepis", 1],
    ["Fyzika", 2],
    ["Hudební výchova", 4],
    ["Výtvarná výchova", 2],
    ["Tělesná výchova", 3],
    ["Chemie", 4],
]
znamky = []
dulezite_predmety = ["Český jazyk", "Anglický jazyk", "Matematika", "Fyzika"]
for zaznam in school_report:
    #Při prvním běhu
    #zaznam = ["Cesky jazyk, 1"]
    #chci uložit jen dulelezite predmety v seznamu dulezite_predmety
    #podivej se jestli je predmet v zaznam vu v seznamu dulezite_predmety
    if zaznam[0] in dulezite_predmety:
        #zaznam[0] = Cesky jazyk
        #zaznam[1] = 1
        znamky.append(zaznam[1]) #ukazujeme pozici ze ktere chceme ulozit do znamek (tedy v tomto případě známka je v school_report na pozici 1)
print(znamky)
prumer_school = statistics.mean(znamky)
print(prumer_school)