valor = float(input('Digite o valor da compra: '))

if valor >= 250:
    desconto = valor * 0.16
    totalValor = valor - desconto
    print(f'O valor é R${totalValor:.2f} e o desconto foi de R${desconto:.2f}')
else:
    print(f'O valor é R${valor:.2f}')
