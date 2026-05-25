rain=True
if rain:
    print("take a umbrella")
else:
    print("Rain varala Chill ah poo") 

rain=input("Rain Varutha ilaiya(yes/no): ")
if rain=="yes":
    print("take a umbrella")
else:
    print("Umbrella theva ila") 

rain=input("Ipo rain epdi iruku(heavy/light/no) :")
if rain=="heavy":
    print("Take Umbrella with rain coat")
elif rain=="light":
    print("Take Umbrella")
else:
    print("Rain varala Enjoy pannu") 
    
age=19
if age>=18:
    print("You can vote")
else:
    print("You are not eligible") 

age1=int(input("Enter Your Age"))
if age1>=18:
    print("you are eligible for vote")
else:
    print("sorry you cant't vote now")


Marks=int(input("Please enter your marks : "))
if Marks>=90:
    print("Excellant")
elif Marks>=60:
    print("Good")
elif Marks>=35:
    print("You Passed but Need to Improve")
else:
    print("you are fail")


num=int(input("Enter Any Number : "))
if num>0:
    print("Positive")
elif num<0:
    print("Negative")
else:
    print("Zero")

age=int(input("Enter Your Age :"))
if age>=20:
    print("You Are Adult")
elif age==19:
    print("you are enter into the adult")
elif age>13:
    print("Teen")
else:
    print("Child")

year=int(input("Enter year : "))
if year%400==0 and year%4==0 :
    print("This is Leap Year")
else:
    print("This is not leap year" )
