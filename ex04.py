maior = 0
menor = 0

for i in range(10):
    num = int(input('Informe um número inteiro: '))

    if i == 0:
        maior = num
        menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num

print(f'O maior número informado foi: {maior}')
print(f'O menor número informado foi: {menor}')
