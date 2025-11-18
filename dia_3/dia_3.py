### condicionais, if, else, elif, operadores lógicos, blocos de código, escopo, namespace global, namespace local. ###
# estrutura condicional simples (verificar se uma pessoa tem altura suficiente para entrar em um brinquedo  de parque de diversões)



### opção 1 - sem usar variáveis para armazenar os valores dos ingressos e fotos ###

print("Bem-vindo ao parque de diversões!")
idade = int(input("Digite sua idade: \n")) # recebendo a idade do usuário
if idade <= 12: # Se a idade for menor ou igual a 12
    print("Você é criança e seu ingresso custa $5.")
elif idade < 18: # Se a idade for menor que 18 (e maior que 12)
    print("Você é menor de idade e seu ingresso custa $7.")
else: # Se não for nenhuma das anteriores, é maior de 18
    print("Você é maior de idade e seu ingresso custa $14.")
    
quer_foto = input("Você quer incluir uma foto no brinquedo? (sim/não): \n").lower() # recebendo a resposta do usuário e convertendo para minúsculo
if quer_foto == "sim": # se a resposta for sim
    print("O valor da foto é $3.00")
    print("Aproveite o parque!")
    print("-------------------------------:)-------------------------------\n")
else: # se a resposta for não
    print("Aproveite o parque!")
    print("-------------------------------:)-------------------------------\n")
        
print("Para entrar no brinquedo, você precisa ter pelo menos 1.20 metros de altura.")
altura = float(input("Digite sua altura em metros, exemplo 1.75: \n")) # recebendo a altura do usuário em float
if altura >= 1.20: # if + condição
    print("Você tem altura suficiente para entrar no brinquedo!")
else: # else + bloco de código
    print("Desculpe, você não tem altura suficiente para entrar no brinquedo.")
    
  

    
### opção 2 - usando variáveis para armazenar os valores dos ingressos e fotos ###
   
print("Bem-vindo ao parque de diversões!")

# Cria uma variável para o valor do ingresso e inicia com 0
valor_ingresso = 0

idade = int(input("Digite sua idade: \n"))

if idade <= 12:
    print("Você é criança e seu ingresso custa $5.")
    valor_ingresso = 5 # Atribue o valor do ingresso à variável
elif idade < 18:
    print("Você é menor de idade e seu ingresso custa $7.")
    valor_ingresso = 7 # Atribue o valor do ingresso à variável
else:
    print("Você é maior de idade e seu ingresso custa $14.")
    valor_ingresso = 14 # Atribue o valor do ingresso à variável

# Cria uma variável para o valor da foto
valor_foto = 0
quer_foto = input("Você quer incluir uma foto no brinquedo? (sim/não): \n").lower()

if quer_foto == "sim":
    valor_foto = 3 # Atribua o valor da foto à variável
    print("O valor da foto é $3.00")

# Calcule o valor total somando as variáveis
valor_total = valor_ingresso + valor_foto
print(f"O valor total a pagar é: ${valor_total:.2f}\n")

print("-------------------------------:)-------------------------------\n")
print("Para entrar no brinquedo, você precisa ter pelo menos 1.20 metros de altura.")
altura = float(input("Digite sua altura em metros, exemplo 1.75: \n"))

if altura >= 1.20:
    print("Você tem altura suficiente para entrar no brinquedo! Divirta-se!")
else:
    print("Desculpe, você não tem altura suficiente para entrar no brinquedo. Tente outro brinquedo!")
    

# agora na mesma situação, se as 3 condiçoões forem testadas. Numa terceira hipotese de acrescentar $3 caso a pessoas queira uma foto no brinquedo.




### Modulo operador % (módulo) - retorna o resto da divisão entre dois números ###

verificar_numero_par_ou_impar = int(input("Digite um número inteiro para verificar se é par ou ímpar: \n")) # recebendo um número inteiro do usuário
if verificar_numero_par_ou_impar % 2 == 0: # se o resto da divisão por 2 for igual a 0, o número é par
    print(f"O número {verificar_numero_par_ou_impar} é par.") # imprime se for par
else:
    print(f"O número {verificar_numero_par_ou_impar} é ímpar.") # imprime for se ímpar




### Phyton Pizza ###
# Nesse bloco de código, criamos uma calculadora de pedidos de pizza. O usuário pode escolher o tamanho da pizza (P, M ou G), se quer adicionar pepperoni e/ou queijo extra. O valor total é calculado com base nas escolhas do usuário e exibido no final.
# Com o uso de condicionais (if, elif, else) e operadores lógicos, podemos determinar o preço final da pizza com base nas preferências do cliente.
# E o uso == e += que são operadores importantes para comparação e atribuição de valores em Python.

print("Bem-vindo à Python Pizza Delivery!")
tamanho = input("Qual tamanho de pizza você quer? (P/M/G): \n").upper() # recebendo o tamanho da pizza e convertendo para maiúsculo
pepperoni = input("Você quer pepperoni? (sim/não): \n").lower() # recebendo a resposta do usuário e convertendo para minúsculo
queijo_extra = input("Você quer queijo extra? (sim/não): \n").lower() # recebendo a resposta do usuário e convertendo para minúsculo
valor_pizza = 0 # inicializando a variável do valor da pizza
# condições para calcular o valor da pizza
if tamanho == "P": # se o tamanho for P / o operador == é um operador de comparação que verifica se os valores são iguais
    valor_pizza += 15 # adiciona 15 ao valor da pizza / o += é um operador de atribuição que adiciona o valor à variável
    if pepperoni == "sim": # se quiser pepperoni
        valor_pizza += 2 # adiciona 2 ao valor da pizza
    if queijo_extra == "sim": # se quiser queijo extra
        valor_pizza += 1 # adiciona 1 ao valor da pizza
elif tamanho == "M": # se o tamanho for M
    valor_pizza += 20 # adiciona 20 ao valor da pizza
    if pepperoni == "sim": # se quiser pepperoni
        valor_pizza += 3 # adiciona 3 ao valor da pizza
    if queijo_extra == "sim": # se quiser queijo extra
        valor_pizza += 1 # adiciona 1 ao valor da pizza
elif tamanho == "G": # se o tamanho for G
    valor_pizza += 25 # adiciona 25 ao valor da pizza
    if pepperoni == "sim": # se quiser pepperoni
        valor_pizza += 3 # adiciona 3 ao valor da pizza
    if queijo_extra == "sim": # se quiser queijo extra
        valor_pizza += 1 # adiciona 1 ao valor da pizza
print(f"O valor total da sua pizza é: ${valor_pizza}. Aproveite sua pizza!") # imprime o valor total da pizza




### Operadores False e True com and, or, not ###

### Exemplo com 'and' / Ele funciona assim: se ambas as condições forem verdadeiras, o resultado será verdadeiro. Se uma ou ambas as condições forem falsas, o resultado será falso. ###
print("--- Operador 'and' ---")

# Ambas as condições são True -> o resultado é True
condicao_1 = True
condicao_2 = True
print(f"True and True é: {condicao_1 and condicao_2}")

# Uma das condições é False -> o resultado é False
condicao_1 = True
condicao_2 = False
print(f"True and False é: {condicao_1 and condicao_2}")

# Ambas as condições são False -> o resultado é False
condicao_1 = False
condicao_2 = False
print(f"False and False é: {condicao_1 and condicao_2}")




### Exemplo com 'or' / Ele funciona assim: se uma ou ambas as condições forem verdadeiras, o resultado será verdadeiro. Se ambas as condições forem falsas, o resultado será falso. ###
print("\n--- Operador 'or' ---")

# Uma das condições é True -> o resultado é True
condicao_1 = True
condicao_2 = False
print(f"True or False é: {condicao_1 or condicao_2}")

# Ambas as condições são True -> o resultado é True
condicao_1 = True
condicao_2 = True
print(f"True or True é: {condicao_1 or condicao_2}")

# Ambas as condições são False -> o resultado é False
condicao_1 = False
condicao_2 = False
print(f"False or False é: {condicao_1 or condicao_2}")




### Exemplo com 'not' / Ele inverte o valor lógico da condição. Se a condição for True, o resultado será False, e vice-versa. ###
print("\n--- Operador 'not' ---")

# Inverte o valor True para False
condicao_1 = True
print(f"not True é: {not condicao_1}")

# Inverte o valor False para True
condicao_1 = False
print(f"not False é: {not condicao_1}")




### Exemplo combinado com 'and', 'or' e 'not' / Combina múltiplas condições usando os operadores lógicos. ###
print("\n--- Exemplo Combinado: Verificação de Login ---")

usuario_logado = True
tem_permissao = True
usuario_bloqueado = False

# Verificação: o usuário pode acessar se ele estiver logado E tiver permissão, E NÃO estiver bloqueado.
pode_acessar = usuario_logado and tem_permissao and (not usuario_bloqueado)
print(f"Pode acessar o sistema? {pode_acessar}")

# Verificação: o usuário pode entrar na festa se for maior de 18 OU tiver um convite.
idade_valida = False
tem_convite = True
pode_entrar_festa = idade_valida or tem_convite
print(f"Pode entrar na festa? {pode_entrar_festa}")




### voltando ao exemplo do parque de diversões, agora com operadores lógicos ###

print("Bem-vindo ao parque de diversões!")

#Cria uma variável para o valor do ingresso e inicia com 0
valor_ingresso = 0

idade = int(input("Digite sua idade: \n"))

if idade <= 12:
    print("Você é criança e seu ingresso custa $5.")
    valor_ingresso = 5 # Atribue o valor do ingresso à variável
elif idade >= 45 and idade <= 55: # Usando o operador lógico and para oferecer ingresso grátis para pessoas entre 45 e 55 anos
    print("Você tem entre 45 e 55 anos, seu ingresso é grátis!")
    valor_ingresso = 0 # Atribue o valor do ingresso à variável  
elif idade < 18:
    print("Você é menor de idade e seu ingresso custa $7.")
    valor_ingresso = 7 # Atribue o valor do ingresso à variável
else:
    print("Você é maior de idade e seu ingresso custa $14.")
    valor_ingresso = 14 # Atribue o valor do ingresso à variável

# Cria uma variável para o valor da foto
valor_foto = 0
quer_foto = input("Você quer incluir uma foto no brinquedo? (sim/não): \n").lower()

if quer_foto == "sim":
    valor_foto = 3 # Atribua o valor da foto à variável
    print("O valor da foto é $3.00")

# Calcule o valor total somando as variáveis
valor_total = valor_ingresso + valor_foto
print(f"O valor total a pagar é: ${valor_total:.2f}\n")

print("-------------------------------:)-------------------------------\n")
print("Para entrar no brinquedo, você precisa ter pelo menos 1.20 metros de altura.")
altura = float(input("Digite sua altura em metros, exemplo 1.75: \n"))

if altura >= 1.20:
    print("Você tem altura suficiente para entrar no brinquedo! Divirta-se!")
else:
    print("Desculpe, você não tem altura suficiente para entrar no brinquedo. Tente outro brinquedo!")
    

#agora na mesma situação, se as 3 condiçoões forem testadas. Numa terceira hipotese de acrescentar $3 caso a pessoas queira uma foto no brinquedo.
