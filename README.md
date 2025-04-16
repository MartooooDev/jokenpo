# Jokenpo

Repositório para o código do jogo Jokenpo, trabalho da disciplina de Raciocínio Algorítmico.

## Como jogar

No Jokenpo, cada jogador escolhe uma opção entre pedra, papel e tesoura. Após ambos escolherem, devem revelar ao mesmo tempo sua escolha, e o ganhador será decidido com base em qual mão é mais forte, seguindo a seguinte ordem:

* Pedra ganha de Tesoura;
* Tesoura ganha de Papel;
* Papel ganha de pedra;

Caso os dois jogadores escolham a mesma opção na rodada, ocorrerá um empate, e haverá uma nova rodada para decidir o vencedor.

#### O Programa

Para jogar Jokenpo neste programa, o usuário deverá escolher uma opção entre três modos de jogo: JxJ (Jogador vs Jogador), JxCOM (Jogador vs Computador) e COMxCOM (Computador vs Computador).

Cada uma das entidades que participam do jogo tem um comportamento:

- Jogador:
  - Cada jogador incluído na partida terá seu nome solicitado, e, após todos os jogadores inserirem seus nomes, o jogo terá início.
  - No jogo, cada jogador terá oportunidade de digitar sua escolha entre 1 (Pedra), 2 (Papel) e 3 (Tesoura). Após a escolha de todos os jogadores, o programa automaticamente anunciará o resultado da partida, sendo empate ou vitória de algum participante da partida.
- Computador :
  - O Computador não tem um nome próprio, sendo apenas COM1 ou COM2.
  - No jogo, a escolha do computador é feita automaticamente por uma função random, que escolherá uma jogada aleatória ao(s) computador(es).
