class bankaccount :
    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance 

    def deposit(self,amount) :
        self.balance += amount
        print(f"{amount} Deposited succesfully")
    
    def withdraw(self,amount) :
        if amount > self.balance :
            print(f"Insufficient Balance")
        else :
            self.balance -= amount
            print(f"{amount}.Rs/ Withdraw Successfull")
            
    def blance(self):
        print(f"Current Balance : {self.balance}")
name = input("Enter your Name : ")
account = bankaccount(name,1000)

while True :
    print("\n1. Deposit")
    print("2. withdraw")
    print("3. Balance")
    print("4. Exit")

    choice = input("Choose Option: ")

    if choice == "1" :
        amount = int(input("Enter a Amount: "))
        account.deposit(amount)
    
    elif choice == "2" :
        amount = int(input("Enter Withdraw Amount: "))
        account.withdraw(amount)

    elif choice == "3":
        account.blance()
    
    elif choice == "4" :
        print("Thank you for Banking")
        break
    else :
        print("Invalid Choice")
