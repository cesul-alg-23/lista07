populacao = int(input('Informe a população atual: '))
taxa = float(input('Informe a taxa de crescimento: '))

for i in range(1, 16):
    populacao += int(populacao * taxa / 100)
    print(f"{i}º ano: {populacao}")
