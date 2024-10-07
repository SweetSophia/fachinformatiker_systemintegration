import os
# Screen clearen
os.system('cls')

cola_basis = 2.50
cola_discount = 1.20
pepsi_basis = 2.20
pepsi_discount = 1.20
pommes_basis= 3.80
pommes_discount = 1.50
menue_disc = pommes_basis + pepsi_basis + pommes_basis - cola_discount - pepsi_discount -pommes_discount
us_best = ()

print("Das ist ein einfacher \\Satz")
print("Das ist ein \"einfacher\" Satz")
print("Das ist ein einfacher \n Satz")
print("Das ist ein ein\t einfacher Satz")
print()
print("/o---------------------o\\")
print("| Artikel  \t  Preis |")
print("|-----------------------|")
print(f"| Cola   \t| {cola_basis:.2f}€ |")
print(f"| Pepsi \t| {pepsi_basis:.2f}€ |")
print(f"| Pommes \t| {pommes_basis:.2f}€ |")
print(f"| Menü  \t| {pommes_basis + pepsi_basis + pommes_basis:.2f}€ |")
print("\\o---------------------o/")
print()
print("| Rabatte mit Treukarte:")
print("| ----------------------")
print(f"| Cola    \t| {cola_basis - cola_discount:.2f}  |")
print(f"| Pepsi   \t| {pepsi_basis - cola_discount:.2f}  |")
print(f"| Pommes  \t| {pommes_basis - pommes_discount:.2f}  |")
print(f"| Menü  \t| {menue_disc:.2f}€ |")
print()
print("/o---------------------o\\")
print("| Terminal Bestellung:")
print("| Was moechten Sie \t|")
print("| bestellen?     \t|")
us_best = input("Das: ")
if us_best > pommes:pomm
        
print("||")
print("\\o---------------------o/")
input()
os.system('cls')
print