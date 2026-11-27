valor_da_gasolina = float(input("Valor gasolina: "))
valor_do_etanol = float(input("Valor etanol: "))

if valor_do_etanol <= valor_da_gasolina * 0.75:
    print("Compensa mais abastecer com etanol")
else:
    print("Compensa abastecer com gasolina")