"""
    crie um progama que simule um caixe eltronico. O usuário pode sacar valores até que o slado disponível acabe ou até digitar "sair.
    - comece pelo saldo disponível de 500
    - peca p o usuario digitar um valor p saque
    - se o valor foi maior nao tem como
    - se ele difitar sair ele sai
"""

saldo = 500

while saldo > 0:  # irá continuar até ser false. ou ate sair.
    print(f'/n 💸saldo disponível: R${saldo:.2f}') # /n quebra linha
    saque = input("Digite o valor que desja sacar ou difite sair: ")

    if saque.lower()== "sair":
        print("Operação cancelada.")
        break 
    saque = float(saque)
    if saque > saldo:
        print("X saldo insuficiente!")
    else:
        saldo -= saque
        print(f"Saque de R$:{saque:.2f} realizado com sucesso!")