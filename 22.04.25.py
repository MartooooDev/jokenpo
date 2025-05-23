# --------------------------------------------------
# Trabalho da disciplina de Raciocínio Algorítmico
# Pedra, papel, tesoura
#
# Data: 16/04/2025
# --------------------------------------------------

import random
import os
from time import sleep

#Início do jogo
print('Bem-vindo ao Jokenpo!')
exit = 0
sleep(1)

#Apresentação das opções
while exit != 1:
<<<<<<< HEAD

=======
    os.system('cls' if os.name == 'nt' else 'clear') #No Linux o comando é diferente (Martin usando Ubuntu)
>>>>>>> 22b5e1af99c7e56707862b442cdfeb86ff2e6186

    continuar = 0
    pontuacao_j1 = 0
    pontuacao_j2 = 0
    
    #Menu principal apresentado no começo do programa
    print('Selecione uma opção para jogar: ')
    print('1- Jogador VS Jogador')
    print('2- Jogador VS Computador')
    print('3- Computador VS Computador')
    print('4- Sair')

    print('+' + '-' * 30 + '+')

    #Validadores de entrada, p/ garantir q usuário insira valores váliodos
    opcao = 0
    while opcao < 1 or opcao > 4:
        opcao = int(input('Sua escolha: '))
        if opcao < 1 or opcao > 4:
            print("*Opção inválida. Escolha entre 1 e 4.*")
    print('+' + '-' * 30 + '+')
    
    #Saída do programa
    if opcao == 4:
        print('Saindo do jogo...')
        sleep(1)
        print('Programa feito por Elgson Nascimento, Martin Romão e Maria Pietra.')
        print('Obligado por jogar com a gente!')
        sleep(1)
        exit = 1
        break

    #Entrada de nomes antes do loop da rejogabilidade, para não precisar ficar inserindo toda vez, e ficar mais fácil de mostrar no placar
    if opcao == 1 :
        nome_j1 = input("Digite o nome do jogador 1:\n")
        nome_j2 = input("Digite o nome do jogador 2:\n")
    elif opcao == 2:
        nome_j1 = input("Digite o nome do jogador 1:\n")
        nome_j2 = 'COM'
    elif opcao == 3 :
        nome_j1 = 'COM1'
        nome_j2 = 'COM2'

    #Loop de rejogabilidade
    while continuar != 2:
        #Jogador VS Jogador
        if opcao == 1:
            print('Você selecionou Jogador vs Jogador')
            print('+' + '-' * 30 + '+')
            print('Caso não estejam cientes das regras, aqui está um resumo simples: ')
            print('Pedra ganha de Tesoura')
            print('Tesoura ganha de Papel')
            print('Papel ganha de Pedra')
            print('+' + '-' * 30 + '+')

            print(f'{nome_j1}, {nome_j2}, prazer em tê-los aqui!')
            print('Vamos começar o jogo!')
            print('+' + '-' * 30 + '+')

# INÍCIO DO BLOCO DE ESCOLHA DO JOGADOR 1  
            print('1- Pedra')
            print('2- Papel')
            print('3- Tesoura\n')
                                              
            escolha_j1 = 0                                                                          
            while escolha_j1 < 1 or escolha_j1 > 3:
                escolha_j1 = int(input(f'{nome_j1}, Escolha uma das opções (1, 2 ou 3): '))
                if escolha_j1 < 1 or escolha_j1 > 3:
                    print("*Número inválido. Escolha 1, 2 ou 3.*")

            if escolha_j1 == 1:
                escolha_j1_convertido = "Pedra"
            elif escolha_j1 == 2:
                escolha_j1_convertido = "Papel"
            else:
                escolha_j1_convertido = "Tesoura"

# FIM DO BLOCO DE ESCOLHA DO JOGADOR 1  
            print('+' + '-' * 30 + '+')
# INÍCIO DO BLOCO DE ESCOLHA DO JOGADOR 2  
            print('\n\n1- Pedra')
            print('2- Papel')
            print('3- Tesoura\n')

            escolha_j2 = 0
            while escolha_j2 < 1 or escolha_j2 > 3:
                escolha_j2 = int(input(f'{nome_j2}, Escolha uma das opções (1, 2 ou 3):'))
                if escolha_j2 < 1 or escolha_j2 > 3:
                    print("*Número inválido. Escolha 1, 2 ou 3.*")

            if escolha_j2 == 1:
                escolha_j2_convertido = "Pedra"
            elif escolha_j2 == 2:
                escolha_j2_convertido = "Papel"
            else:
                escolha_j2_convertido = "Tesoura"

# FIM DO BLOCO DE ESCOLHA DO JOGADOR 2
# INÍCIO DO BLOCO DE RESULTADO DA RODADA

            sleep(2)
            print('+' + '-' * 30 + '+')
            print(f'| {"ESCOLHAS DA RODADA":^28} |')
            print('+' + '-' * 30 + '+')
            print(f'| {nome_j1:^10} | {nome_j2:^10} |')
            print('+' + '-' * 30 + '+')
            print(f'| {escolha_j1_convertido:^10} | {escolha_j2_convertido:^10} |')
            print('+' + '-' * 30 + '+')
            sleep(2)

            if escolha_j1 == escolha_j2:
                sleep(1), print('.'), sleep(1), print('.')
                print('Empate!')
                sleep(2)
            elif (escolha_j1 == 1 and escolha_j2 == 2) or (escolha_j1 == 2 and escolha_j2 == 3) or (escolha_j1 == 3 and escolha_j2 == 1):
                sleep(1), print('.'), sleep(1), print('.')
                print(f'{nome_j2} ganhou!')
                sleep(2)
                pontuacao_j2 += 1
            else:
                sleep(1), print('.'), sleep(1), print('.')
                print(f'{nome_j1} ganhou!')
                sleep(2)
                pontuacao_j1 += 1

# FIM DO BLOCO DE RESULTADO DA RODADA
# Escolha de continuar o jogo ou não; se escolher 2, quebra o loop de continuar e mostra o placar final
            continuar = 0
            while continuar < 1 or continuar > 2:
                continuar = int(input("Deseja continuar? \n1- Sim\n2- Não\n"))
                if continuar < 1 or continuar > 2:
                    print("*Opção inválida. Escolha 1 ou 2.*")

        # Jogador VS COMPUTADOR
        if opcao == 2:
            print("Você selecionou o modo Jogador vs Computador!\n")

            print(f'{nome_j1}, {nome_j2}, prazer em tê-los aqui!')
            print('Vamos começar o jogo!')
            print('+' + '-' * 30 + '+')

            print('1- Pedra')
            print('2- Papel')
            print('3- Tesoura\n')

            escolha_jogador = 0
            while escolha_jogador < 1 or escolha_jogador > 3:
                escolha_jogador = int(input("Escolha uma das opções (1, 2 ou 3): "))
                if escolha_jogador < 1 or escolha_jogador > 3:
                    print("*Número inválido. Escolha 1, 2 ou 3.*")

            if escolha_jogador == 1:
                escolha_jogador_convertido = "Pedra"
            elif escolha_jogador == 2:
                escolha_jogador_convertido = "Papel"
            else:
                escolha_jogador_convertido = "Tesoura"

# INÍCIO DO BLOCO DE ESCOLHA DO COMPUTADOR
            escolha_computador = random.randint(1, 3)

            if escolha_computador == 1:
                escolha_computador_convertido = "Pedra"
            elif escolha_computador == 2:
                escolha_computador_convertido = "Papel"
            else:
                escolha_computador_convertido = "Tesoura"
# FIM DO BLOCO DE ESCOLHA DO COMPUTADOR

            sleep(2)
            print('+' + '-' * 30 + '+')
            print(f'| {"ESCOLHAS DA RODADA":^28} |')
            print('+' + '-' * 30 + '+')
            print(f'| {nome_j1:^10} | {nome_j2:^10} |')
            print('+' + '-' * 30 + '+')
            print(f'| {escolha_jogador_convertido:^10} | {escolha_computador_convertido:^10} |')
            print('+' + '-' * 30 + '+')
            sleep(2)

            if escolha_jogador == escolha_computador:
                sleep(1), print('.'), sleep(1), print('.')
                print('Empate!')
                sleep(2)
            elif (escolha_jogador == 1 and escolha_computador == 2) or \
                (escolha_jogador == 2 and escolha_computador == 3) or \
                (escolha_jogador == 3 and escolha_computador == 1):
                sleep(1), print('.'), sleep(1), print('.')
                print("Você venceu esta rodada!")
                sleep(2)
                pontuacao_j1 += 1
            else:
                sleep(1), print('.'), sleep(1), print('.')
                print("O computador venceu esta rodada!")
                sleep(2)
                pontuacao_j2 += 1

            print("-" * 25)

            continuar = 0
            while continuar < 1 or continuar > 2:
                continuar = int(input("Deseja continuar? \n1- Sim\n2- Não\n"))
                if continuar < 1 or continuar > 2:
                    print("*Opção inválida. Escolha 1 ou 2.*")
                
        # COMPUTADOR VS COMPUTADOR
        if opcao == 3:
            print("Você selecionou o modo Computador vs Computador!\n")

            print(f'{nome_j1}, {nome_j2}, prazer em tê-los aqui!')
            print('Vamos começar o jogo!')
            print('+' + '-' * 30 + '+')
            escolha_cpu1 = random.randint(1, 3)  
            
            if escolha_cpu1 == 1:
                escolha_cpu1_convertido = "Pedra"
            elif escolha_cpu1 == 2:
                escolha_cpu1_convertido = "Papel"
            else:
                escolha_cpu1_convertido = "Tesoura"


            escolha_cpu2 = random.randint(1, 3) 

            if escolha_cpu2 == 1:
                escolha_cpu2_convertido = "Pedra"
            elif escolha_cpu2 == 2:
                escolha_cpu2_convertido = "Papel"
            else:
                escolha_cpu2_convertido = "Tesoura"

            sleep(2)
            print('+' + '-' * 30 + '+')
            print(f'| {"ESCOLHAS DA RODADA":^28} |')
            print('+' + '-' * 30 + '+')
            print(f'| {nome_j1:^10} | {nome_j2:^10} |')
            print('+' + '-' * 30 + '+')
            print(f'| {escolha_cpu1_convertido:^10} | {escolha_cpu2_convertido:^10} |')
            print('+' + '-' * 30 + '+')
            sleep(2)

            if escolha_cpu1 == escolha_cpu2:
                sleep(1), print('.'), sleep(1), print('.')
                print("Empate!")
                sleep(2)
            elif (escolha_cpu1 == 1 and escolha_cpu2 == 2) or \
                (escolha_cpu1 == 2 and escolha_cpu2 == 3) or \
                (escolha_cpu1 == 3 and escolha_cpu2 == 1):
<<<<<<< HEAD
                input("cpu 1 venceu!: Pressione enter...")
                pontuacao_j1 += 1;
            else:
                input("cpu 2 venceu!: Pressione enter...")
                pontuacao_j2 += 1;

            continuar = int(input("Deseja continuar? \n1- Sim\n2- Não: "))

        
        else:
            print('Opção inválida! Digite um valor válido.');
            break;
=======
                sleep(1), print('.'), sleep(1), print('.')
                print("cpu 2 venceu!")
                sleep(2)
                pontuacao_j2 += 1
            else:
                sleep(1), print('.'), sleep(1), print('.')
                print("cpu 1 venceu!")
                sleep(2)
                pontuacao_j1 += 1

            continuar = 0
            while continuar < 1 or continuar > 2:
                continuar = int(input("Deseja continuar? \n1- Sim\n2- Não\n"))
                if continuar < 1 or continuar > 2:
                    print("*Opção inválida. Escolha 1 ou 2.*")
>>>>>>> 22b5e1af99c7e56707862b442cdfeb86ff2e6186

# INICIO DO BLOCO DE RESULTADO FINAL
    if continuar == 2:
        # Aqui a pontuação acumulada em todas as rodadas será mostrada após o input de 'continuar' ser 2
        print('Você selecionou a opção de parar de jogar.\n')
        sleep(2)
        print('+' + '-' * 30 + '+')
        print(f'| {"PLACAR FINAL":^28} |')
        print('+' + '-' * 30 + '+')
        print(f'| {nome_j1:^12} | {nome_j2:^12} |')
        print('+' + '-' * 30 + '+')
        print(f'| {pontuacao_j1:^12} | {pontuacao_j2:^12} |')
        print('+' + '-' * 30 + '+')
        sleep(2)
        input('Pressione ENTER para voltar ao menu principal...')
        # Após essa mensagem, o programa voltará ao menu principal
