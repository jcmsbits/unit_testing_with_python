import os
from unittest import TestCase
from src.bank_account import BankAccount

class BankAccountTest(TestCase):    
    # setUp se va a ejecutar cada vez para cada prueba
    # no se comparte el mismo objeto entre pruebas
    # en la misma clase se puede compartir lo que esté en setUp
    def setUp(self):        
        self.account = BankAccount(1000, log_file = "transaction_log.txt")

    # tearDown se va a ejecutar al finalizar cada prueba que se realice
    def tearDown(self):
        if os.path.exists(self.account.log_file):
            print("Despues de la ultima prueba")
            os.remove(self.account.log_file)
    
    # unittest tiene su propio assert personalizado
    def _count_lines(self, log_file):
        with open(log_file, "r") as f:
            return len(f.readlines())
        
    def test_deposit(self):
        new_balance = self.account.deposit(500)        
        # assert new_balance == 1500
        self.assertEqual(new_balance, 1500)

    def test_withdraw(self):
        new_balance = self.account.withdraw(200)        
        # assert new_balance == 800
        self.assertEqual(new_balance, 800)

    def test_get_balance(self):        
        # assert self.account.get_balance() == 1000
        self.assertEqual(self.account.get_balance(), 1000)

    def test_transfer_account(self):
        account = BankAccount(200)
        new_balance = self.account.transfer_account(account,100)
        # assert new_balance == 900
        self.assertEqual(new_balance, 900)

    def test_transaccion_log(self):
        self.account.deposit(500)
        print("ultima prueba")
        # assert os.path.exists("transaction_log.txt")
        self.assertTrue(os.path.exists("transaction_log.txt"))

    def test_count_transactions(self):
        # assert self._count_lines(self.account.log_file) == 1
        self.assertEqual(self._count_lines(self.account.log_file), 1)
        self.account.deposit(500)
        # assert self._count_lines(self.account.log_file) == 2
        self.assertEqual(self._count_lines(self.account.log_file), 2)

    def test_transfer_account(self):
        other_account = BankAccount(500)        
        with self.assertRaises(ValueError, msg = "No hubo error"):            
            self.account.transfer_account(other_account, 1100)