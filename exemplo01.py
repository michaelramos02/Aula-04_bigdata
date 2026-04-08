# # Estrutura if

# idade = int(input('Digite a sua idade: '))

# if idade >= 18: 
#      print('Maior de idade')

# elif idade >= 15:
#      print('Quase adulto')
# else:
#      print('Menor de idade')

# ------------------------------------------------------

# Estrutura de pontuação
     

pontos = float(input('Digite os seus pontos: '))

if pontos >= 100:
     print('Execelente!')
elif pontos >= 50:
     print('Bom desemp')
else:
     print('Pode melhorar')
     

# operadores AND e OR
     
usuario = input('nome: ')
senha = input('Senha: ')

if usuario == 'admin' and senha == 'senha1234':
     print('Acesso autorizado')
else:
     print('Acesso negado')