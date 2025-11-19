### Funções com Output ###
# São funções que retornam um valor após sua execução.
# Utilizamos a palavra reservada 'return' para isso.
# Elas podem retornar qualquer tipo de dado: números, strings, listas, dicionários, etc.

def format_name(f_name, l_name): # Função que formata o nome com a primeira letra maiúscula
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}" # Retorna o nome completo formatado

formated_string = format_name("tAYga", "rAYANNE") # Chamada da função
print(formated_string)  # Output: Tayga Rayanne


# Outra forma de fazer a mesma função:

def format_name(f_name, l_name): # Função que formata o nome com a primeira letra maiúscula
    if f_name == "" or l_name == "":  # Verifica se algum dos nomes está vazio (Se f_name ou l_name for igual a "vazio", retorne "Você esqueceu de digitar o nome ou sobrenome.")
        return "Você esqueceu de digitar o nome ou sobrenome."  # Retorna uma mensagem de erro
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Resultado: {formated_f_name} {formated_l_name}" # Retorna o nome completo formatado

print(format_name(input("Qual o seu primeiro nome? "), input("Qual é o seu sobrenome? ")))  # Chamada da função e output direto


# Docstring
# São strings de documentação que explicam o propósito de uma função.
# Elas são escritas logo após a definição da função, entre aspas triplas.

def format_name(f_name, l_name):
    """Recebe um nome e um sobrenome e os formata
para retornar a versão do nome em maiúsculas apenas no início."""
    if f_name == "" or l_name == "":
        return "Você esqueceu de digitar o nome ou sobrenome."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Resultado: {formated_f_name} {formated_l_name}"
print(format_name(input("Qual o seu primeiro nome? "), input("Qual é o seu sobrenome? ")))
# A docstring acima explica o que a função faz, facilitando o entendimento para quem for ler o código depois.