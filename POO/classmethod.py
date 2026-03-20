# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.
class Pessoa:
    ano = 2023  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def methodo_de_classe(cls):
      print('hey')

    @classmethod
    def criar_sem_nome(cls, idade):
      return cls('Anônima', idade)

    @classmethod
    def criar_com_50_anos(cls, nome):
      return cls(nome, idade=50)

p1 = Pessoa('João', 24)
p2 = Pessoa.criar_com_50_anos('Otavio')
p3 = Pessoa.criar_sem_nome(22)
# print(Pessoa.ano)
# Pessoa.methodo_de_classe()
print(p1.__dict__)
print(p2.__dict__)
print(p3.__dict__)