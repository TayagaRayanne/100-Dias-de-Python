### desafio do jogo FizzBuzz ###
# instruções:
# Escreva um programa que imprima os números de 1 a 100.
# Para múltiplos de três, imprima "Fizz" em vez do número.
# Para os múltiplos de cinco, imprima "Buzz".
# Para números que são múltiplos de três e cinco, imprima "FizzBuzz".

# O código está em inglês por que o curso original é nessa língua e alguns códigos devem ser entregues na IDE virtual em inglês.

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)