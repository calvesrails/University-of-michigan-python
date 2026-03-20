# lista = [4, 34, 554, 65, 45362, 6, 6, 23]

# lista.sort()
# sorted(lista)

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# def ordena(item):
#   return item['nome']

lista.sort(key=lambda item: item['nome'])

print(lista)

