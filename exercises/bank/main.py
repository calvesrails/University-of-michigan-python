from account import Account
from savings_account import SavingsAccount
from checking_account import CheckingAccount
from bank import Bank

acc_corrente = CheckingAccount('999-01', '01')
autenticado = Bank().autenticacao(acc_corrente.agencia, 'ddd', acc_corrente.numero)
print(acc_corrente.__dict__)

acc_corrente.depositar(10.00)
print(acc_corrente.saldo)
acc_corrente.sacar(5.00, autenticado)
print(acc_corrente.saldo)