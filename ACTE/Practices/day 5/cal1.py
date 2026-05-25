class Calculator:
    def add(self):
        a = int(input("Enter 1st value: "))
        b = int(input("Enter 2nd value: "))
        return a + b

calci = Calculator()
result = calci.add()
print("Sum =", result)


