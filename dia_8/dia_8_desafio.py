### calculadora do amor ###
# Objetivo: Criar um programa que calcula a pontuação do amor entre duas pessoas com base nos seus nomes.

# Regras:
# 1. Combine os dois nomes em uma única string.
# 2. Conte o número de vezes que as letras da palavra "TRUE" aparecem na string combinada.
# 3. Conte o número de vezes que as letras da palavra "LOVE" aparecem na string combinada.
# 4. Combine os dois totais para criar uma pontuação de amor de dois dígitos.
# 5. Imprima a pontuação do amor com uma mensagem apropriada com base no valor da pontuação.

# Exemplo:
# Nome 1: "Kanye West"
# Nome 2: "Kim Kardashian"
# Pontuação do amor: 42

def calculate_love_score(name1, name2):
  # 1. Preparar os Nomes
  combined_names = name1 + name2
  lower_names = combined_names.lower()

  # 2. Calcular o Total de TRUE
  t = lower_names.count('t')
  r = lower_names.count('r')
  u = lower_names.count('u')
  e = lower_names.count('e')
  true_total = t + r + u + e

  # 3. Calcular o Total de LOVE
  l = lower_names.count('l')
  o = lower_names.count('o')
  v = lower_names.count('v')
  e2 = lower_names.count('e') # Note: O 'e' é contado novamente, pois é uma letra diferente na palavra LOVE! (aparece como e2)
  love_total = l + o + v + e2

  # 4. Combinar e Imprimir
  love_score_str = str(true_total) + str(love_total)
  love_score_int = int(love_score_str)

  print(love_score_int)

# Exemplo de Teste
calculate_love_score("Kanye West", "Kim Kardashian")

# Lógica do Programa:
# A função calculate_love_score combina os dois nomes, conta as letras relevantes para "TRUE" e "LOVE",
# e então combina esses totais para formar uma pontuação de amor de dois dígitos, que é então impressa.
# Você pode testar a função com diferentes nomes para ver como a pontuação do amor varia!
