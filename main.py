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

# Číslo 7. Cyklus se opakuje dokud není roven 5 do té doby se do proměné bude ukládat hodnota 3
x = 0
cyklus = 0
while cyklus < 5:
    x += 3
    print(f"Opakování {cyklus+1}")
    
# Číslo 8. Výsledná hodnota po pěti cyklech vypíše
    cyklus += 1
    print(cyklus)

# Číslo 9. Podmínka pro uživatele ať zadá věk 1 a program odpoví "Děkuji"
vek = int(input("Zadejte věk 1: "))
if vek == 1:
    print("Děkuji")

# Číslo 9,5. Pokud uživatel zadá jinou celočíselnou hodnotu, vypíše mu to "Zadej jen celočíselnou hodnotu"
else:
    print("Zadej jen celočíselnou hodnotu.")

# Číslo 10. 
import random
cisla = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(random.choice(cisla))

# Bonus k číslu 4 a 9 
