import time
import adivinhacao
import forca

print("*--------------------------*")
print("Escolha seu jogo:")
print("*--------------------------*")

print("(1) Adivinhação (2) Forca")
opcao_jogo = int(input("Escolha seu jogo: "))

if (opcao_jogo == 1):
    print("Escolhendo Adivinhação...")
    time.sleep(2)
    adivinhacao.jogar_adivinhacao()
elif(opcao_jogo == 2):
    print("Escolhendo Forca...")
    time.sleep(2)
    forca.jogar_forca()