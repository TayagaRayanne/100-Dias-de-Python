### Funções em python e Karel ###

print("Hello World!")
num_char = len("Hello World!")
print(num_char)

def my_function(): # define a função e da nome a ela
    print("Hello")
    print("Bye")
    
    
    
    
### Indentação em Python ###
# A indentação em Python é feita com 4 espaços ou uma tabulação.
# A indentação é usada para definir blocos de código, como o corpo de uma função
# ou o corpo de uma estrutura condicional.
# Cada espaço representa um nível de indentação e se refere a um bloco de código.

def my_function(): # chama a função para ser executada
    if 3 > 2: # o if está indentado dentro da função
        print("Yes") # esta linha está indentada dentro do bloco if e dentro da função
    else: # o else também está indentado dentro da função
        print("No") # esta linha está indentada dentro do bloco else e dentro da função
my_function() # esta linha não está indentada, então está fora da função





### Laços de repetição ###
# For e While #
# Este exemplo abaixo é um laço for que repete a ação de pular 6 vezes de um joguinho chamado Karel.
# O codigo está aqui para servir como anotação para o desafio do dia 6, que fiz na Reeborgs World.

turn_left = lambda: None  # Placeholder for the turn_left function
move = lambda: None       # Placeholder for the move function

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for step in range(6):
    jump()

number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
    print(number_of_hurdles)
    
