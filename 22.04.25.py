# --------------------------------------------------
# Trabalho da disciplina de Raciocínio Algorítmico
# Pedra, papel, tesoura;
#
# Data: 16/04/2025
# --------------------------------------------------
import random
import os
from time import sleep

#Início do jogo
print('Bem-vindo ao Jokenpo!');
exit = 0;

#Apresentação das opções
while exit != 1:
    sleep(2)
    os.system('cls')

    continuar = 0;
    pontuacao_j1 = 0;
    pontuacao_j2 = 0;
    
    print('Selecione uma opção para jogar: ');
    print('1- Jogador VS Jogador');
    print('2- Jogador VS Computador');
    print('3- Computador VS Computador');
    print('4- Sair');

    print('----------------------------------');
    opcao = int(input('Sua escolha: '));
    print('----------------------------------');

    if opcao != 3 :
        nome_j1 = input("Digite o nome do jogador 1:\n")
        if (opcao == 1):
            nome_j2 = input("Digite o nome do jogador 2:\n")

    while continuar != 2:
        #Jogador VS Jogador
        if opcao == 1:
            print('Você selecionou Jogador VS Jogador');
            print('-------------------------------------\n');
            print('Caso não estejam cientes das regras, aqui está um resumo simples: ')
            print('Pedra ganha de Tesoura');
            print('Tesoura ganha de Papel');
            print('Papel ganha de Pedra');
            print('-------------------------------------\n');

            print('Vamos lá!');
            print(f'{nome_j1}, {nome_j2}, prazer em tê-los aqui!');
            print('Vamos começar o jogo!');
            print('-------------------------------------\n');

            print(f'{nome_j1}, escolha uma das opções:')
            print('1- Pedra');
            print('2- Papel');
            print('3- Tesoura\n');

            escolha_j1 = int(input(''));

            print(f'{nome_j2}, escolha uma das opções:')
            print('1- Pedra');
            print('2- Papel');
            print('3- Tesoura\n');

            escolha_j2 = int(input(''));

            print('-------------------------------------\n');
            print( '|       J1       |       J2       \n')
            print(f'|       {escolha_j1}        X       {escolha_j2}       \n')
            print('-------------------------------------\n');

            if escolha_j1 == escolha_j2:
                sleep(1), print('.'), sleep(1), print('.'), sleep(1), print('.')
                print('Empate!');
            elif (escolha_j1 == 1 and escolha_j2 == 2) or (escolha_j1 == 2 and escolha_j2 == 3) or (escolha_j1 == 3 and escolha_j2 == 1):
                sleep(1), print('.'), sleep(1), print('.'), sleep(1), print('.')
                input(f'{nome_j2} ganhou!');
                pontuacao_j2 += 1;
            else:
                sleep(1), print('.'), sleep(1), print('.'), sleep(1), print('.')
                input(f'{nome_j1} ganhou!');
                pontuacao_j1 += 1;
                
            continuar = int(input("Deseja continuar? \n1- Sim\n2- Não"))

    
        #Jogador VS COMPUTADOR
        if opcao == 2:
            print("Modo: Jogador vs Computador Selecionado!\n")

            # Loop das partidas dentro do modo JvC
            while True:
                print(f"\n--- Placar: Jogador {pontuacao_j1} x {pontuacao_j2} Computador ---")
                print("Opções: 1: Pedra | 2: Tesoura | 3: Papel")

                # Obter jogada do jogador (número) com validação
                escolha_jogador_num = 0
                # Validação usa a lista [1, 2, 3] diretamente, não 'opcoes_jogo'
                while escolha_jogador_num not in [1, 2, 3]:
                    try:
                        entrada_jogador = input("Sua escolha (1, 2 ou 3): ").strip()
                        if entrada_jogador: # Verifica se não está vazio
                            escolha_jogador_num = int(entrada_jogador)
                            if escolha_jogador_num not in [1, 2, 3]:
                                print("   *Número inválido. Escolha 1, 2 ou 3.*")
                        else:
                            print("   *Entrada vazia. Escolha 1, 2 ou 3.*")
                    except ValueError:
                        print("   *Entrada inválida. Por favor, digite um NÚMERO (1, 2 ou 3).*")


                # Gerar jogada do computador (número)
                escolha_computador_num = random.randint(1, 3) # <<< Precisa do 'import random'

                # Converter número da escolha do jogador para nome
                if escolha_jogador_num == 1:
                    nome_jogador = "Pedra"
                elif escolha_jogador_num == 2:
                    nome_jogador = "Tesoura"
                else: # Se não for 1 ou 2, só pode ser 3
                    nome_jogador = "Papel"

                # Converter número da escolha do computador para nome
                if escolha_computador_num == 1:
                    nome_computador = "Pedra"
                elif escolha_computador_num == 2:
                    nome_computador = "Tesoura"
                else: # Se não for 1 ou 2, só pode ser 3
                    nome_computador = "Papel"

                # Mostrar as escolhas com nomes
                print(f"\nVocê escolheu: {nome_jogador}")
                print(f"Computador escolheu: {nome_computador}")

                # Lógica do Jokenpô usando os números (1:Pedra, 2:Tesoura, 3:Papel)
                if escolha_jogador_num == escolha_computador_num:
                    print("Resultado: Empate!")
                elif (escolha_jogador_num == 1 and escolha_computador_num == 2) or \
                    (escolha_jogador_num == 2 and escolha_computador_num == 3) or \
                    (escolha_jogador_num == 3 and escolha_computador_num == 1):
                    print("Resultado: Você venceu esta rodada!")
                    pontuacao_j1 += 1
                else:
                    print("Resultado: Computador venceu esta rodada!")
                    pontuacao_j2 += 1

                print("-" * 25) # Separador

                # Perguntar se quer continuar neste modo
                continuar_neste_modo = ""
                while continuar_neste_modo not in ['s', 'n']:
                    continuar_neste_modo = input("Jogar outra partida neste modo? (s/n): ").lower().strip()
                    if continuar_neste_modo not in ['s', 'n']:
                        print("   *Digite 's' para sim ou 'n' para não.*")

                # Se não quer continuar, volta ao menu principal
                if continuar_neste_modo == 'n':
                    print("\nVoltando ao menu principal...")
                    sleep(1.5) # <<< Precisa do 'import time'
                    break # Sai do loop de partidas (JvC)

                # Se digitou 's', o loop continua para a próxima rodada
                os.system('cls' if os.name == 'nt' else 'clear') # <<< Precisa do 'import os'

            continuar = int(input("Deseja continuar? \n1- Sim\n2- Não"))
                
    #COM VS COM
        if opcao == 3:
            print("cpu vs cpu")
            escolha_cpu1 = random.randint(1, 3)  
            escolha_cpu2 = random.randint(1, 3) 

            if escolha_cpu1 == 1:
                nome_cpu1 = "Pedra"
            elif escolha_cpu1 == 2:
                nome_cpu1 = "Tesoura"
            else:
                nome_cpu1 = "Papel"

            if escolha_cpu2 == 1:
                nome_cpu2 = "Pedra"
            elif escolha_cpu2 == 2:
                nome_cpu2 = "Tesoura"
            else:
                nome_cpu2 = "Papel"

            print(f"cpu 1 escolheu: {nome_cpu1}")
            print(f"cpu 2 escolheu: {nome_cpu2}")

            # Lógica do Jokenpô
            if escolha_cpu1 == escolha_cpu2:
                print("Empate!")
            elif (escolha_cpu1 == 1 and escolha_cpu2 == 2) or \
                (escolha_cpu1 == 2 and escolha_cpu2 == 3) or \
                (escolha_cpu1 == 3 and escolha_cpu2 == 1):
                input("cpu 1 venceu!")
                pontuacao_j1 += 1;
            else:
                input("cpu 2 venceu!")
                pontuacao_j2 += 1;

            continuar = int(input("Deseja continuar? \n1- Sim\n2- Não"))

        #Sair
        if opcao == 4:
            print('Saindo do jogo...');
            sleep(1);
            exit = 1;
            break;
        else:
            print('Opção inválida! Digite um valor válido.');
    
    print('Você selecionou a opção de parar de jogar.\n Pontuação final:\n');
    print('---------------')
    print('|  J1  |  J2  |')
    print(f'|   {pontuacao_j1}  |   {pontuacao_j2}  |')
    print('---------------')
