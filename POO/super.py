# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class


# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super(MinhaString, self).upper()
#         print('DEPOIS DO UPPER')
#         return retorno


# string = MinhaString('Luiz')
# print(string.upper())

class A:
  atributo_a = 'Qualquer valor a '

  def metodo(self):
    print('A')

class B(A):
  atributo_b = 'Qualquer valor b'

  def metodo(self):
    print('B')
    super().metodo()

class C(B):
  atributo_c = 'Qualquer valor c'

  def metodo(self):
    print('C')
    super().metodo()


c = C()

print(c.atributo_a, c.atributo_b)
print(c.metodo())