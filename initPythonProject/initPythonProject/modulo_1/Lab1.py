## Lição 1
print("Olá! mundo!")
print("\n")

## Lição 2
# Use expressões algébricas para calcular (A), (B) e (C) na tabela de ticket médio abaixo:

# 19/01
qtd_total_vendas_1 = 3
ticket_medio_1 = 320.52

# 20/01
valor_total_vendas_2 = 834.47
ticket_medio_2 = 119.21

# 23/01
valor_total_vendas_3 = 15378.12
qtd_total_vendas_3 = 5

# Calcule aqui:
A = qtd_total_vendas_1 * ticket_medio_1
B = valor_total_vendas_2 / ticket_medio_2
C = valor_total_vendas_3 / qtd_total_vendas_3

# Print
print('(A) = ', A)  # (A) = 961.56
print('(B) = ', B)  # (B) = 7.000000000000001
print('(C) = ', C)  # (C) = 3075.6240000000003

print("\n")

## Lição 3
# Aplique três métodos distintos na string abaixo.
cancao = 'Roda mundo, roda gigante, roda moinho, roda pião.'

# Substitua todas as vírgulas por barras /
result1 = cancao.replace(',', '/')
print(result1)

# Deixe a string em maiúscula
result2 = cancao.upper()
print(result2)

# Encontre a posição da palavra "moinho" na string
result3 = cancao.find('moinho')
print(result3)

print("\n")

## Lição 4
# Extraia da string abaixo o valor da taxa selic na variável `selic` e o valor do ano na variável `ano`. Imprima os valores na tela.

noticia = 'Selic vai a 2,75% e supera expectativas é a primeira alta em 6 anos.'

selic = noticia[12:17]
ano = noticia[-7]

print(selic)
print(ano)

print("\n")

## Lição 5
# Utilize a tabela da verdade para responder: qual o valor da variável `x`?

a = False
b = True
x = not a & b

# Resposta
#x = True