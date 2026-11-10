# Perguntas ao cliente
# pizza pequena= 19,90
# pizza media = 29,90
# pizza grande = 39,90

FRETE = 2
dia_semana = "sabado"

print(f"""
       =======================================
        🍕Seja bem-vindo a pizzaria sabores🍕
       =======================================
""")
nome_cliente = input(f"""
        🥸Digite o seu nome:
""")
pizza_sabor = input(f"""
        🍕Escolha uma das opções abaixo;
        1- Para frango com requijão
        2- Calabresa
        3- Mussarela
        4- Banana com chocolate
          """)
pizza_tamanho = input(f"""
        Escolha o tamanho da pizza:
        1- pequeno
        2- médio
        3- grande
""")
forma_entrega = input(f"""
        Escolha a forma de entrega:
        1- consumo no local
        2- entrega na residencia
""")

# estrutura condicional para a promoção
# comprando qualquer pizza e qualquer tamanho no sabado o refri é de graça.
# comprando qualquer pizza de qualquer tamanho no domingo, o frete e o refri é gratuitos.
# comprando uma pizza de calabresa tamanho médio, em qualquer dia, p frete é grtuito.
if dia_semana == "sabado":
    print(f" pedido aceito com sucesso")
    print(f"o refri é por nossa conta!")
elif dia_semana == "domingo":
    print(f" pedido aceito com sucesso")
    print(f"o frete e o refri é por nossa conta!")
elif pizza_sabor == "calabresa" and pizza_tamanho == "media":
    print(f" pedido aceito com sucesso")
    print(f"o refri é por nossa conta!")







# print(f"""
#         =======================================
#                 🧾Resumo do pedido
#         nome do cliente: {nome_cliente}
#         sabor da pizza: {pizza_sabor}
#         tamanho da pizza: {pizza_tamanho}
#         forma de entrega: {forma_entrega}
#         =======================================
# """)