# estrutruras condicionais permitem que o progama execute blocos de código diferentes dependendo de uma condição. A condição é sempre avaliada como True(verdadeiro) e o False(falso).

# se o usuário tiver a idade maior que 18 ele poderá entrar.
# if -> Verifica uma condição e executa o bloco de códigpo associado se a condição pe verdadeira.
# idade_usuario = int(input("Digite a sua idade: ")) 
# if idade_usuario > 18:
#     print("O usuário pode acessar o local.")

#else ->permite executar o bloco de código se a condição di if for falso.
# if idade_usuario > 18:
#     print("O usuario pode acessar o local.😁")
# else:
#     print("o usuário não pode entrar.😒")

# elif -> abreviação (else if) é usado para testar varias condições. Ele só será exibido se todas as condiçoes anteriores forem falsas.
nota = int(input("Digite a sua nota: "))
# nota maior ou igual a 90, "aprovado com excelencia"
# nota for maior ou igual a 70, "aprovado"
# qualquer outra nora, "reprovado"
if nota >= 90:
    print("aprovado com excelencia")
elif nota >= 70: 
    print("aprovado")
else:
    print("reprovado")  
    