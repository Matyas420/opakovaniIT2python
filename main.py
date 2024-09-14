import random

# Číslo 1. Proměna jméno
jmeno = "Matyas"

# Číslo 2. Proměna přijímení
prijmeni = "Polednik"

# Číslo 3. Výpis proměnných do konzole
print("jmeno" + " " + "prijmeni")

# Číslo 4. Zadání věku uživatele
vek = int(input("Zadejte svůj věk: "))

# Číslo 5. Výpis délek první a druhé proměné
print(len("jmeno" + "prijmeni"))

# Číslo 6. Uložení hodnotu 6 do proměné
cislo = 6 

# Číslo 7. Cyklus se opakuje dokud není roven 5 do té doby se do proměné x bude ukládat hodnota 3
x = 0
cyklus = 0
while cyklus < 5:
    x += 3
    
# Číslo 8. Výsledná hodnota se po pěti cyklech vypíše
    cyklus += 1
    print(x)

# Číslo 9. Uživatel zadá věk a isdigit zkontroluje zda je věk číslice tak program vypíše "Děkuji"
vek = input("Zadejte věk: ")
if vek.isdigit():
    print("Děkuji")
else:
    print("Zadej jen celočíselnou hodnotu.")

# Číslo 10. Program vygeneruje náhodnou hodnotu z listu "cisla" a pak ji zapíše
cisla = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(random.choice(cisla))

# Bonus k číslu 4 a 9 
# Číslo 4. Program se opakuje dokud uživatel nezadá svůj věk
while True:
    vek = input("Zadejte svůj věk: ")
    if vek.isdigit():
        break

# Číslo 9. 
while True:
    vek = input("Zadejte věk: ")
    if vek.isdigit():
        print("Děkuji")
        break
    else:
        print("Zadej jen celočíselnou hodnotu.")
