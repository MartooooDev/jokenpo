import random

jogador_humano1 = input("Digite seu nome: ")
# jogador_humano2 = 
# cpu1 =
# cpu2 =
# pedra = 1 
# tesoura = 2
# papel = 3
jogar = int(input("Você gostaria de jogar jokenpo?\nPara jogar digite 1, para não jogar digite 2: "))

if jogar == 1:
    print(f"Parabéns {jogador_humano1}, você vai jogar!")
    print("\n-------(1)jogador vs jogador-------\n-------(2)jogador vs cpu-------\n-------(3)cpu vs cpu-------\n--------------(4)sair--------------")
    jogar2 = int(input("Gostaria de jogar quais modos do jokenpo?\n1, 2, 3 ou 4?: "))

    if jogar2 == 1:
        print("jogador vs jogador")
    elif jogar2 == 2:
        print("jogador vs cpu")
    elif jogar2 == 3:
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
        
    elif jogar2 == 4:
        print("Saindo do jogo...")
    else:
        print("Opção inválida. Escolha 1, 2, 3 ou 4.")
elif jogar == 2:
    print("Parece que você não quer jogar")
else:
    print("Opção inválida. Digite 1 para jogar ou 2 para sair.")
    
# pedra < papel, pedra = pedra, pedra > tesoura
# tesoura < pedra, tesoura = tesoura, tesoura > papel
# papel < tesoura, papel = papel, papel > pedra

