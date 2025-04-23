# --------------------------------------------------
# Trabalho da disciplina de Raciocínio Algorítmico
# Pedra, papel, tesoura;
#
# Data: 16/04/2025
# --------------------------------------------------


import random
from time import sleep

#Início do jogo
print('Bem-vindo ao Jokenpo!');
exit = 0;

#Apresentação das opções
while opcao != 1:
    print('Selecione uma opção para jogar: ');
    print('1- Jogador VS Jogador');
    print('2- Jogador VS COM');
    print('3- COM VS COM');
    print('4- Sair');

    print('----------------------------------');
    opcao = int(input('Sua escolha: '));
    print('----------------------------------');

    #Jogador VS Jogador

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
            print("cpu 1 venceu!")
        else:
            print("cpu 2 venceu!")

    #Sair
    if opcao == 4:
        print('Saindo do jogo...');
        sleep(1);
        exit = 1;
        break;
    else:
        print('Opção inválida! Digite um valor válido.');