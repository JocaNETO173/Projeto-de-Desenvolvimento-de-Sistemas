palavra = 'carambola'

teste_valores = []
print(type(teste_valores))

i = 0
secreto = ''

for i in range(len(palavra)):
    teste_valores.append('_')
    secreto += f'{teste_valores[i]} '
print(secreto)

