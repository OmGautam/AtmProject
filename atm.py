class atm(object):
    def __init__(self,cardNumber,pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
    
    def cashWithdrawal(self):
        print("Cash Withdrawed")
    
    def cashEntry():
        print("Cash Entered")

user = atm("$15","1234")

print(user.cardNumber)