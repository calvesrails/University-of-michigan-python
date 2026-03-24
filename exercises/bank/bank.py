

class Bank:
  def __init__(self):
    self.agencias = ['999-01', '222-02', '333-03']
    self.clientes = ['Caio', 'João', 'Cauã']
    self.contas = ['01', '02', '03']

  # def autenticacao(self, agencia, cliente, conta):
  #   mensagem = []
  #   if agencia is not None:
  #     mensagem.append('Agencia não localizada') if agencia not in self.agencias else None
  #   else:
  #     print("Adicione uma agência para autenticar")
  #     return

  #   if cliente is not None:
  #     mensagem.append('Cliente não localizado') if cliente not in self.clientes else None
  #   else:
  #     print("Adicione um cliente para autenticar")
  #     return

  #   if conta is not None:
  #     mensagem.append('Conta não localizada') if conta not in self.contas else None
  #   else:
  #     print("Adicione uma conta para autenticar")
  #     return
  #   if any(mensagem):
  #     print(f'Erro na autenticação: {", ".join(mensagem)}')
  #   else:
  #     print('autenticação realizada com sucesso')

  def autenticacao(self, agencia, cliente, conta):
      campos = [
          ('agência', agencia, self.agencias, 'Agência não localizada'),
          ('cliente', cliente, self.clientes, 'Cliente não localizado'),
          ('conta', conta, self.contas, 'Conta não localizada'),
      ]

      mensagens = []

      for nome, valor, base, erro in campos:
          if valor is None:
              print(f'Adicione uma {nome} para autenticar')
              return False
          if valor not in base:
              mensagens.append(erro)

      if mensagens:
          print(f'Erro na autenticação: {", ".join(mensagens)}')
          return False

      print('Autenticação realizada com sucesso')
      return True

bank = Bank()

bank.autenticacao('999-01', 'Cai', '01')

