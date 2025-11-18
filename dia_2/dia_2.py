### este bloco de código vai subscrição, extração,  concatenação, conversão e soma em strings. ###


print("Exemplo de subscrição e extração em números inteiros"[0]) # vai retornar o primeiro caractere da string #subscrição

print("Exemplo de subscrição e extração em números inteiros"[5]) # vai retornar o sexto caractere da string #subscrição

print("Hello"[4]) # vai retornar o quinto caractere da string #subscrição

print("123" + "345") # vai concatenar as duas strings #concatenação



### este bloco de código vai realizar operações matemáticas com números inteiros e de ponto flutuante, além de booleanos. ###


print(int("123") + int("345")) # vai converter as strings em inteiros e somar os valores #conversão e soma

print(int("123") + 345) # vai converter a string em inteiro e somar com o valor inteiro #conversão e soma

print("123" + str(345)) # vai converter o valor inteiro em string e concatenar com a string #conversão e concatenação

print(123 + 345) # vai somar os dois valores inteiros #soma

print(123_456_789) # vai retornar o número inteiro 123456789 (o underscore é ignorado) #número inteiro com underscore

print(3.1234) # vai retornar o número de ponto flutuante 3.1234 #número de ponto flutuante

#  print(true) # vai retornar o valor booleano True #booleano
#  print(False) # vai retornar o valor booleano False #booleano



### Tipos de dados e funções ###

print(type(123)) # vai retornar o tipo de dado do valor inteiro 123 #tipo de dado
print(type(3.1234)) # vai retornar o tipo de dado do valor de ponto flutuante 3.1234 #tipo de dado
print(type("Hello")) # vai retornar o tipo de dado da string "Hello" #tipo de dado
print(type(True)) # vai retornar o tipo de dado do valor booleano True #tipo de dado
print(type(False)) # vai retornar o tipo de dado do valor booleano False #tipo de dado

# #Type Casting é a conversão de um tipo de dado em outro tipo de dado.

print(str(123)) # vai converter o valor inteiro 123 em string #conversão
print(int("123")) # vai converter a string "123" em inteiro #conversão
print(float("3.1234")) # vai converter a string "3.1234" em ponto flutuante #conversão
print(int(3.1234)) # vai converter o valor de ponto flutuante 3.1234 em inteiro (3) #conversão
print(int(True)) # vai converter o valor booleano True em inteiro (1) #conversão
print(int(False)) # vai converter o valor booleano False em inteiro (0) #conversão
print(float(True)) # vai converter o valor booleano True em ponto flutuante (1.0) #conversão
print(float(False)) # vai converter o valor booleano False em ponto flutuante (0.0) #conversão
print(bool(1)) # vai converter o valor inteiro 1 em booleano (True) #conversão
print(bool(0)) # vai converter o valor inteiro 0 em booleano (False) #conversão
print(bool(123)) # vai converter o valor inteiro 123 em booleano (True) #conversão
print(bool("")) # vai converter a string vazia em booleano (False) #conversão
print(bool("Hello")) # vai converter a string "Hello" em booleano (True) #conversão
print(bool(3.1234)) # vai converter o valor de ponto flutuante 3.1234 em booleano (True) #conversão
print(bool(0.0)) # vai converter o valor de ponto flutuante 0.0 em booleano (False) #conversão


nome_do_usuario = input("Qual é o seu nome? ") # vai pedir para o usuário digitar o nome e armazenar na variável nome_do_usuario #input e variável
length_do_nome = len(nome_do_usuario) # vai calcular o tamanho do nome do usuário e armazenar na variável length_do_nome #função len e variável
print("O seu nome tem " + str(length_do_nome) + " letras.") # vai imprimir o tamanho do nome do usuário #print, concatenação e conversão


# Ordem de operações matemáticas: parênteses, exponenciação, multiplicação e divisão, adição e subtração.
# ()
# **
# * ou /  
# + ou -

print(3 * 3 + 3 / 3 - 3) # vai realizar as operações matemáticas na ordem correta #ordem de operações matemáticas
#a explicação da ordem de operações matemáticas é:
3 * 3 = 9 # multiplicação
3 / 3 = 1 # divisão
9 + 1 = 10 # adição
10 - 3 = 7 # subtração
# resultado final: 7.0


# função round() arredonda o número para o inteiro mais próximo
imc = 84 / 1.65 ** 2
imc = round(imc)
print(imc)
print(imc) # vai imprimir o valor do imc arredondado #print e arredondamento



# o uso de f-strings (formatted string literals) é uma forma de formatar strings de maneira mais fácil e legível.
# Ele permite inserir expressões dentro de strings, que são avaliadas em tempo de execução e substituídas pelo valor resultante.

altura = input("Qual é a sua altura em metros? ") # vai pedir para o usuário digitar a altura e armazenar na variável altura #input e variável
peso = input("Qual é o seu peso em kg? ") # vai pedir para o usuário digitar o peso e armazenar na variável peso #input e variável
imc = int(peso) / float(altura) ** 2 # vai calcular o imc e armazenar na variável imc #cálculo do imc
imc = round(imc) # vai arredondar o valor do imc #arredondamento
print(f"O seu IMC é {imc}") # vai imprimir o valor do imc usando f-string #print e f-string


print(6 + 4 / 2 - (1 * 2))


### projeto calculadora ###

print("Bem vindo à calculadora de gorjetas!")

conta = float(input("Qual é o valor da conta? \n")) # essa linha pede para o usuário digitar o valor da conta e armazena na variável conta
gorjeta = int(input("Qual é a porcentagem de gorjeta que você gostaria de dar? 10, 12 ou 15? \n")) # essa linha pede para o usuário digitar a porcentagem de gorjeta que ele gostaria de dar e armazena na variável gorjeta
pessoas = int(input("Quantas pessoas vão dividir a conta? \n")) # essa linha pede para o usuário digitar o número de pessoas que vão dividir a conta e armazena na variável pessoas
valor_da_gorjeta = conta * gorjeta / 100 # essa linha calcula o valor
total_da_conta = conta + valor_da_gorjeta # essa linha calcula o valor total da conta
valor_por_pessoa = total_da_conta / pessoas # essa linha calcula o valor que cada pessoa vai pagar
valor_por_pessoa = round(valor_por_pessoa, 2) # essa linha arredonda o valor que cada pessoa vai pagar para duas casas decimais
print(f"O valor que cada pessoa deve pagar é: R$ {valor_por_pessoa}") # essa linha imprime o valor que cada pessoa deve pagar usando f-string

