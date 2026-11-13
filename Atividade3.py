for venda in range(6):
    valor = float(input('Valor da compra: R$'))

    if valor >= 200:
        desconto = valor * 0.10

    else:
        desconto = 0

    valor_final = valor - desconto

    print(f'desconto: R$ {desconto:.2f}')
    print(f'valor final: R$ {valor_final:.2f}')
    print('fim das cinco vendas!')
