### Randomização ###
# é a geração de números aleatórios, que podem ser usados para criar jogos, simulações e outros programas que requerem elementos de sorte ou imprevisibilidade.

### é nescessário importar a biblioteca random para usar suas funções. ###
import random


# random_integer = random.randint(1, 10)  # Gera um número inteiro aleatório entre 1 e 10
# print(random_integer)
# random_float = random.random()  # Gera um número de ponto flutuante aleatório entre 0.0 e 1.0
# print(random_float)

# ndom_number_0_to_1 = random.random()  # Gera um número de ponto flutuante aleatório entre 0.0 e 1.0
# print(random_number_0_to_1)

# random_float = random.uniform(1, 10)  # Gera um número de ponto flutuante aleatório entre 0.0 e 5.0
# print(random_float)

# random_heads_or_tails = random.randint(0, 1)  # Gera 0 ou 1
# if random_heads_or_tails == 0:
#     print("Cara")
# else:
#     print("Coroa")



# escolhe um item aleatório de uma lista usanso choice(). O choice() é uma função da biblioteca random que seleciona um item aleatório de uma sequência (como uma lista ou uma tupla).

# state_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut"]
# random_state = random.choice(state_of_america)  # Escolhe um estado aleatório da lista
# print(random_state)

#para adicionar um item ao final da lista usamos append

# state_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut"]
# state_of_america.append("New York")  # Adiciona "New York" ao final da lista
# print(state_of_america)





# duas formas de escolher um nome aleatório de uma lista

# friends = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
# print(random.choice(friends))

# outra forma de fazer

# random_index = random.randint(0, len(friends) - 1)
# print(friends[random_index])






# esse exemplo usa len para descobrir o tamanho da lista

# state_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut"]
# print(len(state_of_america))
# # ou
# print(random.randint(0, len(state_of_america) - 1))

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes"]
# vegetables = ["Spinach", "Kale", "Celery", "Potatoes"]
# dirty_dozen = (fruits + vegetables)
# print(dirty_dozen)






# nesse exemplo substituímos o último item da lista e adicionamos um novo item ao final da lista:

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# fruits[-1] = "Melons"
# fruits.append("Lemons")
# print(fruits)

# nesse exemplo criamos uma lista dentro de outra lista:

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
 
# print(dirty_dozen[1][1])