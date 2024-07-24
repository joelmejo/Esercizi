# Progettare un semplice sistema bancario con i seguenti requisiti:

#     Classe del Account:
#         Attributi:
#             account_id: str - identificatore univoco per l'account.
#             balance: float - il saldo attuale del conto.
#         Metodi:
#             deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
#             get_balance(): restituisce il saldo corrente del conto.
#     Classe Bank:
#         Attributi:
#             accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
#         Metodi:
#             create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
#             deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
#             get_balance(account_id): restituisce il saldo del conto con l'ID specificato.

bank = Bank()
account1 = bank.create_account("123")
print(account1.get_balance())

	
# Expected
# 0

bank = Bank()
account1 = bank.create_account("123")
bank.deposit("123",100)
print(bank.get_balance("123"))

	
# Expected
# 100

bank = Bank()
account2 = bank.create_account("456")
bank.deposit("456",200)
print(bank.get_balance("456"))

	
# Expected
# 200