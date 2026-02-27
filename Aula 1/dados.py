import random as rd
print('Jogo de 21')
print('Você irá rodar dois dados de 6 lados')
print('Os dois resultados serão somados, o objetivo é chegar o mais perto possível do número 21')
print('Você poderá escolher continuar jogando ou desistir, afinal, se passar de 21 você perde')
print('1 = rodar de novo, 2 = desistir')
option = input('Digite um valor:')
continuar = '1'
soma_total = 0

while continuar == '1':
    dado1 = rd.randint(1, 6)
    dado2 = rd.randint(1, 6)
    soma_rodada = dado1 + dado2
    soma_total += soma_rodada
    
    print(f'Você tirou [{dado1}] e [{dado2}] e a soma total é {soma_total}')
    continuar = input('Digite [1] para rodar de novo ou [2] para desistir/parar: ')

    if(soma_total > 21):
        print(f'Você passou muito de 21, tente novamente!')
        break
    elif(soma_total == 21):
        print('Parabéns! Você atingiu 21!')
        break
    elif(continuar == '2' and soma_total < 21):
        print(f'Você parou, e seu resultado foi {soma_total}')
    
    print('Rodada do Computador!')
    dadoPC1 = rd.randint(1, 6)
    dadoPC2 = rd.randint(1, 6)
    somaPC = dadoPC1 + dadoPC2