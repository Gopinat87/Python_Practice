def intrest_calci(amount,intrest,time) :
    return (amount*intrest*time)/ 100 

def total_intrest() :
    amount = float(input("Entet a Total amount: "))
    intrest = float(input("Enter Intrest: "))
    time = float(input("Enter time in Year: "))
    intrest_calculation = intrest_calci(amount,intrest,time)
    print(f"Your Total Intrest Amount is {intrest_calculation}")

total_intrest()

