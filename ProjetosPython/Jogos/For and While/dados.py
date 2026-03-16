import random as rd

def jogar_dados():

    print('*--------------------*')
    print('BEM VINDO AO JOGO DE 21 COM DADOS')
    print('*--------------------*')

    print('Jogo de 21')
    print('Você irá rodar dois dados de 6 lados')
    print('Os dois resultados serão somados, o objetivo é chegar o mais perto possível do número 21')
    print('Você poderá escolher continuar jogando ou desistir, afinal, se passar de 21 você perde')
    print('1 = rodar de novo, 2 = desistir')
    continuar = input('Digite um valor:')
    soma_total = 1 

    while continuar == '1':
        dado1 = rd.randint(1, 6)
        dado2 = rd.randint(1, 6)
        soma_rodada = dado1 + dado2
        soma_total += soma_rodada
        
        if(continuar == '1'):
            
            
            print(f'Você tirou [{dado1}] e [{dado2}] e a soma total é {soma_total}')
            continuar = input('Digite [1] para rodar de novo ou [2] para desistir/parar: ')

            if(soma_total > 21):
                print(f'Você passou muito de 21, tente novamente!')
                break
            elif(soma_total == 21):
                print('Parabéns! Você atingiu 21!')
                break
    if(continuar == '2' and soma_total < 21):
            print(f'Você parou, e seu resultado foi {soma_total}')
jogar_dados()