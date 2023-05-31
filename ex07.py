num = int(input('Informe um número inteiro: '))

primo = True
limite = (num // 2) + 1
for i in range(2, limite):
    if num % i == 0:
        primo = False
        break

if primo:
    print('É primo!')
else:
    print('Não é primo!')
