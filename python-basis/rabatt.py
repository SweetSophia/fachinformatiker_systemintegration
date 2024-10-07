# DIN 66001
bestellwert = float(input("Preis angeben: "))
rabatt = 0

if bestellwert >= 100:
    rabatt = bestellwert*0.1
    
else:
    rabatt = 0
    
print(f"Der Rabatt beträgt:130 {rabatt:.2f}. Der Gesamtpreis beträgt: {bestellwert-rabatt}")