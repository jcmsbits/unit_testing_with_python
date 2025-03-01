import unittest, sys
from pprint import pprint
sys.path.append(".")

from tests.test_bank_account import BankAccountTest


def bank_account_suite():
    # Para ejecutar un conjunto de pruebas específicas usamos TestSuite
    # Para ejecutar esta Suite debemos ejecutar con algún runner
    suite = unittest.TestSuite()
    suite.addTest(BankAccountTest("test_deposit"))
    suite.addTest(BankAccountTest("test_withdraw"))

    return suite









if __name__ == "__main__":
    # Instanciamos el runner    
    runner = unittest.TextTestRunner()
    runner.run(bank_account_suite())