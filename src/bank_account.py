class BankAccount:
    def __init__(self, balance = 0, log_file = None):
        self.balance = balance
        self.log_file = log_file
        self._log_transaction("Cuenta Creada")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._log_transaction(f"Deposited {amount}. New balance: {self.balance}")
        return self.balance
    
    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
            self._log_transaction(f"Withdraw {amount}. New balance: {self.balance}")
        return self.balance
    
    def get_balance(self):
        self._log_transaction(f"Checked balance. Current balance: {self.balance}")
        return self.balance
    
    def transfer_account(self, account, amount):

        if self.balance < amount:
            raise ValueError("No hay saldo suficiente")
            # self._log_transaction("No hay saldo disponible")
        self.balance -= amount
        account.deposit(amount)
        return self.balance

    def _log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(f"{message}\n")
        