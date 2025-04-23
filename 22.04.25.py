jogador_humano1 = input("Digite seu nome: ")
jogar = int(input("Você gostaria de jogar jokenpo?\nPara jogar digite 1, para não jogar digite 2: "))

if jogar == 1:
    print(f"Parabéns {jogador_humano1}, você vai jogar!")
    print("\n-------(1)jogador vs jogador-------\n-------(2)jogador vs maquina-------\n-------(3)maquina vs maquina-------\n--------------(4)sair--------------")
    jogar2 = int(input("Gostaria de jogar quais modos do jokenpo?\n1, 2, 3 ou 4?: "))

    if jogar2 == 1:
        print("jogador vs jogador")
    elif jogar2 == 2:
        print("jogador vs maquina")
    elif jogar2 == 3:
        print("maquina vs maquina")
    elif jogar2 == 4:
        print("Saindo do jogo...")
    else:
        print("Opção inválida. Escolha 1, 2, 3 ou 4.")
elif jogar == 2:
    print("Parece que você não quer jogar")
else:
    print("Opção inválida. Digite 1 para jogar ou 2 para sair.")