### Programa de Classificação (Grading Program) ###

# Você tem acesso a um banco de dados de student_scores (pontuações dos alunos) no formato de um dicionário. As keys (chaves) em student_scores são os nomes dos alunos e os values (valores) são as pontuações de seus exames.
# Escreva um programa que converte suas pontuações em notas (grades).
# Ao final do seu programa, você deve ter um novo dicionário chamado student_grades que deve conter os nomes dos alunos como keys e suas notas avaliadas como values.
# A versão final do dicionário student_grades será verificada.
# NÃO modifique as linhas 1 a 7 para alterar o dicionário student_scores existente.

# Este é o critério de pontuação:

# Pontuações de 91 a 100: Grade = "Outstanding" (Excepcional)
# Pontuações de 81 a 90: Grade = "Exceeds Expectations" (Excede as Expectativas)
# Pontuações de 71 a 80: Grade = "Acceptable" (Aceitável)
# Pontuações de 70 ou menos: Grade = "Fail" (Reprovado)


student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score >= 91:
        student_grades[student] = "Outstanding"
    elif score >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif score >= 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
        
print(student_grades)