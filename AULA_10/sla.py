pizza = 0
faturamento = 0
maior_venda = 0
menor_venda = 0
acima_50 = 0
while True:
    valor = float(input("Valor da pizza vendida (0 para encerrar) R$: ")) 
    if valor == 0:
        break
    if valor < 0:
        print("Valor inválido, digite um valor positivo!")
        continue 
    pizza += 1
    faturamento += valor
    if valor > maior_venda:   #na primeira venda ele é maior 
        maior_venda = valor
    if pizza == 1 or valor < menor_venda:
        menor_venda = valor
    if valor > 50:
        acima_50 += 1
# print(f"Esse foi o valor da variável pizza no while: {pizza}")
# print(f"Esse foi o valor da variável faturamento no while: {faturamento:.2f}")
# print(f"Esse foi o valor da variável valor no while: {valor}")
if pizza ==0:
    print("Nenhuma venda registrada")
else:
        ticket_medio = faturamento / pizza
        print("=== FECHAMENTO DE CAIXA ===")
        print(f"pizza vendidas: {pizza}")
        print(f"faturamento total: {faturamento:.2f}")
        print(f"teckte medio: {ticket_medio:.2f}")
        print(f"maior venda: {maior_venda:.2f}")
        print(f"menor venda: {menor_venda:.2f}")
        print(f"pizza acima de 50: {acima_50:.2f}")

    # Se o valor for 0, encerra o loop
    # verificar se o valor é positivo ou não(valor correto)

