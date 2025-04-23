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

    #Sair
    if opcao == 4:
        print('Saindo do jogo...');
        sleep(1);
        exit = 1;
        break;
    else:
        print('Opção inválida! Digite um valor válido.');