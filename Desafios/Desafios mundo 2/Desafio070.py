#Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

# A) qual é o total gasto na compra.

# B) quantos produtos custam mais de R$1000.

# C) qual é o nome do produto mais barato.


print('+-'*25)
print(' Utencílios Sergio Sena ')
print('+-'*25)

item = str(input('Digite o produto: '))
valor = float(input('Digite o valor do produto: '))
ytyjuhresp = ('Quer continuar? [S/N]: ').upper().strip()[0]
print(f'Item:{item} Valor:{valor} Continuar?{resp}')    