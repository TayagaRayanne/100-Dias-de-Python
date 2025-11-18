### esta sessão é sobre print e input ###

print("lista de frutas:\nbanana\nmaçã\nlaranja")# \n é usado para pular linha

print("Hello!" + " Tayga")# concatenação de strings

input("Qual é o seu nome? ")# input sempre retorna uma string
print("Hello!" + " tayga")# concatenação de strings

print("Hello! " + input("Qual é o seu nome? ") + "!")# concatenação de strings com input




### esta sessão é sobre variáveis ###

nome = input("Qual é o seu nome? ")# input sempre retorna uma string
print("Hello! " + nome + "!")# concatenação de strings com input




### esta sessão é sobre funções len (ela não gosta de trabalhar com números inteiros dando um TypeError quando forçamos) ###

print(len(input("Qual é o seu nome? ")))# len conta o número de caracteres na string, incluindo espaços

username = input("Qual é o seu nome? ")# input sempre retorna uma string
length = len(username)# len conta o número de caracteres na string, incluindo espaços
print(length)# imprime o número de caracteres na string



# atividade da aula 1 com tudo que aprendemos no dia 1

print("Bem vindos ao Montando Sua Banda!")
cidade_natal = input("Qual é o nome da sua cidade natal?\n")
nome_do_animal_de_estimacao = input("Qual é o nome do seu animal de estimação?\n")
print("O nome da sua banda é " + cidade_natal + " " + nome_do_animal_de_estimacao + "!")

