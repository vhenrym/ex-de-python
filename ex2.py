# Solicitar ao usuário 5 números e verificar se é par ou imar

cont = 1
while cont <= 5:
    numero = int(input("Número: "))
    if numero % 2==0:
        print('PAR')
    else:
        print('IMPAR')
        cont += 1