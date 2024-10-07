# DIN 66001
temp1 = float(input("Temperatur 1 angeben: "))
temp2 = float(input("Temperatur 2 angeben: "))
temp3 = float(input("Temperatur 3 angeben: "))

durchschnitt = (temp1 + temp2 + temp3)/3

print(f"Die Durschnittstemperatur beträgt : {round(durchschnitt,2)}°C")

if durchschnitt < 15:
    print("Es wird kühl. Die Jacke nicht vergessen.")
else:
    print("Es wird heiß! Trinken nicht vergessen.")