"""
crie um sistema que peça ao usuária digitar uma senha ara acessar sua conta bancaria. Ele tem **apenas 3 tentativas para acertar. 
Se ele errar as 3 o sistema bloqueia a conta.
- A senha correta: 1234
-o usuário tem 3 tentativas input()
-se ele errar 3x, conta bloqueada.
"""

SENHA_CORRETA = "1234"  # constante, boa prática, escopo global.i 
tentativas = 3 # variável contadora, pode ser 1 ou j, escopo global

while tentativas > 0:
    senha = input("Digite a sua senha: ") # variável no escopo local
    if senha == SENHA_CORRETA:
        print("Senha correta! 🔓")
        break # finaliza o código.
    else:
        # tentativas = tentativas -1  ou -= 1
        tentativas -= 1
        print(f'Senha incorreta... tentativas restantes: {tentativas}')

    if tentativas == 0:
        print("X conta bloqueada")
