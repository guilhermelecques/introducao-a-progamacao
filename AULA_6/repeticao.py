sabores_pizza = ["Mussarela", "Calabresa", "Pepprtoni", "Quato queijos", "Frango com catupiri"]
print("Faça seu pedido (Digite 'sair' para encerrar): ")
pizza = ""      # aqui ficará armazenado o pizza do cliente.

# enquanto o sair não for difitado o while continuará sendo executado.
while pizza.capitalize() != "Sair":
    pizza = input("Escolha um sabor: ").capitalize()
    if pizza in sabores_pizza:
        print(f'{pizza} foi adicionado a sua compra.') 
    elif pizza.capitalize() == "Sair":
        print( "Pedido encerrado!")
    else:
        print("Esse sabor não está  disponível. Escolha outro: ")