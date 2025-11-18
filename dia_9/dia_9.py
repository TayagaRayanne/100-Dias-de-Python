programing_dicionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                        "Function": "A piece of code that you can easily call over and over again.",
                        "Loop": "The action of doing something over and over again.",
                        }

# print(programing_dicionary["Bug"])

# Um dicionário é uma coleção de pares chave-valor. Cada valor é acessado através de sua chave única.
# Neste exemplo, "Bug", "Function" e "Loop" são as chaves, e suas definições correspondentes são os valores.
# Você pode adicionar novos pares chave-valor ao dicionário, modificar valores existentes ou excluir pares conforme necessário.
# Diferente de listas ou tuplas, os dicionários não mantêm uma ordem específica dos elementos.
# Eles são ideais para armazenar dados que precisam ser acessados rapidamente por uma chave única.

### Aninhamento de Dicionários (Nesting Dictionaries) ###
# Dicionários podem conter outros dicionários, listas ou outros tipos de dados como valores

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesse caso, cada país é uma chave e sua capital é o valor associado.

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

print(travel_log["France"]["cities_visited"][0]) # Primeiro seleciono Travel_log, depois France e por fim o indice da cidade que quero acessar.

# Nesse exemplo, o dicionário travel_log contém outros dicionários como valores.
# Cada país é uma chave, e o valor associado é outro dicionário que contém informações detalhadas sobre as cidades visitadas e o total de visitas.
