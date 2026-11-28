valor_da_gasolina = float(input("Valor gasolina: ").replace(',','.'))
valor_do_etanol = float(input("Valor etanol: ").replace(',','.'))

if valor_do_etanol <= valor_da_gasolina*0.75:
    print("Slk Compensa mais abastecer com etanol")
else:
    print("Slk Compensa mais abastecer com gasolina")