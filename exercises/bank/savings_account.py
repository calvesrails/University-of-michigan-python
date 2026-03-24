from account import Account

class SavingsAccount(Account):

  def sacar(self, valor, autenticado):
      if autenticado:
        try:
            valor = float(valor)
            if valor <= 0:
                print("Informe um valor maior que zero.")
                return

            if valor > self.saldo:
                print("Saldo insuficiente.")
                return

            self.saldo -= valor
            print(f"Saque realizado. Saldo atual: {self.saldo}")

        except ValueError:
            print("Adicione um valor numérico.")
      else:
        None