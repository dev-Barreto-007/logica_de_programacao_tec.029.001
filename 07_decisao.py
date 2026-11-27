nome = input("Informe seu  Nome:" ).strip().title()
idade = int(input("Informe sua Idade:" ))

if idade >= 18:
    print(f"{nome} é maior de idade, boa guerreiro!.")
else: 
    print(f"{nome} é menor de idade vaza daqui.")