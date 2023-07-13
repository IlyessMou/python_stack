from BankACCOUNT import BankAccount
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []
    # other methods
    def create_account(self, int_rate, balance=0):
        account = BankAccount(int_rate, balance)
        self.accounts.append(account)
    def make_deposit(self,amount,account_number):
        if account_number < len(self.accounts):
            account = self.accounts[account_number]
            account.deposit(amount)
        else:
            print("this account doesn't exist")
    def make_withdrawal(self,amount,account_number):
        if account_number < len(self.accounts):
            account = self.accounts[account_number]
            account.withdraw(amount)
        else:
            print("this account doesn't exist")
    def display_user_balance(self,account_number):
        if account_number < len(self.accounts):
            account = self.accounts[account_number]
            account.display_account_info()
        else:
            print("this account doesn't exist")
    def transfer_money(self, amount, other_user, sender_account_number, receiver_account_number):
        if ((sender_account_number < len(self.accounts)) and (receiver_account_number<len(other_user.accounts))):
            from_account = self.accounts[sender_account_number]
            to_account = other_user.accounts[receiver_account_number]
            if (from_account.balance>= amount):
                from_account.withdraw(amount)
                to_account.deposit(amount)
                print(f"Transfer of ${amount} from {self.name} to {other_user.name} successful.")
            else:
                print("You don't have enough Money!!")
        else:
            print("Invalid account number or user.")



    
    
    


