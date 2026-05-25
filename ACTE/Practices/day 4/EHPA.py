def add_contact() :
    with open("contacts.txt","a")as f:
        name =input("Enter a name: ")
        number=input("Enter a number: ")
        email=input("Enter a Email: ")
        f.write(f"{name},{number},{email}\n")
    print("Contact info successfully added")

def view_contact():
    try:
        with open("contacts.txt","r") as f:
            print("Contact Records")
            for line in f:
                name,number,email = line.strip().split(",")
                print(f"\n Name : {name},\n Number: {number},\n Email {email}")
    except FileNotFoundError:
        print("Conatacts File not found")

while True:
    print("\n 1.Add Contact \n 2.View Contact \n 3.Exit")
    choice = input("Enter Choice : ")
    if choice == "1":
        add_contact()
    elif choice=="2":
        view_contact()
    elif choice=="3":
        break
    else :
        print("Invalid Choice")
