# solicitar a idade de várias pessoas e calcular a media da idade delas
#finalizar quando o usuario utilizar uma idade negativa

conta_idades = 1
soma_idade = 0

while True:
    idade = int(input('Informe a idade: '))
    if idade < 0:
        break
    soma_idade += idade
    conta_idades += 1

print(soma_idade)
if conta_idades > 0:
    media = soma_idade / conta_idades
    print(f'Média de idade das pessoas: {media:.2f}')
else:
    print('idade invalida')