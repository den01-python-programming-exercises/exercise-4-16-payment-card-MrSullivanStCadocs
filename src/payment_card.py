class PaymentCard:
  def __init__(self, opening_balance):
    self.opening_balance = opening_balance


  def __str__(self):
    return str("The card has a balance of " + str(self.opening_balance) + " pounds.")