
import random
print ("S͓̽e͓̽j͓̽a͓̽ ͓̽B͓̽e͓̽m͓̽-͓̽V͓̽i͓̽n͓̽d͓̽o͓̽ ͓̽a͓̽o͓̽ ͓̽e͓̽n͓̽i͓̽g͓̽m͓̽a͓̽ ͓̽d͓̽o͓̽ ͓̽M͓̽t͓̽.͓̽ ͓̽H͓̽o͓̽l͓̽l͓̽y͓̽!͓̽")

n_secreto = random.randint(1, 10)
n_escolhido = int(input("͓̽D͓̽i͓̽g͓̽i͓̽t͓̽e͓̽ ͓̽a͓̽ ͓̽s͓̽e͓̽n͓̽h͓̽a͓̽:͓̽ "))

if(n_escolhido == n_secreto):
    print(f"Você acertou! O número correto era {n_secreto}!")
else:
    print(f"Você errou! O número correto era {n_secreto}!")
