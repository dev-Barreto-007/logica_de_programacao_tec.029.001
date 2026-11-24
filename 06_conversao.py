nome = input("Digite seu  Nome:" )
idade = input("Informe sua Idade:" )
altura = input("Informe sua altura:" ).replace(',','.')

idade = int(idade)
altura = float(altura)

print(f"Nome: {nome}. Tipo: {type(nome)}")
print(f"Idade: {idade}. Tipo: {type(idade)}")
print(f"Altura: {altura} metros. Tipo: {type(idade)}")