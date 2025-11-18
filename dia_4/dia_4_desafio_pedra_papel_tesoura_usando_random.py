### Pedra, Papel e Tesoura ###
# Neste desafio, foi criado um jogo simples de Pedra, Papel e Tesoura contra o computador.
# O usuário escolherá entre "pedra", "papel" ou "tesoura", e o computador fará uma escolha aleatória.
# O programa determinará o vencedor com base nas regras do jogo:
# - Pedra ganha de Tesoura
# - Tesoura ganha de Papel
# - Papel ganha de Pedra
# - Se ambos escolherem a mesma opção, é um empate.

import random
pedra = "pedra"
papel = "papel"
tesoura = "tesoura"

print("Bem vindo ao jogo de Pedra, Papel e Tesoura!")  
user_choice = input("Escolha pedra, papel ou tesoura:\n").lower() # O user_choice é uma variável que armazena a escolha do usuário. Converte a entrada do usuário para minúsculas
while user_choice not in [pedra, papel, tesoura]: # Verifica se a escolha do usuário é válida com um ENQUANTO. O not in verifica se o valor não está na lista
    user_choice = input("Escolha inválida. Por favor, escolha pedra, papel ou tesoura:\n").lower() # Solicita uma nova escolha se a anterior for inválida
computer_choice = random.choice([pedra, papel, tesoura]) # Escolhe aleatoriamente entre pedra, papel ou tesoura para o computador
print(f"Você escolheu: {user_choice}") # Exibe a escolha do usuário
print(f"O computador escolheu: {computer_choice}") # Exibe a escolha do computador

# Determina o vencedor com base nas regras do jogo
if user_choice == computer_choice: # Verifica se houve empate com um SE
    print("Empate!")
elif (user_choice == pedra and computer_choice == tesoura) or \
     (user_choice == papel and computer_choice == pedra) or \
     (user_choice == tesoura and computer_choice == papel): # Condições para o usuário ganhar
    print("Você ganhou!")
else: # Se não for empate e o usuário não ganhar, o computador vence.
    print("Você perdeu!")
