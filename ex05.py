import random

sorteio = random.randint(0, 100)
acertou = False

for i in range(1, 11):
    palpite = int(input('Informe o seu palpite: '))

    if palpite == sorteio:
        acertou = True
        print(f'Parabéns! Você acertou em {i} tentativas!')
        break
    else:
        print('Errooooouuuu! Tenta de novo, mané!')

        if palpite < sorteio:
            print('Chutou muito baixo!')
        else:
            print('Chutou muito alto!')


if not acertou:
    print(f'O número sorteado foi {sorteio}')
