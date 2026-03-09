import time
import random as rd



print('Seja Bem-vindo ao conversor de unidades!')
numero_inteiro = int(input('Digite um número: '))
print('Escolha para qual unidade você quer converter seu número')
unidade = int(input('(1) Hexadecimal (2) Octal\n Escolha: '))
numero_convertido = ''
formato = ''

def toHex(numero_inteiro):
    return hex(numero_inteiro)

def toOct(numero_inteiro):
    return oct(numero_inteiro)

if(unidade == 1):
    numero_convertido = toHex(numero_inteiro)
    formato = 'Hexadecimal'
    print(f'Seu número em formato inteiro era {numero_inteiro}\n Você selecionou converter para {formato}\n E ele fica assim: {numero_convertido}')

elif(unidade == 2):
    numero_convertido = toOct(numero_inteiro)
    formato = 'Octal'
    print(f'Seu número em formato inteiro era {numero_inteiro}\n Você selecionou converter para {formato}\n E ele fica assim: {numero_convertido}')
else:
    print('Essa opção não está disponível!')
time.sleep(3)


