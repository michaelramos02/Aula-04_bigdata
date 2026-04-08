valor = float(input('Digite o valor da compra: '))
formaPagamento = input('Digite a forma de a pagamento: ').lower()

if valor > 250 and formaPagamento == 'a vista':
    print(f'O valor total é R${valor - valor*0.16:.2f} e o desconto aplicado foi de R${valor * 0.16:.2f}')
else:
    print(f'o valor total é R${valor:.2f}')
