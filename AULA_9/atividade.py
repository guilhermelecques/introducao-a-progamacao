# numero = int(input("Digite um numero inteiro e positivo para a contagem: "))

# while numero > 0:
#     print(numero)
#     numero -= 1
#    print(f"FOGO!!!")
# -----------------------------------------------------------------------------

# while True:
#     senha = input("Crie uma senha (deve ter no mínimo 8 caracteres): ")

    
#     if len(senha) >= 8:
#         print("Senha criada com sucesso!")
#         break  
#     else:
#         print(" A senha precisa ter no mínimo 8 caracteres! Tente novamente.")
#-----------------------------------------------------------------------------------

num_secreto = 17

while True:
    palpite = int(input("Digite seu aplpite!"))
    if palpite == num_secreto:
        print("Você ACERTOU!!")
    elif palpite < num_secreto:
        print("MUITO BAIXO")
    else:
        print("MUITO ALTO")