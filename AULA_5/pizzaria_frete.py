# frete da pizzaria


# distancia = float(input("Digite a sua distância em KM: "))1
# if distancia <= 5:
#     print("Frete: R$ 5,00")
# elif distancia <= 10:
#     print("Frete: R$ 10,00")
# else:
#     print("Não entregamos nessa distância. 😕")


# distancia = int(input("Digite a sua distância em KM: "))2
# taxa_fixa = 5.00   #cobrada em toda entrega
    
# if distancia <= 5:
#     valor_km = 1.00
#     frete = 5.00 + (distancia * valor_km)
#     print(f"R$ {frete:.2f}".replace(".", ","))
# elif distancia <= 10:
#     valor_km = 2.00
#     frete = taxa_fixa + (distancia * valor_km)
#     print(f"R$ {frete:.2f}".replace(".",","))
# else:
#     print("Não entregamos nessa distância. 😕")

distancia = int(input("Digite a sua distância em KM: "))
dia_semana = input("Digite o dia da semana: ".lower())
valor = float(input("Valor do pedido: R$ "))
taxa_fixa = 5.00   #cobrada em toda entrega
    
if distancia <= 5:
    valor_km = 1.00
    frete = taxa_fixa + (distancia * valor_km)
    print(f"R$ {frete:.2f}".replace(".", ","))
elif distancia <= 10:
    valor_km = 2.00
    frete = taxa_fixa + (distancia * valor_km)
    print(f"R$ {frete:.2f}".replace(".",","))
else:
    print("Não entregamos nessa distância. 😕")


dia_semana = input("Digite o dia da semana: ".lower())
valor = float(input("Valor do pedido: R$ "))
if dia_semana == "terca" or dia_semana == "terça":
    if valor > 40.00:
          print("🍰 Você ganhou uma sobremesa grátis!")
elif dia_semana == "quarta": 
    desconto = valor * 0.15
    print(f"R$ {desconto:.2f}".replace(".",","))
elif dia_semana == "sabado" or dia_semana =="sábado" or dia_semana == "domingo":
    if valor < 100.00:
        print(f"R$ {valor:.2f}".replace(".",","))
else:
    print("Dia sem promoção :(")



print(f"dia da semana: {dia_semana}")
print(f"Valor do pedido: {frete:.2f}".replace(".","."))


