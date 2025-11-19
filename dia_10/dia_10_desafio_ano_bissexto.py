# Desafio Ano bissexto
# 💪 Esse é um desafio difícil! 💪
# Escreva um programa que retorne Verdadeiro ou Falso, mesmo que um determinado ano seja bissexto.
# Um ano normal tem 365 dias, anos bissextos têm 366, com um dia extra em fevereiro.

# É assim que você determina se um ano específico é um ano bissexto.
# - em todo ano que seja divisível por 4 sem resto
# - exceto em todos os anos que são divisíveis igualmente por 100 sem resto
# - a menos que o ano também seja divisível por 400 sem restante

# Se inglês não for sua primeira língua, ou se a lógica acima estiver confusa, tente usar este fluxograma.

# por exemplo, o ano 2000:
# 2000 ÷ 4 = 500 (Leap)  
# 2000 ÷ 100 = 20 (Not Leap)  
# 2000 ÷ 400 = 5 (Leap!)  
# Então, o ano 2000 é um ano bissexto.

# Mas o ano de 2100 não é um ano bissexto porque:
# 2100 ÷ 4 = 525 (Leap)  
# 2100 ÷ 100 = 21 (Not Leap)  
# 2100 ÷ 400 = 5.25 (Not Leap)  

# Aviso

# Seu retorno deve ser booleano e corresponder exatamente ao formato de Exemplo de Saída, incluindo ortografia e pontuação.

# Exemplo de Entrada 1
# 2400
# Exemplo de Retorno 1
# True

# Exemplo de Entrada 2
# 1989
# Exemplo Retorno 2
# False

# Como testar seu código e ver sua saída?
# Os exercícios de programação do Udemy não têm console, então você não pode usar essa função. Você precisará chamar sua função com valores codificados fixamente assim:input()

# def is_leap_year(year):
#   # your code here
 
# # Call your function with hard coded values
# is_leap_year(2024)

# Uma forma de fazer isso é usar a função print() para ver a saída do seu código. Por exemplo:

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(is_leap_year(2400))  # True
print(is_leap_year(1989))  # False
print(is_leap_year(2000))  # True
print(is_leap_year(2100))  # False

# Outra forma de fazer:

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
print(is_leap_year(2400))  # True
print(is_leap_year(1989))  # False
print(is_leap_year(2000))  # True
print(is_leap_year(2100))  # False
    
# A diferença é que aqui usamos uma única linha com operadores lógicos para verificar as condições de ano bissexto.
# Isso torna o código mais conciso e fácil de ler.

    