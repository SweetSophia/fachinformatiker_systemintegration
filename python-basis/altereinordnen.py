alter = input(("Alter eingeben"))

if alter >= 18:
    print(f"Erwachsenenalter, da {alter} Jahre alt.")
elif alter < 14:
    print(f"Kind, da {alter} Jahre alt.")
else:
    print(f"Jugendlich, da {alter} Jahre alt.")