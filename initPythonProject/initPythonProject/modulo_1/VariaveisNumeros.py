# Numeros
print("\nNumeros")
print(type(37))
print(type(10.1))
print(type(1 + 2j))

# Operação
print("\nOperação")

qtd_items_carrinho_compra = 0

qtd_items_carrinho_compra = qtd_items_carrinho_compra + 1 # incremento
print(qtd_items_carrinho_compra)

qtd_items_carrinho_compra = qtd_items_carrinho_compra + -1 # decrementando
print(qtd_items_carrinho_compra)

qtd_items_carrinho_compra += 1
print(qtd_items_carrinho_compra)

qtd_items_carrinho_compra -= 1
print(qtd_items_carrinho_compra)

# Conta básica
print("\nConta básica")
preco = 47
quantidade = 0.250
total_a_pagar = preco * quantidade
print("Total a pagar: ", total_a_pagar)

a = 3
b = 2

c = a / b
print("Resultado: ", c) # divisão normal - resultado fracionado

d = a // b
print("Resultado: ", d) # divisão normal - resultado inteiro por conta do '//'

# Conversão
print("\nConversão")
print("int(3.9): ", int(3.9))
print("float(10): ", float(10))
print("complex(1): ", complex(1))

# Exercício
soma_valor_total_venda_19 = 153.98
soma_qtd_total_vendas_19 = 3
ticket_medio_19 = soma_valor_total_venda_19 / soma_qtd_total_vendas_19
print("(19/01) - Ticket médio: ", ticket_medio_19)

soma_valor_total_venda_20 = 337.01
soma_qtd_total_vendas_20 = 7
ticket_medio_20 = soma_valor_total_venda_20 / soma_qtd_total_vendas_20
print("(20/01) - Ticket médio: ", ticket_medio_20)

soma_valor_total_venda_23 = 295.33
soma_qtd_total_vendas_23 = 5
ticket_medio_23 = soma_valor_total_venda_23 / soma_qtd_total_vendas_23
print("(23/01) - Ticket médio: ", ticket_medio_23)
print("Média geral: ", (ticket_medio_19 + ticket_medio_20 + ticket_medio_23) / 3)