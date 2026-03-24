from abc import ABC, abstractmethod

class Account(ABC):
  def __init__(self, agencia, numero):
    self.agencia = agencia
    self.numero = numero
    self.saldo = 0

  def depositar(self, valor):
    try:
      if float(valor) <= 0:
        print("Você precisa adicionar um valor válido")
        return
      else:
        self.saldo += float(valor)
        print(f"Depósito realizado. Saldo atual: {self.saldo}")

    except ValueError:
      print('Adicione um valor numérico')

  @abstractmethod
  def sacar(self, valor):
    ...