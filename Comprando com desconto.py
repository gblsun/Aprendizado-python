preco_mercadoria = float(input("Digite o preço da mercadoria: "))
quantidade_comprada = int(input("Digite a quantidade comprada: "))

# DESCONTO
desconto_fixo = 0.10
desconto_por_unidade = 0.01
desconto_total = desconto_fixo + (quantidade_comprada * desconto_por_unidade)

# PRECO SEM DESCONTO
preco_sem_desconto = preco_mercadoria * quantidade_comprada

# PRECO COM DESCONTO
preco_com_desconto = preco_sem_desconto - (preco_sem_desconto * desconto_total)

print(f"{preco_sem_desconto:.2f}")
print(f"{preco_com_desconto:.2f}")
