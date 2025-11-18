### Funções com inputs ###

# def greet():
#     print("Hello!")
#     print("How do you do?")
#     print("Isn't the weather nice?")
    
# greet()

# def greet_with_name(name):
#     print(f"Hello {name}!")
#     print(f"How do you do {name}?")
    
# greet_with_name("Tay")

### qual a diferença entre parâmetros e argumentos? ###
# Parâmetros são os nomes usados na definição da função, enquanto argumentos são os valores reais passados para a função quando ela é chamada. 


### Funções com mais de um input ###

def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"What is it like in {location}?")
    
greet_with("Tay", "Brazil") # Argumentos posicionais é quando a ordem importa
greet_with(location="Brazil", name="Tay")  # Argumentos nomeados é quando a ordem não importa

# Keyword Arguments - Argumentos nomeados #
# Ao usar argumentos nomeados, você pode passar os argumentos em qualquer ordem, desde que você especifique o nome do parâmetro.
# Isso torna o código mais legível e menos propenso a erros relacionados à ordem dos argumentos.
### Desafio ###
# Crie uma função que gere senhas aleatórias com base em critérios fornecidos pelo usuário
greet_with(name="Angela", location="London")
