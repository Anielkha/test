# def greet_user(name):
#     print(f"Ahoj {name}")
# def sum_two_number(a, b):
#     result = a + b
#     result = result +5 
#     return result
# greet_user("Jirko")
# greet_user("Míšo")
# print(sum_two_number(3,4))

# def centimetry_na_palec(centimetry):
#     result = centimetry * 2.54
#     return result
# print(centimetry_na_palec((5)))

# def palce_na_centimetry(palce):
#     result = palce / 2.54
#     return result
# print(palce_na_centimetry((5)))

# def mult(a,b):
#     result = a*b
#     return result
# print(mult(3,4))

# slovo = input()
# def zadej_slovo(slovo):
#     result = 8* '*' + slovo + 8* '*'
#     return result
# print(zadej_slovo(slovo))

item = {"title": "Čajová konvička s hrnky", "price": 899, "in_stock": True}
print(item["title"])

print(f"Vybraný předmět je {item['title']} a stojí {item['price']} Kč.")

item = {"title": "Čajová konvička s hrnky", "price": 899, "in_stock": True}
# Název předmětu je Čajová konvička s hrnky
# Funguje ve verzi 3.12
print(f"Název předmětu je {item["title"]}")
# Funguje od verze 3.6
print(f"Název předmětu je {item['title']}")
item["weight"] = 0.8
key = "price"
item[key] = 929
# Má item klíč weight?
if "weight" in item:
    print(item["weight"])
else:
    print("Hmotnost není udána")