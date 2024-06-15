codigo1, numero_peca1, valor_peca1 = input().split()
codigo1 = int(codigo1)
numero_peca1 = int(numero_peca1)
valor_peca1 = float(valor_peca1)

codigo2, numero_peca2, valor_peca2 = input().split()
codigo2 = int(codigo2)
numero_peca2 = int(numero_peca2)
valor_peca2 = float(valor_peca2)


valor_final = (numero_peca1 * valor_peca1) + (numero_peca2 * valor_peca2)

print(f"VALOR A PAGAR: R$ {valor_final:.2f}")