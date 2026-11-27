massa = float(input("Sua massa muscular: ").replace(',','.'))
altura = float(input("Sua altura: ").replace(',','.'))

if massa <= 140 and altura >= 1.15:
    print(f"Entrada do usuário foi permitida.")
else: 
    print(f"Entrada do usuário foi negada.")