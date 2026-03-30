import time
import random as rd

def jogar_forca():
    print('*--------------------*')
    print('BEM VINDO AO JOGO DE FORCA')
    print('*--------------------*')
    print('Escolhendo Palavra')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('..')
    time.sleep(1)
    print('...')

    arquivo = open("palavras.txt" , "r")
    palavras = []
    
    for linha in palavras:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    palavra_escolhida = int(rd.randint(0, len(palavras)))

    # time.sleep(1)
    # print('Palavra escolhida!')
    # time.sleep(1)
    palavra_secreta = palavras[palavra_escolhida]
    letras_acertadas = ["_" for letra in palavra_secreta]
    perdeu = False
    acertou = False
    erros = 0

    print(f'Palavra: {letras_acertadas}')
    while(not perdeu and not acertou):
        
        chute = input('Digite uma Letra: ')
        chute = chute.strip().lower()

        #Index define a posição da letra
        
        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute.lower() == letra.lower()):
                    # print(f'A letra {chute} está na posição {index}!')
                    letras_acertadas[index] = letra
                index += 1
                
        else:
            erros = erros + 1
            
        perdeu = erros == 6
        acertou = "_" not in letras_acertadas

        
        print(f'Palavra: {letras_acertadas}')
        print(f'Erros: {erros}')
        if perdeu == True:
            print('Você perdeu!')
        elif acertou == True:
            print('Parabéns, você adivinhou a palavra secreta!')
        







if(__name__ == "__main__"):
    jogar_forca()