nome = input("Informe seu  Nome:" ).strip().title()
idade = int(input("Informe sua Idade:" ))

if idade >= 18:
    print(f"{nome} é maior de idade.")
else: 
    print(f"{nome} é menor de idade.")