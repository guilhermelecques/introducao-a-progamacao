dia = input("Informe o dia da semana: ").lower()
valor = float(input("informe o valor da pizza: "))
taxa_fixa = 5.00
frete = taxa_fixa

if dia == "terca" or dia =="terça":
    if valor > 40:
        print("🍰 Você ganhou uma sobremesa grátis!")
        valor_final = valor + taxa_fixa
        print(f"Total a pagar: R$ {valor_final:.2f}".replace(".",","))
elif dia == "quarta":
    valor_2 = valor * 0.85
    valor_final = valor_2 + taxa_fixa
    print("🍕Você ganhou 15% de desconto na sua pizza!")
    print(f"Total a pagar: R$ {valor_final :.2f}".replace(".",","))
elif dia == "sabado" or dia == "sábado" or dia =="domingo":
    if valor > 100:
        print("🛵Você ganhou frete grátis!")
        frete = 0
        valor_final = valor + frete
        print(f"Total a pagar: R$ {valor_final :.2f}".replace(".",","))
    else:
        frete = taxa_fixa
        valor_final = valor + frete
        print(f"Total a pagar: R$ {valor_final :.2f}".replace(".", ","))
else:
    valor_final = valor + taxa_fixa
    print("Dia sem promoção :(")
    print("total a pagar: R$ {valor_final:.2f}".replace(".",","))