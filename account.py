class account:

  def __init__ (self, name):

    self.__acount_name=name
    self.__acount_balance=0

  def deposit(self, amount):

    if amount>0:
      return True
    else:
      return False
  def withdraw(self,amount):

    if amount>0:
      if amount<=self.__account_balance:
        self.__account_balance=self.__account_balance-amount

        return True
      else:
        return False
    else:
      return False

  def getbalance(self):
    return self.account_balance

  def getname(self):
    return self.account_name
