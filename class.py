class Account:
    
    def __init__(self,balance,account_no):
        self.balance= balance
        self.account_no = account_no

    def credit(self,amount):
        self.balance += amount
        print(f"The amount {amount} is credited to your account,{self.account_no}")
        print("total_balance = ",self.get_balance())
        
    
    def debit(self,amount):
         self.balance -= amount
         print(f"The amount {amount} is debited from your account,{self.account_no}")
         print("total_balance = ",self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(1000,"asad123")
acc1.debit(100)
