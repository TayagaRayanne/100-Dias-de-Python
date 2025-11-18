### loop for ###
# este bloco é dedicado ao loop for em python

# fruits = ["apple", "peach", "pear"]
# for fruit in fruits: # enquanto houver frutas na lista fruits, ele irá repetir o bloco printando cada fruta.
#     print(fruit)
#     print(fruit + " pie")


### esse código abaixo é uma lista de scores de estudantes em um exame:

# student_scores = [150, 200, 250, 300, 350, 400, 450]
# total_exam_score = sum(student_scores)

# sum = 0
# for score in student_scores:
#     sum += score
# print(f"O total de score é: {sum}")



### outra forma de fazer:

# student_scores = [150, 200, 250, 300, 350, 400, 450]
# max_score = 0

# for score in student_scores:
#     if score > max_score:
#         max_score = score
# print(f"O maior score é: {max_score}")


### loop for com o comando range() ###
total = 0
for number in range(1, 101): # O range cria uma lista de números de 1 a 100. Ele começa do 1 e vai até 101, mas não inclui o 101.
    total += number # essa linha soma todos os números dessa lista
print(total)