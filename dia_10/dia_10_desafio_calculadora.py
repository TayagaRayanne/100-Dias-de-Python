### Desafio Calculadora ###
# Este desafio envolve a criação de uma calculadora simples que pode realizar operações básicas como adição, subtração, multiplicação e divisão.

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def apresentar_calculadora():
    print("Bem-vindo à Calculadora!")
    for symbol in operations:
        print(symbol)
    num1 = float(input("Digite o primeiro número: "))
    should_continue = True
    while should_continue:
        operation_symbol = input("Escolha uma operação: ")
        num2 = float(input("Digite o próximo número: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"\nO resultado da sua operação: {num1} {operation_symbol} {num2} = {answer}\n")
        if input(f"Digite 's' para continuar calculando com esse resultado '{answer}', ou qualquer outra tecla para sair e reiniciar a calculadora: ") == 's':
            num1 = answer
        else:
            should_continue = False
            apresentar_calculadora()
            
apresentar_calculadora()

    



#my_favorite_operation = 