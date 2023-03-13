import random
import time

jogadas=['pedra','papel','tesoura']
def jogo():
    try:
        escolha= ['']
        while escolha:
            escolha =input(['pedra', 'papel', 'tesoura'])
            if escolha == 'pedra' or escolha == 'papel' or escolha == 'tesoura':
                break

    finally:
        pc=random.choice(jogadas)
        print(pc)
        time.sleep(1)
        if pc == 'pedra' and escolha == 'papel':
            print ('Você ganhou :)')
        elif pc == 'pedra' and escolha =='tesoura':
            print ('Haha! Você perdeu :P Mais sorte da próxima vez')
        elif pc == 'pedra' and escolha == 'pedra':
            print('Empate! Você até que não é ruim')
        elif pc == 'papel' and escolha == 'papel':
            print('Empate! Você até que não é ruim')
        elif pc == 'papel' and escolha == 'pedra':
            print ('Haha! Você perdeu :P Mais sorte da próxima vez')
        elif pc == 'papel' and escolha == 'tesoura':
            print ('Você ganhou :)')
        elif pc == 'tesoura' and escolha == 'pedra':
            print ('Você ganhou :)')
        elif pc == 'tesoura' and escolha == 'papel':
            print ('Haha! Você perdeu :P Mais sorte da próxima vez')
        elif pc == 'tesoura' and escolha == 'tesoura':
            print('Empate! Você até que não é ruim')
        novo = input('Pressione qualquer tecla para jogar novamente: ')
        if novo != '' or novo == '':
            print(jogo())

jogo()