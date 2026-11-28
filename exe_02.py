nome = input("Digite seu nome: ").title().strip()
massa = float(input("Digite sua massa: ").replace(',','.'))
altura = float(input("Digite sua altura: ").replace(',','.'))

imc = massa / (altura * altura)

if imc < 18.5:
    print(f"{nome} Usuário está abaixo do peso anemico magrelo")
elif imc < 25:
    print(f"{nome} Usuário está com  o peso ideal de uma pessoa saúdavel")
elif imc < 30:
    print(f"{nome} Usuário está acima do gordo")
elif imc < 35:
    print(f"{nome} Usuário está imenso de obeso")
elif imc < 40:
    print(f"{nome} Usuário está no nível 2 de obesidade")
else:
    print(f"{nome} Usuário está gordo mórbido")