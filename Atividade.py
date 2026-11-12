valor = float(input('valor do ingresso: R$ '))

print('\nTIPO DE ENTRADA')
print('1 - inteira')
print('2 - meia entrada')
print('3 - promoção')

opcao = int(input('Escolha Opção: '))
desconto =  0

match opcao:
    case 1:
        desconto = 0
    case 2:
        desconto = 0.50
    case 3:
        desconto = 0.30
    case _:
        print('Opção invalida')
        

if opcao in [1, 2, 3]:
    valor_desconto = valor * desconto
    valor_final = valor - valor_desconto


    print(f'desconto: R$ {valor_desconto:.2f}')
    print(f'valor final: R$ {valor_final:.2f}')
