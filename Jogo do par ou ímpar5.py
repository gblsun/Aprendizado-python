numero = int(input("Digite um número natural maior ou igual a dois: "))

impar_anterior = numero - 1 if numero % 2 == 0 else numero - 2

par_posterior = numero + 2 if numero % 2 == 0 else numero + 1

print(impar_anterior, par_posterior)