# Tabuada na unha #
print("#Feito na unha")
n = int(input('Digita a tabuada que você quer ver :'))
print('-'*12)
print('{} x {:2} = {}'.format(n,0,n*0))
print('{} x {:2} = {}'.format(n,1,n*1))
print('{} x {:2} = {}'.format(n,2,n*2))
print('{} x {:2} = {}'.format(n,3,n*3))
print('{} x {:2} = {}'.format(n,4,n*4))
print('{} x {:2} = {}'.format(n,5,n*5))
print('{} x {:2} = {}'.format(n,6,n*6))
print('{} x {:2} = {}'.format(n,7,n*7))
print('{} x {:2} = {}'.format(n,8,n*8))
print('{} x {:2} = {}'.format(n,9,n*9))
print('{} x {:2} = {}'.format(n,10,n*10))
print('-'*12)

# Tabuada com range #
print("#Feito com range")
for item in range(11):
    print('{} x  {:2}  = {}'.format(n,item,n*item))
print('-'*12)  