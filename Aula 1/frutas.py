print('Digite uma senha:')
senha = int(input('Senha:'))
print(senha)

for caractere in senha:
  if caractere > 5:
    print('Senha só pode ter números de 0 a')
  else:
    print('')

# Para cada caractere na senha, verificar se é um número de 1 a 5