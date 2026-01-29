# 1)

class BookStore:

    NoOfBooks = 0

    def __init__(self, name, author):
        self.Name = name
        self.Author = author
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def Display(self):
        print(f"{self.Name} by {self.Author}. No of books : {self.NoOfBooks}")

obj1 = BookStore("Linux System Programming","Robert Love")
obj1.Display()

obj2 = BookStore("C Programming","Dennis Ritchie")
obj2.Display()


# 2)

class BankAccount:

    ROI = 10.5

    def __init__(self, name, amount):
        self.Name = name
        self.Amount = amount

    def Display(self):
        print("Account Holder:", self.Name)
        print("Current Balance:", self.Amount)

    def Deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.Amount = self.Amount + amount
        print(f"{amount} deposited successfully.")

    def Withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount <= self.Amount:
            self.Amount = self.Amount - amount
            print(f"{amount} withdrawn successfully.")
        else:
            print("Insufficient balance")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest

Obj1 = BankAccount("Parth",3000)
Obj1.Display()
Obj1.Deposit()
Obj1.Withdraw()
print("Interest :",Obj1.CalculateInterest())
Obj1.Display()


# 3)

class Numbers:

    def __init__(self):
        self.value = int(input("Enter a number: "))

    def ChkPrime(self):
        if self.value < 2:
            return False
        for i in range(2, int(self.value / 2) + 1):
            if self.value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        return self.value == self.SumFactors()
    
    def Factors(self):
            print(f"Factors of {self.value} are :")
            for i in range(1, self.value):
                if self.value % i == 0:
                    print(i)

    def SumFactors(self):
        sum_factor = 0
        for i in range(1, self.value):
            if self.value % i == 0:
                sum_factor = sum_factor + i
        return sum_factor


OBJ1 = Numbers()
OBJ2 = Numbers()

print("Number:", OBJ1.value)
print("Prime :", OBJ1.ChkPrime())
print("Perfect :", OBJ1.ChkPerfect())
OBJ1.Factors()
print("Sum of factors :", OBJ1.SumFactors())

print("Number:", OBJ2.value)
print("Prime :", OBJ2.ChkPrime())
print("Perfect :", OBJ2.ChkPerfect())
OBJ2.Factors()
print("Sum of factors :", OBJ2.SumFactors())