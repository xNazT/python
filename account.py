class Account:
    
    def __init__(self, name):

        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        
"""adds a specific amount to account balance"""
        
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:

"""withdraw a specific amount from account balance"""
        
        if amount > 0:
            if amount <= self.__account_balance:
                self.__account_balance = self.__account_balance - amount

                return True
            else:
                return False
        else:
            return False

    def get_balance(self) -> float:

        """method to get the balance as a float"""
        
        return self.__account_balance

    def get_name(self) -> str:

        """method to get the account name as a string"""
        
        return self.__account_name
