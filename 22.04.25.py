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
    sleep(3)
    os.system('cls')
    print('Selecione uma opção para jogar: ');
    print('1- Jogador VS Jogador');
    print('2- Jogador VS COM');
    print('3- COM VS COM');
    print('4- Sair');

    print('----------------------------------');
    opcao = int(input('Sua escolha: '));
    print('----------------------------------');

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
        print('Quem está jogando?');

        nome_j1 = input('Digite o nome do jogador 1: ');
        nome_j2 = input('Digite o nome do jogador 2: ');

        pontuacao_j1 = 0;
        pontuacao_j2 = 0;

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
        print(f'|       {escolha_j1}        |       {escolha_j2}       \n')
        print('-------------------------------------\n');

        if escolha_j1 == escolha_j2:
            sleep(1);
            print('.')
            sleep(1);
            print('.')
            sleep(1);
            print('.')
            print('Empate!');
        elif (escolha_j1 == 1 and escolha_j2 == 2) or (escolha_j1 == 2 and escolha_j2 == 3) or (escolha_j1 == 3 and escolha_j2 == 1):
            sleep(1);
            print('.')
            sleep(1);
            print('.')
            sleep(1);
            print('.')
            input(f'{nome_j2} ganhou!');
            pontuacao_j2 += 1;
        else:
            sleep(1);
            print('.')
            sleep(1);
            print('.')
            sleep(1);
            print('.')
            input(f'{nome_j1} ganhou!');
            pontuacao_j1 += 1;
            
    #Jogador VS COM

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
        else:
            input("cpu 2 venceu!")

    #Sair
    if opcao == 4:
        print('Saindo do jogo...');
        sleep(1);
        exit = 1;
        break;
    else:
        print('Opção inválida! Digite um valor válido.');