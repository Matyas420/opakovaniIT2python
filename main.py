import random

# Číslo 1. Proměna pro jméno
jmeno = "Matyáš"

# Číslo 2. Proměna pro přijmení
prijmeni = "Polednik"

# Číslo 3. Výpis proměnných do konzole
print(jmeno + " " + prijmeni)

# Číslo 4. Zadání věku 
vek = int(input("Zadejte svůj věk: "))

# Číslo 5. Výpis délek první a druhé proměné
print(len(jmeno))
print(len(prijmeni))

# Číslo 6. Uložení hodnotu 6 do proměnné
cislo = 6 

# Číslo 7. Cyklus se opakuje dokud není roven 5 do té doby se do proměné "cislo" bude ukládat hodnota 3
for i in range(1,6):
    cislo += 3
    
# Číslo 8. Výsledná hodnota se po pěti cyklech vypíše
print(cislo)

# Číslo 9. Uživatel zadá věk a isdigit zkontroluje zda je věk číslice potom program vypíše "Děkuji" a když ne tak else
vek = input("Zadejte věk: ")
if vek.isdigit():
    print("Děkuji")
else:
    print("Zadej jen celočíselnou hodnotu.")

# Číslo 10. Program vygeneruje náhodné číslo z listu "cisla" a pak ji uloží do proměnné "hodnota"
cisla = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
hodnota = random.choice(cisla)
print(hodnota)

# Bonus k číslu 4 a 9 
# Číslo 4. Program se opakuje dokud uživatel nezadá svůj věk
while True:
    vek = input("Zadejte svůj věk: ")
    if vek.isdigit():
         break

# Číslo 9. Program se opakuje dokud uživatel nezadá svůj věk
while True:
    vek = input("Zadejte věk: ")
    if vek.isdigit():
        print("Děkuji")
        break
    else:
        print("Zadej jen celočíselnou hodnotu.")
    
