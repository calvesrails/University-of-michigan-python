# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
# python não tem sobrecarga de métodos
# ele tem Sobreposição de métodos (override)

from abc import ABC, abstractmethod

class Notificacao(ABC):
  def __init__(self, mensagem):
    self.mensagem = mensagem

  @abstractmethod
  def enviar(self) -> bool:
    ...

class NotificacaoSMS(Notificacao):
  def enviar(self) -> bool:
    print('SMS: enviando - ', self.mensagem)
    return True

class NotificacaoEmail(Notificacao):
  def enviar(self):
    print('E-Mail: enviando - ', self.mensagem)
    return True

def notificar(notificacao):
  notificacao_enviada = notificacao.enviar()

  if notificacao_enviada:
    print('Notificacao enviada')
  else:
    print('Notificação não enviada')


notificar(NotificacaoEmail('Testando e-mail'))
notificar(NotificacaoSMS('Testando SMS'))