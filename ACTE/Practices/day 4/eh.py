
try:
    a = (input("Enter a name: "))
    b= int(input("Enter 2nd number: "))
    print(a+b)
except ValueError as e:
    print("Enter Integer value only",e)
except TypeError as e:
    print("Enter supported values" , e)
except Exception:
    print("Something Wrong")
finally:
    print("Done")
