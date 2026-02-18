# Manipulando chaves e valores em dicionários
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}

# print(pessoa['nome'])

# del pessoa['sobrenome']

# print(pessoa)

# print(pessoa.get('sobrenome', 'teste'))

# print(pessoa)


# Métodos úteis dos dicionários em Python
# len -- quantas chaves
# keys -- iterável com as chaves
# values -- iterável com os valores
# items -- iterável com chaves e valores
# setdefault -- adiciona valor se a chave não existe
# copy -- retorna uma cópia rasa (shallow copy), não entra em subniveis, ultilizar a lib copy para copia profunda
# get -- obtém uma chave
# pop -- Apaga um item com a chave especificada (del)
# popitem -- Apaga o último item adicionado
# update -- Atualiza um dicionário com outro


# print(len(pessoa))

# print(list(pessoa.keys()))

# print(pessoa.keys())


# print(list(pessoa.values()))
# print(pessoa.values())


# print(list(pessoa.items()))
# print(pessoa.items())

# for chave, valor in pessoa.items():
#     print(chave, valor)


pessoa2 = pessoa.copy()

pessoa2['nome'] = 'Caio'


print(pessoa)
print(pessoa2)