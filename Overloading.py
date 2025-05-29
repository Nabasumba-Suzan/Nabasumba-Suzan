class ATM:
    def withdraw(self, amount=None):
        if amount is None:
            print("Withdrawing default amount of 10,000 UGX")
        else:
            print(f"Withdrawing {amount} UGX")

atm = ATM()
atm.withdraw()
atm.withdraw(50000)
