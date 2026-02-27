import random as rd
print ("S͓̽e͓̽j͓̽a͓̽ ͓̽B͓̽e͓̽m͓̽-͓̽V͓̽i͓̽n͓̽d͓̽o͓̽ ͓̽a͓̽o͓̽ ͓̽M͓̽t͓̽.͓̽ ͓̽H͓̽o͓̽l͓̽l͓̽y͓̽!͓̽")

n_secreto = rd.randrange(1, 101)
n_tentativas = 0
rodada = 1
pontos = 1000

print('Níveis  de dificuldade')
print('\n(1) Fácil (2) Médio (3) Difícil (4) Aleatório\n')

nível = int(input('Escolha a dificuldade:'))

if(nível == 1):
    n_tentativas = 12
elif (nível == 2):
    n_tentativas = 6
elif (nível == 3):
    n_tentativas = 3
else:
    n_tentativas = rd.randrange(1, 11)

for rodada in range(1, n_tentativas + 1):
    print(f'Tentativa {rodada} de {n_tentativas}')
    n_escolhido = int(input("Digite um número aleatório: "))
    acerto = n_escolhido == n_secreto
    n_maior = n_escolhido > n_secreto
    n_menor = n_escolhido < n_secreto

    if(n_escolhido > 100 or n_escolhido < 1):
        print('o valor digitado não é permitido!')
        continue

    print(f"Você digitou o número: {n_escolhido}")

    if(acerto):
        print(f"Você acertou! o número correto era {n_secreto}!")
        break
    else:
        if(n_maior == True):
            print(f"Você errou! Mas o número {n_escolhido} é maior que o número secreto!")
        if(n_menor == True):
            print(f"Você errou! Mas o número {n_escolhido} é menor que o número secreto!")
        if(rodada == n_tentativas):
            print(f"Sinto muito, você perdeu, o número secreto era: {n_secreto}")


        perda_de_pontos = abs(n_secreto - n_escolhido)
        pontos = pontos - perda_de_pontos

        

            
print(f'Seus pontos finais foram {pontos}!')
print("Fim do Jogo")