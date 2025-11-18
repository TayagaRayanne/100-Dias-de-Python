### Desafio Leilão as Cegas ###

# Neste desafio, você criará um programa de leilão as cegas.
# Um leilão as cegas é um tipo de leilão onde os licitantes não sabem as ofertas dos outros participantes.
# Seu programa deve permitir que vários usuários façam lances, armazenando seus nomes e valores
# em um dicionário. No final, o programa deve determinar o vencedor com o maior lance e exibir seu nome e valor.


import os
import art


# Função para limpar a tela do console no Windows para manter os lances ocultos.
def clear():
  if os.name == 'nt':
    os.system('cls')

print(art.logo)


# Dicionário para armazenar os lances dos licitantes
bids = {}
bidding_finished = False


# Função para encontrar o licitante com o maior lance no dicionário de lances.
def find_highest_bidder(bidding_record):
  """Encontra o licitante com o lance mais alto."""
  highest_bid = 0
  winner = ""
  
  # Itera sobre o dicionário de lances
  for bidder, bid_amount in bidding_record.items(): # Percorre cada par chave-valor no dicionário
    if bid_amount > highest_bid: # Compara o lance atual com o maior lance registrado
      highest_bid = bid_amount
      winner = bidder
  
  # Exibe o resultado do leilão    
  print(f"\n-------- Resultado do Leilão --------\n")
  print(f"🏆 Parabéns, {winner}! Você venceu o leilão com um lance de R${highest_bid:.2f}") # Formata o resultado para exibir o valor como moeda com duas casas decimais



# Loop principal do leilão.
while not bidding_finished:
  name = input("Qual é o seu nome?: ")
  
  # Garante que o lance é um valor numérico válido
  while True: # Loop até que um valor válido seja inserido
    try: # Tenta converter a entrada para float
      price = float(input("Qual é o seu lance?: R$"))
      break
    except ValueError: # Captura o erro se a conversão falhar
      print("❌ Por favor, insira um valor numérico válido para o lance.") 
      
  bids[name] = price # Adiciona o nome e o lance ao dicionário de lances. Ele está fora do loop para garantir que só valores válidos sejam armazenados.
  
  # Aceita "sim" ou "yes" e "não" ou "no" (em maiúsculas ou minúsculas)
  should_continue = input("Há mais um licitante (Pessoa a dar um lance)? Digite 'sim' ou 'não'.\n").lower()
  
  # Verifica a resposta do usuário para continuar ou finalizar o leilão.
  if should_continue in ("não", "nao", "no"):
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue in ("sim", "yes"):
    clear() # Chama a função que limpa a tela para o próximo licitante não ver os lances anteriores.
  else:
    print("⚠️ Opção inválida. Continuando o leilão para o próximo licitante.")
    clear() # Chama novamente a função de limpar a tela.