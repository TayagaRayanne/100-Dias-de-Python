### Projeto Gerador de Senhas ###

# O código abaixo gera uma senha aleatória com base nas preferências do usuário em relação ao número de letras, símbolos e números que ele deseja na senha.
# Ele faz uso da biblioteca random para selecionar caracteres aleatórios e embaralhar a ordem dos caracteres na senha final.
# A senha gerada é então exibida ao usuário.

# Primeiro, o código importa a biblioteca random, que é essencial para gerar números e escolhas aleatórias.
# Em seguida, ele define três listas: letters, numbers e symbols, que contêm os caracteres que podem ser usados na senha.
# O usuário é então solicitado a inserir o número desejado de letras, símbolos e números para a senha.
# Usando o k=parâmetro da função random.choices(), o código seleciona aleatoriamente o número especificado de caracteres de cada lista.
# O código usa random.choices() para selecionar aleatoriamente o número especificado de letras, símbolos e números das listas correspondentes.
# Essas escolhas são combinadas em uma única lista chamada password.
# A lista password é então embaralhada usando random.shuffle() para garantir que a ordem dos caracteres seja aleatória.
# Finalmente, a lista embaralhada é convertida em uma string usando "".join() e exibida ao usuário como a senha gerada.

# O Código está em inglês por que o curso original é nessa língua e alguns códigos devem ser entregues na IDE virtual em inglês.

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = random.choices(letters, k=nr_letters) + random.choices(symbols, k=nr_symbols) + random.choices(numbers, k=nr_numbers) # o K= é a quantidade de itens que queremos escolher, quantidade de letras, simbolos e numeros.
random.shuffle(password)

print(f"Your password is {''.join(password)}")

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P