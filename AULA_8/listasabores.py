# sabores = ["Mussarela", "Calabresa", "Pepperoni", "Quatro Queijos", "Frango com Catupiry"]

# print("Sabores disponíveis na Pizzaria Sabores:")
# for sabor in sabores:
#     print(f'🍕 - {sabor}')

#--------------------------------------------------------------------------------------------------------------------------
# print("Preparando sua pizza...")
# for minuto in range(1,6):
#     print(f'⏳{minuto} minuto(s) se passou...')

# print("Sua pizza está pronta!")

#--------------------------------------------------------------------------------------------------------------------------
# clientes = ["João", "Maria", "Carlos", "Ana", "Pedro"]

# print("Atendendo clientes:")
# for i, clientes in enumerate(clientes):
#     if i == 3:
#         print("Capacodade máxima atingida.")
#         break
#     print(f"Atendendo {clientes}...")
#--------------------------------------------------------------------------------------------------------------------------

pedidos = ["Mussarela", "cancelado", "Calabresa", "cancelado", "Pepperoni"]

for pedido in pedidos:
    if pedido == "cancelado":
        continue  # pula este e vai para o próximo
    print(f"Preparando pizza de {pedido}...")

