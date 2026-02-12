
print ("S͓̽e͓̽j͓̽a͓̽ ͓̽B͓̽e͓̽m͓̽-͓̽V͓̽i͓̽n͓̽d͓̽o͓̽ ͓̽a͓̽o͓̽ ͓̽M͓̽t͓̽.͓̽ ͓̽H͓̽o͓̽l͓̽l͓̽y͓̽!͓̽")

n_secreto = 46
n_escolhido = int(input("Digite um número aleatório: "))
acerto = n_escolhido == n_secreto
n_maior = n_escolhido > n_secreto
n_menor = n_escolhido < n_secreto

print(f"Você digitou o número: {n_escolhido}")

if(acerto == True):
    print(f"Você acertou! o número correto era {n_secreto}!")
else:
     if(n_maior == True):
        print(f"Você errou! Mas o número {n_escolhido} é maior que o número secreto!")
     if(n_menor == True):
         print(f"Você errou! Mas o número {n_escolhido} é menor que o número secreto!")