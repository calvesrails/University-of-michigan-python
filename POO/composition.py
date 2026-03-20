# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

class Cliente:
  def __init__(self, nome):
    self.name = nome
    self.enderecos = []

  def inserir_endereco(self, rua, numero):
    self.enderecos.append(Endereco(rua, numero))

  def mostrar_enderecos(self):
    for endereco in self.enderecos:
      print(f'Nome: {endereco.rua}, Rua: {endereco.rua}')

  def __del__(self):
    print("APAGANDO,", self.name)

class Endereco:
  def __init__(self, rua, numero):
    self.rua = rua
    self.numero = numero

  def __del__(self):
    print("APAGANDO,", self.rua, self.numero)

cliente1 = Cliente('Maria')
cliente1.inserir_endereco('Rua tal', 322)
cliente1.inserir_endereco('Rua manga', 331)
cliente1.inserir_endereco('Rua laranja', 500)
cliente1.mostrar_enderecos()

del cliente1

print('Termina aqui')