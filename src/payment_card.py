class PaymentCard:
  def __init__(self, opening_balance):
    self.opening_balance = opening_balance


  def __str__(self):
    return str("The card has a balance of " + str(self.opening_balance) + " pounds")

  def eat_affordably(self):
    if(self.opening_balance - 2.6 >= 0):
      self.opening_balance = float(self.opening_balance - 2.6)
    else:
      return self.opening_balance


  def eat_heartily(self):
    if(self.opening_balance - 4.6 >= 0):
      self.opening_balance = float(self.opening_balance - 4.6)
    else:
      return self.opening_balance

  def add_money(self,amount):
    self.amount = amount
    if(self.opening_balance +self.amount <0):
      return self.opening_balance
    elif(self.opening_balance + self.amount <= 150):
      self.opening_balance = self.opening_balance + self.amount
    else:
      self.opening_balance = 150

      