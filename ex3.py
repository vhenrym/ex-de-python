# Solicitar ao usuário 10 números e verificar se é par ou imar

cont = 1
conta_pares = 0
conta_impares = 0
conta_negativos = 0

while cont <=10:
    numero = int(input("Número: "))
    if numero %2 == 0:
        conta_pares += 1
    else:
        conta_impares += 1
    if numero <= 0:
        conta_negativos += 1
    cont += 1

print(f'Quantidade de números pares: {conta_pares}')
print(f'Quantidade de números negativos: {conta_negativos}')
print(f'Quantidade de números impares: {conta_impares}')


