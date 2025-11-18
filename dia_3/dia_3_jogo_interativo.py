print("Bem vindos a Ilha do Tesouro!")
print("Sua missão é encontrar o tesouro perdido.")

vitoria = (r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************
           ''')

# Salve a resposta do usuário na variável 'direcao'
direcao = input("Você está em uma encruzilhada. Para onde você quer ir?\nDigite esquerda ou direita.\n").lower()

if direcao == "esquerda":
    # Salve a próxima resposta na variável 'acao'
    acao = input("Você chegou a um lago. Há uma ilha no meio do lago.\nDigite 'esperar' para esperar por um barco. Digite 'nadar' para nadar até a ilha.\n").lower()
    if acao == "esperar":
        # Salve a resposta da cor na variável 'porta'
        porta = input("Você esperou e um barco chegou te levando até a ilha.\nAgora você encontrou uma casa com 3 portas. Uma vermelha, uma amarela e uma azul.\nQual cor você escolhe?\n").lower()
        if porta == "vermelha":
            print("Você foi queimado por fogo. Fim de jogo.")
        elif porta == "amarela":
            print("Você encontrou o tesouro! Você ganhou!")
            print(vitoria)
        elif porta == "azul":
            print("Você foi atacado por feras. Fim de jogo.")
        else:
            print("Você escolheu uma porta que não existe. Fim de jogo.")
    else:
        print("Você foi atacado por um jacaré. Fim de jogo.")
else:
    print("Você caiu em um buraco. Fim de jogo.")

### esta sessão é sobre tipos de dados ###
