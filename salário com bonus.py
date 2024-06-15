nome_vendedor = input().strip()
salario_fixo = float(input())
total_vendas = float(input())

comissao = total_vendas * 0.15
total_receber = salario_fixo + comissao

print(f"TOTAL = R$ {total_receber:.2f}")
