valor = float(input('valor da venda: R$ '))

print('''
[1] - pix (12% de desconto)
[2] - debito (8% de desconto)
[3] - credito (5% de desconto)
[4] - dinheiro (15% de descontp)
''')
operacao = True
desconto = 0
opcao = int(input('informe a opção escolhida: '))

match opcao:
    case 1:
        print('... pix ...')
        desconto = valor * 0.12

    case 2:
        print('... debito ...')
        desconto = valor * 0.08

    case 3:
        print('... credito ...')
        desconto = valor * 0.05

    case 4:
        print('... dinheiro ...')
        desconto = valor * 0.15

    case _:
        operacao = False
        print('Opção Invalida')

if operacao == True:

#if desconto != 0:
    valor_final = valor - desconto
    print(f'preço: {valor}')
    print(f'desconto: {desconto}')
    print(f'total a pagar: {valor_final}')

else:
    print('escolha umas das opções acima')



    
 