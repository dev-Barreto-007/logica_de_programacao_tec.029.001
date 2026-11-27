nome = input("Seu nome: ").strip().title()
nota1 = int(input("nota1: "))
nota2 = int(input("nota2: "))


media = (nota1+nota2)/2

print(f"Média:{media}")

if media >= 7:
    print(f"{nome} felizmente está aprovado.")
elif media >=5:
    print(f"{nome} infeliznente está de recuperação.")
else:
    print(f"{nome} infelizmente está reprovado.")