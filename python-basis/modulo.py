summe = 0

for zahl in range(1,10):
    print(f"Wir sind im Durchlauf {zahl}")
    if zahl  % 3 == 0:
        print(f"Die Zahl {zahl} lässt sich glatt durch 3 teilen.")
        summe = summe + zahl
        #alternative: summe += zahl
print(f"Die Summe ist: {summe}.")
        